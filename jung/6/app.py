from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import google.generativeai as genai  # Google AI for Gemini

app = Flask(__name__, template_folder='templates')  # 'myweb/templates' 대신 'templates' 사용
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Gemini API 키 설정 (안전하게 관리해야 함!)
GENAI_API_KEY = "AIzaSyBK1CPlrVCCXfjxFuMt_F2h0zW1embq3Ws"  # 실제 API 키로 대체
genai.configure(api_key=GENAI_API_KEY)

# Gemini 모델 설정 (원하는 모델 선택)
MODEL_NAME = "gemini-1.5-flash"  # 또는 다른 모델 이름
generation_config = {
    #"max_output_tokens": 200,  # 답변 최대 길이
    "temperature": 0.9,       # 창의성 조절 (0.0 ~ 1.0)
    "top_p": 1.0             # 확률 분포 기반 샘플링
}
# 안전 설정을 위한 새로운 방법
# 안전 설정을 위한 새로운 방법
safety_settings = [
    {
        "category": "harassment",
        "threshold": "block_medium_and_above"
    },
    {
        "category": "hate_speech",
        "threshold": "block_medium_and_above"
    },
    {
        "category": "sexually_explicit",
        "threshold": "block_medium_and_above"
    }
]

model = genai.GenerativeModel(
    model_name=MODEL_NAME,
    generation_config=generation_config,
    safety_settings=safety_settings
)




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='user_posts', lazy=True)
    comments = db.relationship('Comment', backref='user_comments', lazy=True)
    bulletin_posts = db.relationship('BulletinPost', backref='user_bulletin_posts', lazy=True)  # BulletinPost 연결

    def __repr__(self):
        return f'<User {self.username}>'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', backref='written_posts', lazy=True)
    comments = db.relationship('Comment', backref='post_comments', cascade='all, delete-orphan', lazy=True)

    def __repr__(self):
        return f'<Post {self.title}>'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post = db.relationship('Post', backref='comment_set', cascade='all', lazy=True)  # backref 이름 변경
    author = db.relationship('User', backref='authored_comments', lazy=True)

    def __repr__(self):
        return f'<Comment {self.id}>'


# 새로운 게시판 모델
class BulletinPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', backref='written_bulletin_posts', lazy=True)

    def __repr__(self):
        return f'<BulletinPost {self.title}>'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    # 최근 게시글을 BulletinPost 모델에서 불러오도록 수정
    recent_posts = BulletinPost.query.order_by(BulletinPost.date_posted.desc()).limit(5).all()
    return render_template('index.html', recent_posts=recent_posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "이미 사용 중인 사용자 이름입니다."
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))  # 수정됨: 회원가입 후 홈페이지로 리디렉션
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))  # 수정됨: 로그인 후 홈페이지로 리디렉션
        else:
            return '로그인 실패'
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/board')
@login_required
def board():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('board.html', posts=posts)


@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = Post(title=title, content=content, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('board'))
    return render_template('new_post.html')


@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('view.html', post=post)


@app.route('/post/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        return '접근 권한이 없습니다.'
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        return redirect(url_for('view_post', post_id=post.id))
    return render_template('edit_post.html', post=post)


@app.route('/post/delete/<int:post_id>')
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        return '접근 권한이 없습니다.'
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('board'))


@app.route('/post/<int:post_id>/comment', methods=['POST'])
@login_required
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    content = request.form['content']
    if content:
        comment = Comment(content=content, post=post, author=current_user)
        db.session.add(comment)
        db.session.commit()
    return redirect(url_for('view_post', post_id=post_id))


@app.route('/bulletin')
def bulletin_board():
    posts = BulletinPost.query.order_by(BulletinPost.date_posted.desc()).all()
    return render_template('bulletin_board.html', posts=posts)


@app.route('/bulletin/new', methods=['GET', 'POST'])
@login_required
def new_bulletin_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = BulletinPost(title=title, content=content, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('bulletin_board'))
    return render_template('new_bulletin_post.html')


@app.route('/bulletin/<int:post_id>')
def view_bulletin_post(post_id):
    post = BulletinPost.query.get_or_404(post_id)
    return render_template('view_bulletin_post.html', post=post)


@app.route('/test')
def test_image():
    return render_template('test.html')


@app.route('/building/<int:id>')
def building_page(id):
    # id가 1~99 사이일 때만 처리 (필요시 예외 처리 가능)
    if not (1 <= id <= 99):
        return "존재하지 않는 건물입니다.", 404

    template_name = f'building/B{id:02d}.html'  # building/B01.html, B02.html
    return render_template(template_name)


@app.route('/gemini-search', methods=['POST'])
def gemini_search():
    data = request.get_json()
    query = data.get('query')

    try:
        # Gemini API 호출
        response = model.generate_content(query)
        gemini_results = response.text
    except Exception as e:
        gemini_results = f"Gemini 검색 오류: {str(e)}"

    return jsonify({'result': gemini_results})


class BulletinComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    bulletin_post_id = db.Column(db.Integer, db.ForeignKey('bulletin_post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bulletin_post = db.relationship('BulletinPost', backref='comments', lazy=True)
    author = db.relationship('User', backref='bulletin_comments', lazy=True)

    def __repr__(self):
        return f'<BulletinComment {self.id}>'

@app.route('/bulletin/<int:post_id>/comment', methods=['POST'])
@login_required
def add_bulletin_comment(post_id):
    post = BulletinPost.query.get_or_404(post_id)
    content = request.form.get('content')

    if content:
        comment = BulletinComment(content=content, bulletin_post=post, author=current_user)
        db.session.add(comment)
        db.session.commit()
    
    return redirect(url_for('view_bulletin_post', post_id=post_id))



with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)