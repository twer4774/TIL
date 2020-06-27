# Authentication(인증)

## 인증절차

1. 회원가입
2. 사용자의 아이디와 비밀번호를 저장. 비밀번호는 암호화(단방향해시 이용)
3. 사용자의 로그인
4. 로그인시 이용된 비밀번호를 암호화하여 DB에 저장되어 있는 해시함수 결과값과 비교
5. 로그인 성공 시 API서버는 acceess token발급

### 비밀번호 암호화

- 외부 해킹 및 내부 DB 접근자로 인한 피해 예방

- 단방향 해시함수로 암호화

  - 복호화가 굉장히 어렵다
    - Rainbow attack이라는 해킹 기술 이용
    - 해시가 검색할 때 빠르다는 점을 이용하여 미리 해시테이블을 만들고 맞추는 작업을 함
    - bcrypt 암호 알고리즘의 탄생
  - 원본 데이터를 알면 간단히 알 수 있다

- 파이썬 모듈 - hashlib

- ```python
   import hashlib
   m = hashlib.sha256() #sha256암호 알고리즘
   m.update(b"test password") #b는 binary로 인코딩하기 위한 prefix
   m.hexdigest() #암호화된 값을 hex(16진수)로 표시
  
  '0b47c69b1033498d5f33f5f7d97bb6a3126134751629f4d0185c115db44c094e'
  ```

### bcrypt 알고리즘

- key setup phase 라는 일종의 막대한 전처리 요구로 느리게 만든 Blowfish란 녀석의 특징에 반복횟수를 변수로 지정가능하게 하여 해싱시간을 조절할 수 있게 함
- salting
  - 실제 비밀번호 + 랜덤 데이터 => 해시
  - 개발자도 어떠한 salt를 썼는지 모름
- key stretching
  - 기존 단방향 해시 알고리즘드르이 실행속도가 너무 빠르다는 취약점을 보완하기 위해 단방향 해시값을 계산하고 그 해시값을 또 해시하여 여러번 해시 값을 계산하는 것

```
pip install bcrypt
```

```python
import bcrypt
bcrypt.hashpw(b"secrete password", bcrypt.gensalt())
b'$2b$12$hElZMbAI7r030apc2JQi6.r/.JLWNNo7E8RebNpkC1GXBmJM7/h.2'
#16진수
 bcrypt.hashpw(b"secrete password", bcrypt.gensalt()).hex()
'243262243132243665395966566d62737868754f71784f6b433230792e346e4b6e5a63546157696f4e667157444d50704d73516c6a6d4377387a4847'
```

## access token

- Front end -> Back end : 사용자의 access token을 HTTP Request에 첨부해서 서버에 전송

- HTTP는 stateless

  - 이전에 어떤 HTTP 통신을 했는지 모름
  - => HTTP 통신을 할때는 해당 HTTP Request를 처리하기 위해서 필요한 모든 데이터를 첨부해서 요청
  - 로그인 정보 또한 HTTP 요청에 첨부해서 보내야 API 서버에서 해당 사용자가 이미 로그인 된 상태임을 알 수 있음 ==> access token : 사용자의 로그인 정보
  - API 서버에서 사용자의 로그인 정보를 access token형태로 생성하여 프론트엔드 서버로 전송하면 프론트엔드 서버는 access token을 그대로 다시 백엔드 서버에 HTTP요청을 보낼 때 첨부하여 전송
  - =>> 결론적으로 access token 정보를 가지고 로그인상태를 확인한다.

- access token 생성방법

  - JWT(JSON Web Tokens)
    - 프론트엔드에서 HTTP Request(회원가입 ID, PW)
    - 백엔드에서 사용자 아이디 생성(user_id)
    - 생성된 user_id를 access token으로 변환
    - 프론트엔드는 쿠키등에 access token을 저장하고 있다가 해당 사용자를 위한 HTTP Request를 백엔드로 보낼때 access token을 첨부하여 보냄
    - 백엔드는 access token을 복호화해서 JSON 데이터를 얻음(user_id)
  - JWT의 구조
    - header : 토큰 타입, 해시알고리즘 지정
    - payload : 데이터부분
    - signature : JWT가 원본 그대로라는 것을 확인할 때 사용되는 부분

- PyJWT

  ```
  pip install PyJWT
  ```

  ```python
  >>> import jwt
  >>> data_to_encode = {'some': 'payload'}
  >>> encryption_secret = 'secret'
  >>> algorithm = 'HS256'
  #암호화
  >>> encoded = jwt.encode(data_to_encode, encryption_secret, algorithm=algorithm)
  #복호화
  >>> jwt.decode(encoded, encryption_secret, algorithms=[algorithm])
  {'some': 'payload'}
  ```

  