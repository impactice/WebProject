from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os # os 모듈을 임포트합니다.
from dotenv import load_dotenv # load_dotenv 함수를 임포트합니다.

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

# 1. Flask 애플리케이션 인스턴스 생성
app = Flask(__name__, template_folder='templates')
# os.getenv()를 사용하여 환경 변수에서 SECRET_KEY를 가져옵니다.
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'default_fallback_key' # SECRET_KEY 환경 변수가 없으면 'default_fallback_key'를 사용 (개발용)

# 2. SQLALCHEMY_DATABASE_URI 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. SQLAlchemy 인스턴스 초기화
db = SQLAlchemy(app)

# Flask-Login 설정
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# ... (이하 나머지 코드는 동일) ...

# 4. 데이터베이스 모델 정의
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # email = db.Column(db.String(120), unique=True, nullable=False) # <--- 이 줄이 주석 처리되었거나 없어야 합니다.
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# 로그인 관리 (Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# 루트 페이지 (홈페이지)
@app.route('/')
def index():
    return render_template('index.html') # templates 폴더의 index.html을 렌더링합니다.


# 회원 가입 페이지
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "이미 사용 중인 사용자 이름입니다."
        new_user = User(username=username, password=hashed_password) # <--- username과 password만 전달
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

# 로그인 페이지
# 로그인 페이지
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))  # <--- 'index'를 'home'으로 수정
        else:
            return '로그인 실패: 사용자 이름 또는 비밀번호가 올바르지 않습니다.'
    return render_template('login.html') 

# 로그아웃 처리
@app.route('/logout')
@login_required
def logout():
    logout_user()  # 로그아웃 처리
    return redirect(url_for('index')) 

# 5. 애플리케이션 컨텍스트 내에서 데이터베이스 테이블 생성
with app.app_context():
    db.create_all()


# 7. 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=8000, debug=True)  # 호스트와 포트를 지정하여 실행할 경우