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

