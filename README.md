# WebProject 

## 이거는 터미널에서 까는 것 그리고 python 다운 받는 거 포함 
- 1. 파이썬을 설치한다
![image](https://github.com/user-attachments/assets/0fcc364f-71fd-4854-b4cf-00055a0c482a)

- 2. 다운로드에 들어가면 
![image](https://github.com/user-attachments/assets/0008980f-0a65-492b-b9a3-2e118d861aa2)

- 이런 파일이 있다 이것을 클릭을 하면 
![image](https://github.com/user-attachments/assets/4cee3f76-a67e-490e-91a2-6de79f2fa8b9)

- 이런 화면이 뜬다 
- 둘다 체크를 해준다 (PATH는 무조건)
![image](https://github.com/user-attachments/assets/dc7e14ce-412b-4cf8-8815-9a3949ee2ad5)

- 그리고 Install Now를 클릭을 해준다 
![image](https://github.com/user-attachments/assets/0e93238b-a2e8-4ba6-9a5b-5ae3e002a4a4)

- 3. WINDOW키와 R키를 누른 다음 cmd를 누른다
![image](https://github.com/user-attachments/assets/0d415544-ad26-47e9-b832-1e88e6a5bc53)

- 확인을 누르면 
![image](https://github.com/user-attachments/assets/b8436623-6245-4f35-90b3-0f34ec1e8e25)

- 터미널이 열린다 

- 4. 터미널 
- 파이썬이 설치 되었있는지 알아보기 위해 
- python --version
- 을 터미널에 입력을 한다 

![image](https://github.com/user-attachments/assets/053e7a4b-3aea-4205-b198-2230c2fadb87)

- 제대로 설치가 되었다 

- 가상환경 설정 (선택사항이지만 권장됨 vscode로 할 거면 필요 없음)
```
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
```
- 5. flask 설치 
- 그 다음 flask를 설치를 하겠다
- pip install flask를 터미널에 입력을 하면
```
pip install flask
```
![image](https://github.com/user-attachments/assets/6a3c714e-fc7a-45ff-a42e-66a62e1c98fa)

- 설치 확인
```
python -m flask --version
```
![image](https://github.com/user-attachments/assets/bcfa65cd-4fb2-45f9-a550-3cfcff8a3986)

- 만약 설치할 때 pip가 안 된다면(중요 이거 안 되면 다음 단계들 다 안됨)
![image](https://github.com/user-attachments/assets/2bf4eb17-a923-4ea4-8b4f-b32af307c310)

- 이렇게 뜬다면 
- 이는 pip가 설치되어 있지 않거나, 시스템 환경 변수(PATH)에 등록되지 않았기 때문이다

- 명령 프롬프트에서 다음 명령어 입력: 
    ```
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    ```
![image](https://github.com/user-attachments/assets/e91ec098-96ce-47de-b51a-86bfa38de6b0)
```
python get-pip.py
```

![image](https://github.com/user-attachments/assets/3a08be23-dcdb-4409-ac7a-e1a67193d7bc)


## vscode로 까는 Flask (일단 임시)

- 1번
![image](https://github.com/user-attachments/assets/34d0db4b-3766-493d-86b4-e71f9fbdbbb2) 

- 2번
![image](https://github.com/user-attachments/assets/44c33bd0-0879-4356-b559-545703a7fdfb)

- 3번
![image](https://github.com/user-attachments/assets/8756fd42-5af7-4a37-af56-8d51eb0f2dc0)

- 4번
![image](https://github.com/user-attachments/assets/7bc41176-1549-4bc0-831e-f5a301fa8072)

- 5번
![image](https://github.com/user-attachments/assets/2e6a4ce6-71ba-4fbd-8106-89d796d0b32f)

- 6번
![image](https://github.com/user-attachments/assets/3eaf8a0c-a307-4992-bf0b-6d84adbd55d8)

- 7번
![image](https://github.com/user-attachments/assets/fb6e9e26-b018-4398-966b-67e33254101b)

- 8번
![image](https://github.com/user-attachments/assets/d6c9113a-3414-45c8-bdf5-a1dbee59a650)

- 9번 
![image](https://github.com/user-attachments/assets/855f5d46-5113-48b0-a580-45b98d02fd8d)

- 10번
![image](https://github.com/user-attachments/assets/504711fc-34d2-4ee3-9911-0873f444520b)

- 11번
![image](https://github.com/user-attachments/assets/425801c8-1bc4-409f-983f-8b3ba499593c)

- 12번
![image](https://github.com/user-attachments/assets/a86a6e39-ac91-4e73-a354-ee48219b1750)

- 13번
![image](https://github.com/user-attachments/assets/02083a46-2824-4845-a9ab-646e74ff4e6b)

- 14번
![image](https://github.com/user-attachments/assets/749b4748-6ad8-44a0-8308-4c97b703a765)

- 15번
![image](https://github.com/user-attachments/assets/c8cb63e7-e8e3-4c6c-8a18-675cdf9ca5f0)

- 16번 
![image](https://github.com/user-attachments/assets/b3a949bf-1959-41f9-afff-6e4dc5e01cfb)

- 17번
![image](https://github.com/user-attachments/assets/ac0842fc-a231-4767-ba71-2d0c10e9cebb)

- 18번
![image](https://github.com/user-attachments/assets/d3afdbfe-dedb-4a70-8b43-593e66bf2089)

- 19번
![image](https://github.com/user-attachments/assets/f442a555-d226-4719-9d4d-ba9572bf7fe7)


## 웹 프로그래밍하다가 깔아야 되는 pip 
- 이거는 Flask에 sql (오류 화면)
![image](https://github.com/user-attachments/assets/12afe5e6-a2d2-406f-a57e-b3d5cb77e895)
```
pip install Flask-SQLAlchemy
```
- 이거는 설치
![image](https://github.com/user-attachments/assets/2692da16-4c1e-45f8-a348-151081531d1a)

```
pip install Flask-SQLAlchemy
```
- 이거는 확인
![image](https://github.com/user-attachments/assets/5b94866d-7c8f-4b1f-aaeb-31d2988bee04)

```
pip show Flask-SQLAlchemy
```

- Flask-Login을 설치
![image](https://github.com/user-attachments/assets/e3b9ce4a-0bf9-4f84-946a-01c62f16e513)

- 설치
![image](https://github.com/user-attachments/assets/cd2db99a-58cd-4c3f-9eb5-eb9fd56ef5d3)

```
pip install Flask-Login
```
- 확인
![image](https://github.com/user-attachments/assets/5f85fdfd-56ad-49c5-a432-42851716098e)

```
pip show Flask-Login
```

## 데이터베이스를 보게 하기 위한 앱
![image](https://github.com/user-attachments/assets/b8ea30a7-75f6-4a67-a8b5-77ce5903f73d)

- 이거는 SQLite를 안 깔을 때 보이는 거
![image](https://github.com/user-attachments/assets/5e7db420-a2cf-44dd-a88c-f1ef43594dc8)

<test> readme수정 <test>

## ai api 
- 안 깔면
![image](https://github.com/user-attachments/assets/1ffa21f2-b9e7-46df-9a56-9cba1d3299f7)
```
pip install google-generativeai
```
- 다운 받는 것이 길이가 너무 길어서 임의로 짤랐음
![image](https://github.com/user-attachments/assets/c68f2a04-b015-4108-b21f-85d7c4eb09b3)

```
myweb/
├── app.py
├── .env
├── templates/
│   ├── index.html
│   ├── bulletin_board.html
│   ├── edit_post.html
│   ├── login.html
│   ├── new_bulletin_post.html
│   ├── new_post.html
│   ├── register.html
│   ├── view.html
│   ├── view_bulletin_post.html
│   ├── building/
│   │   ├── B01.html
│   │   ├── B26.html
│   │   └── B27.html
│   └── board.html
├── static/            # 정적 파일
│   ├── buildingC/
│   │   └── B01.css
│   ├── images/
│   │   └── ...
│   ├── board.css
│   ├── bulletin_board.css
│   ├── image_slider.css
│   ├── image_slider.js
│   ├── style.css
│   └── view.css
└── instance/          # 데이터베이스 파일 (database.db)
    └── database.db 
```
    pip 패키지는 다음과 같습니다:

- Flask
- Flask-SQLAlchemy
- Werkzeug (보안 관련 기능: generate_password_hash, check_password_hash) - Flask 설치 시 함께 설치될 가능성이 높습니다.
- Flask-Login
- google-generativeai
- Authlib
- python-dotenv
따라서 다음 명령어로 필요한 패키지들을 설치할 수 있습니다:
```
pip install Flask Flask-SQLAlchemy Flask-Login google-generativeai Authlib python-dotenv
```


# `app.py` 핵심 코드 설명

이 `app.py` 파일은 Flask 프레임워크를 사용하여 웹 애플리케이션을 구축한 코드입니다. 주요 기능은 사용자 인증 (일반 로그인 및 Google OAuth), 게시판 기능, 댓글 기능, 건물 정보 페이지 제공, 그리고 Gemini AI 모델을 활용한 검색 기능입니다.

## 1. 필요한 라이브러리 import

```python
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import google.generativeai as genai
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()
```

- os: 운영 체제 관련 기능 제공 (예: 환경 변수 접근).
- flask: 웹 프레임워크 Flask 관련 클래스 및 함수 제공.
    - Flask: Flask 애플리케이션 객체 생성.
    - render_template: HTML 템플릿 렌더링.
    - request: 클라이언트로부터의 요청 데이터 접근.
    - redirect: 특정 URL로 리디렉션.
    - url_for: 특정 함수에 대한 URL 생성.
    - jsonify: JSON 응답 생성.
    - session: 사용자 세션 관리.
- flask_sqlalchemy: Flask에서 SQLAlchemy를 쉽게 사용하도록 지원.
    - SQLAlchemy: ORM(Object-Relational Mapping) 도구.
- datetime: 날짜 및 시간 관련 기능 제공.
- werkzeug.security: 비밀번호 해싱 및 검증 관련 기능 제공.
    - generate_password_hash: 비밀번호 해시 생성.
    - check_password_hash: 해시된 비밀번호 검증.
- flask_login: 사용자 로그인 관리 기능 제공.
    - LoginManager: 로그인 관리자 클래스.
    - UserMixin: 사용자 모델에 필요한 속성 및 메서드 제공.
    - login_user: 사용자 로그인 처리.
    - logout_user: 사용자 로그아웃 처리.
    - login_required: 로그인된 사용자만 접근 가능한 뷰 함수 데코레이터.
    - current_user: 현재 로그인된 사용자 정보 접근.
- google.generativeai: Google의 Gemini AI 모델 사용을 위한 라이브러리.
- authlib.integrations.flask_client: OAuth 클라이언트 구현을 위한 라이브러리.
    - OAuth: OAuth 클라이언트 관리 클래스.
- dotenv: .env 파일에서 환경 변수를 로드하는 라이브러리

# 2. Flask 애플리케이션 설정 
```
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# .env 파일에서 시크릿 키를 로드합니다.
app.secret_key = os.getenv('SECRET_KEY')
if not app.secret_key:
    raise ValueError("SECRET_KEY 환경 변수가 설정되지 않았습니다. .env 파일을 확인하세요. (예: python -c \"import os; print(os.urandom(24).hex())\" 로 생성)")

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
```
- Flask 애플리케이션 객체를 생성하고, 템플릿 폴더를 'templates'로 설정합니다.
- SQLAlchemy를 사용하여 SQLite 데이터베이스 (database.db) 연결을 설정합니다.
- SQLAlchemy의 변경 추적 기능을 비활성화합니다.
- .env 파일에서 Flask 애플리케이션의 보안에 중요한 SECRET_KEY를 로드합니다.
- SQLAlchemy 객체 db를 생성하여 데이터베이스 작업을 관리합니다.
- Flask-Login의 LoginManager를 초기화하고, 로그인 뷰를 설정합니다

# 3. Google OAuth 2.0 설정
```
# Google OAuth 2.0 설정
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

# 디버깅: 클라이언트 ID와 시크릿이 제대로 로드되었는지 확인 (서버 시작 시 터미널에 출력됨)
print(f"DEBUG: Loaded GOOGLE_CLIENT_ID: {'*' * (len(GOOGLE_CLIENT_ID) - 10) + GOOGLE_CLIENT_ID[-10:] if GOOGLE_CLIENT_ID else 'None'}")
print(f"DEBUG: Loaded GOOGLE_CLIENT_SECRET: {'*' * (len(GOOGLE_CLIENT_SECRET) - 5) if GOOGLE_CLIENT_SECRET else 'None'}")


CONF_URL = '[https://accounts.google.com/.well-known/openid-configuration](https://accounts.google.com/.well-known/openid-configuration)'

oauth = OAuth(app)

oauth.register(
    name='google',
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    server_metadata_url=CONF_URL,
    client_kwargs={'scope': 'openid email profile'},
)
```
- .env 파일에서 Google OAuth 클라이언트 ID와 시크릿을 로드합니다.
- Authlib의 OAuth 객체를 초기화하고 Google OAuth 설정을 등록합니다

# 4. Gemini API 설정
```
# Gemini API 키 설정 (안전하게 관리해야 함!)
GENAI_API_KEY = os.getenv("GENAI_API_KEY")
genai.configure(api_key=GENAI_API_KEY)

MODEL_NAME = "gemini-1.5-flash"
generation_config = {
    "temperature": 0.9,
    "top_p": 1.0
}
safety_settings = [
    {"category": "harassment", "threshold": "block_medium_and_above"},
    {"category": "hate_speech", "threshold": "block_medium_and_above"},
    {"category": "sexually_explicit", "threshold": "block_medium_and_above"}
]
model = genai.GenerativeModel(
    model_name=MODEL_NAME,
    generation_config=generation_config,
    safety_settings=safety_settings
)
```
- .env 파일에서 Gemini API 키를 로드하고, genai 라이브러리를 설정합니다.
- 사용할 Gemini 모델, 생성 설정, 안전 설정을 정의하고 모델 객체를 생성합니다

# 5. 데이터베이스 모델 정의
```
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=True)
    google_id = db.Column(db.String(120), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    profile_picture = db.Column(db.String(255), nullable=True)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='user_posts', lazy=True)
    comments = db.relationship('Comment', backref='user_comments', lazy=True)
    bulletin_posts = db.relationship('BulletinPost', backref='user_bulletin_posts', lazy=True)

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
    post = db.relationship('Post', backref='comment_set', cascade='all', lazy=True)
    author = db.relationship('User', backref='authored_comments', lazy=True)

    def __repr__(self):
        return f'<Comment {self.id}>'

class BulletinPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', backref='written_bulletin_posts', lazy=True)

    def __repr__(self):
        return f'<BulletinPost {self.title}>'

```
- SQLAlchemy 모델 클래스를 정의하여 데이터베이스 테이블 구조를 나타냅니다 (User, Post, Comment, BulletinPost) 

# 6. Flask-Login 사용자 로더 
```
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```
- Flask-Login이 사용자 세션을 관리하는 데 필요한 콜백 함수입니다

# 7. 라우팅 및 뷰 함수
```
@app.route('/')
def index():
    recent_posts = BulletinPost.query.order_by(BulletinPost.date_posted.desc()).limit(5).all()
    return render_template('index.html', recent_posts=recent_posts, current_user=current_user)

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
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            return '로그인 실패: 사용자 이름 또는 비밀번호가 올바르지 않습니다.'
    return render_template('login.html')

@app.route('/login/google')
def google_login():
    redirect_uri = url_for('google_authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

# --- 수정된 Google 로그인 콜백 처리 부분 (nonce 추가) ---
@app.route('/callback')
def google_authorize():
    try:
        # 이 단계에서 문제가 발생하는지 확인하기 위해 각 호출 전후에 print 추가
        print(f"\n--- Google OAuth Callback Debug ---")
        print(f"DEBUG: Attempting to authorize access token...")
        token = oauth.google.authorize_access_token() # 이 줄에서 오류가 발생할 가능성 높음
        print(f"DEBUG: Token acquired: {token}")

        print(f"DEBUG: Attempting to parse ID token...")
        # Authlib 1.0.0 이상에서는 nonce를 parse_id_token()에 명시적으로 전달해야 함
        # nonce는 authorize_redirect()에서 Authlib이 세션에 자동으로 저장함
        user_info = oauth.google.parse_id_token(token, nonce=session.get('nonce')) # <-- 이 부분 수정!
        print(f"DEBUG: ID token parsed: {user_info}")

        # 나머지 디버깅 print 문 및 로직은 그대로 유지
        print(f"  - Google ID (sub): {user_info.get('sub')}")
        print(f"  - Email: {user_info.get('email')}")
        print(f"  - Name: {user_info.get('name')}")
        print(f"  - Profile Picture: {user_info.get('picture')}")

        google_id = user_info.get('sub')
        user = User.query.filter_by(google_id=google_id).first()
        print(f"DEBUG: User lookup by google_id '{google_id}': {'Found' if user else 'Not Found'}")

        if not user:
            email = user_info.get('email')
            username_candidate = email if email else f"google_user_{google_id}"
            existing_user_by_username = User.query.filter_by(username=username_candidate).first()
            existing_user_by_email = User.query.filter_by(email=email).first()

            print(f"DEBUG: New user path: Proposed username: '{username_candidate}'")
            if existing_user_by_username or existing_user_by_email:
                username = f"google_{google_id}"
                print(f"DEBUG: Conflict detected, modified username to: '{username}')")
                if existing_user_by_email and existing_user_by_email.google_id != google_id:
                    email = None
            else:
                username = username_candidate

            user = User(
                username=username,
                google_id=google_id,
                email=email,
                profile_picture=user_info.get('picture')
            )
            db.session.add(user)
            db.session.commit()
            print(f"DEBUG: New user created in DB: {user}")

        login_user(user)
        print(f"DEBUG: User '{user.username}' (ID: {user.id}) logged in successfully via Google.")
        print(f"--- Google OAuth Callback Debug End ---\n")
        return redirect(url_for('index'))

    except Exception as e:
        print(f"\n!!! CRITICAL ERROR during Google OAuth callback: {e} !!!\n")
        raise e

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
    post = Post.query.get_or_40
```
- 이거는 app.py 주석을 단 버전
```
import os # 운영 체제와 상호작용하기 위한 모듈 (예: 환경 변수 접근)
from flask import Flask, render_template, request, redirect, url_for, jsonify, session # Flask 웹 프레임워크의 핵심 기능들 임포트
from flask_sqlalchemy import SQLAlchemy # Flask에서 SQLAlchemy를 쉽게 사용할 수 있도록 돕는 확장
from datetime import datetime # 날짜와 시간을 다루기 위한 모듈
from werkzeug.security import generate_password_hash, check_password_hash # 비밀번호 해싱 및 검증을 위한 유틸리티
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user # Flask-Login을 이용한 사용자 인증 관리
import google.generativeai as genai # Google Gemini AI 모델을 사용하기 위한 라이브러리
from authlib.integrations.flask_client import OAuth # OAuth 클라이언트 구현을 위한 Authlib 라이브러리
from dotenv import load_dotenv # .env 파일에서 환경 변수를 로드하기 위한 라이브러리

# .env 파일 로드: 애플리케이션에 필요한 환경 변수 (예: API 키, 비밀 키)를 로드합니다.
load_dotenv()

# Flask 애플리케이션 인스턴스 생성
# __name__은 현재 모듈의 이름을 나타내며, Flask가 리소스(템플릿, 정적 파일)를 찾는 데 사용됩니다.
# template_folder='templates'는 HTML 템플릿 파일이 'templates' 디렉토리에 있음을 명시합니다.
app = Flask(__name__, template_folder='templates')

# SQLAlchemy 데이터베이스 URI 설정: SQLite 데이터베이스 'database.db'를 사용하도록 설정합니다.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# SQLAlchemy 이벤트 시스템 추적을 비활성화합니다. 메모리 사용량을 줄일 수 있습니다.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 애플리케이션의 비밀 키 설정: 세션 관리, CSRF 보호 등 보안 관련 기능에 사용됩니다.
# 환경 변수에서 SECRET_KEY를 로드하며, 설정되지 않았다면 오류를 발생시킵니다.
app.secret_key = os.getenv('SECRET_KEY')
if not app.secret_key:
    raise ValueError("SECRET_KEY 환경 변수가 설정되지 않았습니다. .env 파일을 확인하세요. (예: python -c \"import os; print(os.urandom(24).hex())\" 로 생성)")

# SQLAlchemy 데이터베이스 객체 초기화: Flask 애플리케이션과 연동하여 ORM 기능을 제공합니다.
db = SQLAlchemy(app)

# Flask-Login LoginManager 인스턴스 생성 및 초기화
login_manager = LoginManager()
login_manager.init_app(app)
# 로그인되지 않은 사용자가 @login_required 데코레이터가 붙은 페이지에 접근 시 리디렉션될 로그인 뷰를 지정합니다.
login_manager.login_view = 'login'

# Google OAuth 2.0 클라이언트 ID 및 시크릿 로드
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

# 디버깅 목적으로 로드된 Google 클라이언트 ID와 시크릿의 일부를 출력합니다.
# 실제 값 전체가 노출되지 않도록 일부만 표시합니다.
print(f"DEBUG: Loaded GOOGLE_CLIENT_ID: {'*' * (len(GOOGLE_CLIENT_ID) - 10) + GOOGLE_CLIENT_ID[-10:] if GOOGLE_CLIENT_ID else 'None'}")
print(f"DEBUG: Loaded GOOGLE_CLIENT_SECRET: {'*' * (len(GOOGLE_CLIENT_SECRET) - 5) if GOOGLE_CLIENT_SECRET else 'None'}")

# Google OpenID Connect Discovery 문서 URL
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'

# Authlib OAuth 객체 생성
oauth = OAuth(app)

# Google OAuth 클라이언트 등록
# 'google'이라는 이름으로 OAuth 클라이언트를 등록하며, Google의 인증 서버 정보를 사용합니다.
# client_kwargs={'scope': 'openid email profile'}는 Google로부터 요청할 사용자 정보의 범위를 지정합니다.
# 'openid': OpenID Connect를 사용함을 나타냅니다.
# 'email': 사용자의 이메일 주소에 대한 접근 권한을 요청합니다.
# 'profile': 사용자의 기본 프로필 정보(이름, 프로필 사진 등)에 대한 접근 권한을 요청합니다.
oauth.register(
    name='google',
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    server_metadata_url=CONF_URL,
    client_kwargs={'scope': 'openid email profile'},
)

# Gemini API 키 설정: 환경 변수에서 Gemini API 키를 로드하고 genai 라이브러리를 구성합니다.
GENAI_API_KEY = os.getenv("GENAI_API_KEY")
genai.configure(api_key=GENAI_API_KEY)

# Gemini 모델 설정
MODEL_NAME = "gemini-1.5-flash" # 사용할 Gemini 모델의 이름
generation_config = {
    "temperature": 0.9, # 생성할 텍스트의 무작위성(창의성)을 조절합니다. 값이 높을수록 더 무작위적입니다.
    "top_p": 1.0 # 토큰 선택 시 누적 확률 임계값을 설정합니다.
}
safety_settings = [ # 생성될 콘텐츠의 안전성 필터링 설정
    {"category": "harassment", "threshold": "block_medium_and_above"}, # 괴롭힘 관련 콘텐츠 필터링
    {"category": "hate_speech", "threshold": "block_medium_and_above"}, # 혐오 발언 관련 콘텐츠 필터링
    {"category": "sexually_explicit", "threshold": "block_medium_and_above"} # 성적으로 노골적인 콘텐츠 필터링
]
# Gemini GenerativeModel 인스턴스 생성: 위에서 정의한 설정들을 적용합니다.
model = genai.GenerativeModel(
    model_name=MODEL_NAME,
    generation_config=generation_config,
    safety_settings=safety_settings
)

# 데이터베이스 모델 정의
# SQLAlchemy의 db.Model을 상속받아 데이터베이스 테이블과 매핑되는 클래스를 정의합니다.
# UserMixin을 상속받아 Flask-Login이 사용자 객체를 인식하고 관리하는 데 필요한 속성과 메서드를 제공합니다.
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # 사용자 고유 ID (기본 키)
    username = db.Column(db.String(80), unique=True, nullable=False) # 사용자 이름 (고유하며 필수)
    password = db.Column(db.String(120), nullable=True) # 비밀번호 (해시된 형태로 저장, 일반 로그인 시 사용)
    google_id = db.Column(db.String(120), unique=True, nullable=True) # Google OAuth ID (고유하며 선택 사항)
    email = db.Column(db.String(120), unique=True, nullable=True) # 이메일 주소 (고유하며 선택 사항)
    profile_picture = db.Column(db.String(255), nullable=True) # 프로필 사진 URL (선택 사항)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow) # 가입일 (기본값은 현재 UTC 시간)
    # 다른 모델과의 관계 정의 (역참조 설정)
    posts = db.relationship('Post', backref='user_posts', lazy=True) # 이 사용자가 작성한 일반 게시글들
    comments = db.relationship('Comment', backref='user_comments', lazy=True) # 이 사용자가 작성한 댓글들
    bulletin_posts = db.relationship('BulletinPost', backref='user_bulletin_posts', lazy=True) # 이 사용자가 작성한 공지 게시글들

    # 객체를 문자열로 표현할 때 사용되는 메서드
    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True) # 게시글 고유 ID (기본 키)
    title = db.Column(db.String(100), nullable=False) # 게시글 제목 (필수)
    content = db.Column(db.Text, nullable=False) # 게시글 내용 (필수, Text 타입은 긴 문자열에 적합)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow) # 게시글 작성일 (기본값은 현재 UTC 시간)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # 작성자 User의 ID (외래 키, 필수)
    # User 모델과의 관계 정의 (Post의 작성자)
    author = db.relationship('User', backref='written_posts', lazy=True)
    # Comment 모델과의 관계 정의 (이 게시글에 달린 댓글들)
    # cascade='all, delete-orphan': 게시글이 삭제되면 해당 게시글의 모든 댓글도 함께 삭제됩니다.
    comments = db.relationship('Comment', backref='post_comments', cascade='all, delete-orphan', lazy=True)

    def __repr__(self):
        return f'<Post {self.title}>'

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True) # 댓글 고유 ID (기본 키)
    content = db.Column(db.Text, nullable=False) # 댓글 내용 (필수)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow) # 댓글 작성일 (기본값은 현재 UTC 시간)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False) # 댓글이 달린 Post의 ID (외래 키, 필수)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # 댓글 작성자 User의 ID (외래 키, 필수)
    # Post 모델과의 관계 정의 (댓글이 속한 게시글)
    # cascade='all': 부모 객체(Post)가 삭제될 때 자식 객체(Comment)도 함께 삭제됩니다.
    post = db.relationship('Post', backref='comment_set', cascade='all', lazy=True)
    # User 모델과의 관계 정의 (댓글 작성자)
    author = db.relationship('User', backref='authored_comments', lazy=True)

    def __repr__(self):
        return f'<Comment {self.id}>'

class BulletinPost(db.Model):
    id = db.Column(db.Integer, primary_key=True) # 공지 게시글 고유 ID (기본 키)
    title = db.Column(db.String(100), nullable=False) # 공지 게시글 제목 (필수)
    content = db.Column(db.Text, nullable=False) # 공지 게시글 내용 (필수)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow) # 공지 게시글 작성일 (기본값은 현재 UTC 시간)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # 작성자 User의 ID (외래 키, 필수)
    # User 모델과의 관계 정의 (공지 게시글 작성자)
    author = db.relationship('User', backref='written_bulletin_posts', lazy=True)

    def __repr__(self):
        return f'<BulletinPost {self.title}>'

# Flask-Login 사용자 로더 함수
# 세션에 저장된 사용자 ID(user_id)를 기반으로 데이터베이스에서 사용자 객체를 로드합니다.
# Flask-Login이 사용자 세션을 관리하는 데 필수적입니다.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# 라우팅 및 뷰 함수 정의

# 메인 페이지 라우트
@app.route('/')
def index():
    # 데이터베이스에서 가장 최근에 작성된 공지 게시글 5개를 조회합니다.
    recent_posts = BulletinPost.query.order_by(BulletinPost.date_posted.desc()).limit(5).all()
    # 'index.html' 템플릿을 렌더링하고, 조회된 최근 게시글과 현재 로그인 사용자 정보를 전달합니다.
    return render_template('index.html', recent_posts=recent_posts, current_user=current_user)

# 회원 가입 페이지 라우트 (GET: 페이지 표시, POST: 회원 가입 처리)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST': # POST 요청인 경우 (폼 제출)
        username = request.form['username'] # 폼에서 사용자 이름 가져오기
        password = request.form['password'] # 폼에서 비밀번호 가져오기
        hashed_password = generate_password_hash(password) # 비밀번호를 해싱하여 저장 (보안 강화)
        existing_user = User.query.filter_by(username=username).first() # 이미 존재하는 사용자 이름인지 확인
        if existing_user:
            return "이미 사용 중인 사용자 이름입니다." # 중복된 사용자 이름인 경우 메시지 반환
        new_user = User(username=username, password=hashed_password) # 새 User 객체 생성
        db.session.add(new_user) # 데이터베이스 세션에 추가
        db.session.commit() # 변경사항 커밋 (데이터베이스에 저장)
        return redirect(url_for('login')) # 회원 가입 성공 후 로그인 페이지로 리디렉션
    return render_template('register.html') # GET 요청인 경우 회원 가입 템플릿 렌더링

# 로그인 페이지 라우트 (GET: 페이지 표시, POST: 로그인 처리)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': # POST 요청인 경우 (폼 제출)
        username = request.form['username'] # 폼에서 사용자 이름 가져오기
        password = request.form['password'] # 폼에서 비밀번호 가져오기
        user = User.query.filter_by(username=username).first() # 데이터베이스에서 사용자 이름으로 사용자 조회
        # 사용자가 존재하고 비밀번호가 일치하는지 확인
        if user and check_password_hash(user.password, password):
            login_user(user) # Flask-Login을 사용하여 사용자 로그인 처리 (세션에 사용자 정보 저장)
            return redirect(url_for('index')) # 로그인 성공 후 메인 페이지로 리디렉션
        else:
            return '로그인 실패: 사용자 이름 또는 비밀번호가 올바르지 않습니다.' # 로그인 실패 메시지 반환
    return render_template('login.html') # GET 요청인 경우 로그인 템플릿 렌더링

# Google 로그인 시작 라우트
@app.route('/login/google')
def google_login():
    # Google OAuth 인증 후 콜백될 URI를 생성합니다. _external=True는 절대 경로를 생성합니다.
    redirect_uri = url_for('google_authorize', _external=True)
    # Authlib의 authorize_redirect 메서드를 사용하여 Google 인증 페이지로 사용자를 리디렉션합니다.
    # 이 과정에서 Authlib은 nonce(일회용 토큰)를 세션에 저장하여 Replay Attack을 방지합니다.
    return oauth.google.authorize_redirect(redirect_uri)

# Google 로그인 콜백 처리 라우트
# Google 인증 서버로부터 인증 코드를 받아 사용자 정보를 처리합니다.
@app.route('/callback')
def google_authorize():
    try:
        print(f"\n--- Google OAuth Callback Debug ---")
        print(f"DEBUG: Attempting to authorize access token...")
        # Authlib의 authorize_access_token 메서드를 사용하여 액세스 토큰을 교환합니다.
        # 이 단계에서 Google과의 통신 오류가 발생할 수 있습니다.
        token = oauth.google.authorize_access_token()
        print(f"DEBUG: Token acquired: {token}")

        print(f"DEBUG: Attempting to parse ID token...")
        # ID 토큰을 파싱하여 사용자 정보를 추출합니다.
        # Authlib 1.0.0 이상에서는 세션에 저장된 nonce를 명시적으로 전달해야 합니다.
        user_info = oauth.google.parse_id_token(token, nonce=session.get('nonce'))
        print(f"DEBUG: ID token parsed: {user_info}")

        # 추출된 사용자 정보 디버깅 출력
        print(f"  - Google ID (sub): {user_info.get('sub')}")
        print(f"  - Email: {user_info.get('email')}")
        print(f"  - Name: {user_info.get('name')}")
        print(f"  - Profile Picture: {user_info.get('picture')}")

        google_id = user_info.get('sub') # Google 고유 사용자 ID
        user = User.query.filter_by(google_id=google_id).first() # Google ID로 기존 사용자 조회
        print(f"DEBUG: User lookup by google_id '{google_id}': {'Found' if user else 'Not Found'}")

        if not user: # 기존 사용자가 없는 경우 (새로운 Google 로그인 사용자)
            email = user_info.get('email') # Google에서 제공하는 이메일
            username_candidate = email if email else f"google_user_{google_id}" # 이메일이 있으면 사용자 이름 후보로 사용, 없으면 Google ID 기반으로 생성
            existing_user_by_username = User.query.filter_by(username=username_candidate).first() # 사용자 이름 후보로 기존 사용자 확인
            existing_user_by_email = User.query.filter_by(email=email).first() # 이메일로 기존 사용자 확인

            print(f"DEBUG: New user path: Proposed username: '{username_candidate}'")
            # 사용자 이름 또는 이메일이 이미 사용 중인 경우
            if existing_user_by_username or existing_user_by_email:
                username = f"google_{google_id}" # 충돌을 피하기 위해 Google ID를 포함한 사용자 이름 생성
                print(f"DEBUG: Conflict detected, modified username to: '{username}')")
                # 이메일이 이미 다른 Google ID와 연결되어 있다면 해당 이메일은 사용하지 않음
                if existing_user_by_email and existing_user_by_email.google_id != google_id:
                    email = None
            else:
                username = username_candidate # 충돌이 없으면 사용자 이름 후보 사용

            # 새 User 객체 생성 및 데이터베이스에 추가
            user = User(
                username=username,
                google_id=google_id,
                email=email,
                profile_picture=user_info.get('picture')
            )
            db.session.add(user)
            db.session.commit()
            print(f"DEBUG: New user created in DB: {user}")

        login_user(user) # 새롭거나 기존 사용자 로그인 처리
        print(f"DEBUG: User '{user.username}' (ID: {user.id}) logged in successfully via Google.")
        print(f"--- Google OAuth Callback Debug End ---\n")
        return redirect(url_for('index')) # 로그인 성공 후 메인 페이지로 리디렉션

    except Exception as e: # OAuth 처리 중 오류 발생 시 예외 처리
        print(f"\n!!! CRITICAL ERROR during Google OAuth callback: {e} !!!\n")
        raise e # 오류를 다시 발생시켜 디버깅을 돕습니다.

# 로그아웃 라우트 (로그인된 사용자만 접근 가능)
@app.route('/logout')
@login_required # 이 데코레이터는 로그인된 사용자만 이 함수에 접근할 수 있도록 합니다.
def logout():
    logout_user() # Flask-Login을 사용하여 사용자 로그아웃 처리 (세션에서 사용자 정보 제거)
    return redirect(url_for('index')) # 로그아웃 후 메인 페이지로 리디렉션

# 일반 게시판 페이지 라우트 (로그인된 사용자만 접근 가능)
@app.route('/board')
@login_required
def board():
    # 모든 게시글을 작성일 기준으로 내림차순(최신순)으로 조회합니다.
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    # 'board.html' 템플릿을 렌더링하고, 조회된 게시글 목록을 전달합니다.
    return render_template('board.html', posts=posts)

# 새 게시글 작성 페이지 및 처리 라우트 (로그인된 사용자만 접근 가능)
@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST': # POST 요청인 경우 (폼 제출)
        title = request.form['title'] # 폼에서 제목 가져오기
        content = request.form['content'] # 폼에서 내용 가져오기
        # 새 Post 객체 생성: 제목, 내용, 현재 로그인된 사용자를 작성자로 설정
        post = Post(title=title, content=content, author=current_user)
        db.session.add(post) # 데이터베이스 세션에 추가
        db.session.commit() # 변경사항 커밋
        return redirect(url_for('board')) # 게시글 작성 후 게시판 페이지로 리디렉션
    return render_template('new_post.html') # GET 요청인 경우 새 게시글 작성 템플릿 렌더링

# 특정 게시글 상세 보기 페이지 라우트
# <int:post_id>는 URL 경로에서 정수형 게시글 ID를 인자로 받습니다.
@app.route('/post/<int:post_id>')
def view_post(post_id):
    # post_id에 해당하는 게시글을 데이터베이스에서 조회합니다. 없으면 404 오류를 반환합니다.
    post = Post.query.get_or_404(post_id)
    # 'view.html' 템플릿을 렌더링하고, 조회된 게시글 객체를 전달합니다.
    return render_template('view.html', post=post)

# 게시글 수정 페이지 및 처리 라우트 (로그인된 게시글 작성자만 접근 가능)
@app.route('/post/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id) # 수정할 게시글 조회
    # 현재 로그인된 사용자가 게시글의 작성자가 아니면 접근 권한 없음 메시지 반환
    if post.author != current_user:
        return '접근 권한이 없습니다.'
    if request.method == 'POST': # POST 요청인 경우 (폼 제출)
        post.title = request.form['title'] # 폼에서 새 제목 가져와 업데이트
        post.content = request.form['content'] # 폼에서 새 내용 가져와 업데이트
        db.session.commit() # 변경사항 커밋
        return redirect(url_for('view_post', post_id=post.id)) # 수정 후 게시글 상세 페이지로 리디렉션
    return render_template('edit_post.html', post=post) # GET 요청인 경우 게시글 수정 템플릿 렌더링

# 게시글 삭제 처리 라우트 (로그인된 게시글 작성자만 접근 가능)
@app.route('/post/delete/<int:post_id>')
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id) # 삭제할 게시글 조회
    # 현재 로그인된 사용자가 게시글의 작성자가 아니면 접근 권한 없음 메시지 반환
    if post.author != current_user:
        return '접근 권한이 없습니다.'
    db.session.delete(post) # 데이터베이스 세션에서 게시글 삭제
    db.session.commit() # 변경사항 커밋
    return redirect(url_for('board')) # 삭제 후 게시판 페이지로 리디렉션

# 댓글 추가 처리 라우트 (로그인된 사용자만 접근 가능)
@app.route('/post/<int:post_id>/comment', methods=['POST'])
@login_required
def add_comment(post_id):
    post = Post.query.get_or_404(post_id) # 댓글을 추가할 게시글 조회
    content = request.form['content'] # 폼에서 댓글 내용 가져오기
    if content: # 내용이 비어있지 않은 경우에만 댓글 추가
        # 새 Comment 객체 생성: 내용, 대상 게시글, 현재 로그인된 사용자를 작성자로 설정
        comment = Comment(content=content, post=post, author=current_user)
        db.session.add(comment) # 데이터베이스 세션에 추가
        db.session.commit() # 변경사항 커밋
    return redirect(url_for('view_post', post_id=post_id)) # 댓글 추가 후 게시글 상세 페이지로 리디렉션

# 공지 게시판 페이지 라우트
@app.route('/bulletin')
def bulletin_board():
    # 모든 공지 게시글을 작성일 기준으로 내림차순(최신순)으로 조회합니다.
    posts = BulletinPost.query.order_by(BulletinPost.date_posted.desc()).all()
    # 'bulletin_board.html' 템플릿을 렌더링하고, 조회된 공지 게시글 목록을 전달합니다.
    return render_template('bulletin_board.html', posts=posts)

# 새 공지 게시글 작성 페이지 및 처리 라우트 (로그인된 사용자만 접근 가능)
@app.route('/bulletin/new', methods=['GET', 'POST'])
@login_required
def new_bulletin_post():
    if request.method == 'POST': # POST 요청인 경우 (폼 제출)
        title = request.form['title'] # 폼에서 제목 가져오기
        content = request.form['content'] # 폼에서 내용 가져오기
        # 새 BulletinPost 객체 생성: 제목, 내용, 현재 로그인된 사용자를 작성자로 설정
        post = BulletinPost(title=title, content=content, author=current_user)
        db.session.add(post) # 데이터베이스 세션에 추가
        db.session.commit() # 변경사항 커밋
        return redirect(url_for('bulletin_board')) # 공지 게시글 작성 후 공지 게시판으로 리디렉션
    return render_template('new_bulletin_post.html') # GET 요청인 경우 새 공지 게시글 작성 템플릿 렌더링

# 특정 공지 게시글 상세 보기 페이지 라우트
@app.route('/bulletin/<int:post_id>')
def view_bulletin_post(post_id):
    # post_id에 해당하는 공지 게시글을 데이터베이스에서 조회합니다. 없으면 404 오류를 반환합니다.
    post = BulletinPost.query.get_or_404(post_id)
    # 'view_bulletin_post.html' 템플릿을 렌더링하고, 조회된 공지 게시글 객체를 전달합니다.
    return render_template('view_bulletin_post.html', post=post)

# 건물 정보 페이지 라우트
# <int:id>는 URL 경로에서 정수형 건물 ID를 인자로 받습니다.
@app.route('/building/<int:id>')
def building_page(id):
    # 건물 ID가 1에서 99 사이인지 유효성 검사
    if not (1 <= id <= 99):
        return "존재하지 않는 건물입니다.", 404 # 유효하지 않은 ID면 404 오류와 메시지 반환
    # 건물 ID에 해당하는 HTML 템플릿 파일 이름을 생성합니다 (예: B01.html, B10.html).
    template_name = f'building/B{id:02d}.html'
    # 해당 템플릿을 렌더링합니다.
    return render_template(template_name)

# Gemini 검색 API 엔드포인트 (POST 요청 처리)
@app.route('/gemini-search', methods=['POST'])
def gemini_search():
    data = request.get_json() # 클라이언트로부터 JSON 형식의 요청 데이터 가져오기
    query = data.get('query') # 요청 데이터에서 'query' 값 추출 (사용자 검색어)
    try:
        # Gemini 모델을 사용하여 검색 쿼리에 대한 콘텐츠를 생성합니다.
        response = model.generate_content(query)
        gemini_results = response.text # 생성된 텍스트 결과
    except Exception as e: # Gemini API 호출 중 오류 발생 시 예외 처리
        gemini_results = f"Gemini 검색 오류: {str(e)}" # 오류 메시지 생성
    # 검색 결과를 JSON 형식으로 클라이언트에 반환합니다.
    return jsonify({'result': gemini_results})

# 애플리케이션 컨텍스트 내에서 데이터베이스 테이블 생성
# 이 부분은 애플리케이션이 처음 실행될 때 데이터베이스 스키마를 생성하는 데 사용됩니다.
with app.app_context():
    db.create_all()

# 애플리케이션 실행
# 이 스크립트가 직접 실행될 때 (import되지 않고) Flask 개발 서버를 시작합니다.
# debug=True: 디버그 모드를 활성화하여 코드 변경 시 자동 재로드 및 상세한 오류 메시지를 제공합니다.
if __name__ == '__main__':
    app.run(debug=True)

```
