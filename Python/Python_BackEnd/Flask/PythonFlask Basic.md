# Python Back-End

## 1. 환경설정

- python3.7 기준

- 가상환경 설치 - miniconda 이용

  - https://docs.conda.io/en/latest/miniconda.html

- Git 및 관련 툴 설치

  - Git 설치 

    - brew install git
    - git config —global user.name "name"
    - git config —global user.email "email"

  - Git 관련 툴

    - TIG(Text-mode Interface fot Git)
      - brew install tig => 깃 커밋 히스토리를 터미널에서 보여줌. git log와 동일하지만 보기 편함
    - Diff So Fancy => 설치후 셋팅필요
      - brew install diff-so-fancy => git diff 출력화면을 터미널 상에 쉽게 출력해줌

  - Shell : 사용자의 명령어를 운영체제에 전달하여 실행되게 하고, 그 결과물을 사용자에게 전달하는 역할 

    - Bash or ZSH

      - ZSH 설치

        - brew install zsh zsh-completions

      - ZSH 디폴트 셀로 변경

        - ```
          sudo -s echo 'usr/local/bin/zsh >> /etc/shells'
          =>> 안되면 sudo nano /etc/shells에 /usr/local/bin/zsh 추가
          
      chsh -s /usr/local/bin/zsh
          
      재시작 후 echo $SHELL 로 경로 확인
          ```
    
    - Oh My Zsh
    
      - ZSH의 설정관리 툴
      
      - ```
        sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
        ```
      
      - 설정
      
        ```
        nano ~/.zshrc
        plugin에 zsh-syntax-highlighting, history-substring-search 입력
        ```
  
- 가상환경 생성

  ```
  conda create --name api python=3.7
  ```

- 가상환경 활성화

- ```
  source activate api
  source deactivate
  conda env list => 생성된 가상환경 리스트
  ```

- Flask 설치(가상환경에 진행)

  ```
  pip install flask
  ```

- 폴더생성

- ```
  mkdir -p Project/Python-Flask-API
  -p옵션 : 중간경로의 디렉터리가 없으면 자동생성
  ```

## 2. 엔드포인트 : 통신채널

- ping 엔드포인트 만들기(가상환경)

  ```python
  #app.py - nano app.py
  
  from flask import Flask
  
  app = Flask(__name__)
  
  @app.route("/ping", methods=['GET'])
  def ping():
    	return "pong"
  ```

- httpie : 터미널환경에서 http명령어 실행

  - 설치 

    ```
    brew install httpie
    ```

    현재 크롬 restapi확장프로그램 이용(Talend API Tester)

- 실행

  ```
  FLASK_APP=app.py FLASK_DEBUG=1 flask run
  
  #FLASK_DEBUG=1 설정 시 디버그모드 => 소스가 변경되어도 재시작 안해도 됨
  위의 명령은 product로 실행됨
  
  #개발자모드로 실행. 디버그도 실행됨
  FLASK_ENV=development FLASK_APP=app.py flask run
  
  
  http -v GET http://localhost:5000/ping
  ```

  