# 라즈베리파이에 도커레지스트리허브 만들기

### 환경

- Raspberry pi2(Wifi 리시버 장착)
- 32GB SD카드

[라즈베리파이 모니터 강제연결 - 참고용]

- https://its55.tistory.com/118

[RaspberryImager를 이용하면 잘 됨]

[ssh로 접속하기]

- 추후에 포트포워딩으로 외부에서 접속이 가능하도록 해야 함 - 192.168.0.1 (iptime 기준)

```
ssh pi@192.168.0.24
```

## 한글처리, 키보드 처리

- 한글처리

```
sudo apt-get install fonts-unfonts-core
```

- 키보드 키가 잘 동작하지 않을 때
  - 모니터를 연결하면 메뉴 설정에서 아래 키보드로 설정하면 됨

```
sudo raspi-config
Enable Boot to Desktop/Scratch
Change Keyboard Layout
Generic 105-key(Intl) PC
Other
Korean
Korean - Korean(101/104 Key compatible)
The Default for the keyboard layout
No compose key
Yes
Finish
```



## 도커 설치

```
sudo apt install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common
sudo apt-get install docker.io
docker -v
#권한 설정
sudo chmod 666 /var/run/docker.sock
#유저 권한주기? 일단 빼고 안되면 넣을 것
sudo usermod -aG docker pi
```

### 도메인 만들기

- 도커는 https을 기본으로 사용하기 때문에 registry를 만들려면 도메인이 필요함

- freenom에서 생성 (walter47.ga)
  - 처음에 도메인을 찾는것 부터 해야함 (로그인 먼저하면 안됨)
  - 도메인 찾으면 로그인 가능
  - Services - My domain - manage domain(톱니) 
    - Management Tools 
      -  NameServer - default로 둠
      - Register gule record
        - hostname : docker-registry.walter47.ga
        - ip address : 내 IP주소(네이버에서 내 IP주소 찾기하면 됨 - 외부 ip)
    - Manage Freenom DNS
      - 두개를 만들었음
      - Name : 빈칸, Target : 외부 IP
      - Name: docker-registry, Target : 외부 IP

### 인증서 만들기

참고 - 아래 글대로하면 됨

https://novemberde.github.io/2017/04/09/Docker_Registry_0.html

```
# openssl 버전 확인하기
$ openssl version

# cert.d 폴더에 개인키 생성하기. 비밀번호를 입력하자. 개인키 비밀번호 설정
$ mkdir certs && cd certs && openssl genrsa -des3 -out server.key 2048

pi@rasdocker:~/Desktop/docker/certs $ openssl req -new -key server.key -out server.csr
Enter pass phrase for server.key:
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:KR
State or Province Name (full name) [Some-State]:Seoul
Locality Name (eg, city) []:Seoul
Organization Name (eg, company) [Internet Widgits Pty Ltd]:NONE
Organizational Unit Name (eg, section) []:Test
Common Name (e.g. server FQDN or YOUR name) []:docker-registry.walter47.ga

# 개인키에서 패스워드 제거하기
$ cp server.key server.key.origin && openssl rsa -in server.key.origin -out server.key && rm server.key.origin

# 인증서 생성하기. 1년으로 사용하겠다. 2년 3년할 수도 있다. server.crt파일이 생길 것이다.
$ openssl x509 -req -days 730 -in server.csr -signkey server.key -out server.crt
```

### 이미지 만들기

```
$ docker images
$ docker pull hello-world
$ docker tag hello-world docker-registry.walter47.ga:5000/hello
```

### 도커 레지스트리 만들기

- -v /home/~에 경로를 잘 넣을 것!

```
docker pull registry
#도커 레지스트리 컨테이너 생성
docker run -d -p 5000:5000 --restart=always --name docker-registry \
  -v /home/<username>/certs:/certs \
  -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/server.crt \
  -e REGISTRY_HTTP_TLS_KEY=/certs/server.key \
  registry
```

- 도커 이미지 다운로드

  - 먼저 호스트에서 PC에서 https를 연결해줘야 함
    - mac 기준으로 preference-dockerengine에 추가

  ```
  {
    "insecure-registries": ["192.168.0.24:5000", "docker-registry.walter47.ga:5000"],
    "debug": true,
    "experimental": false
  }
  ```

  - 리눅스에서는 (호스트만 하면되서 딱히 필요없을수도?)
    - 라즈베리파이에서 해야됨

  ```
  sudo nano /etc/docker/daemon.json
  
  {
  "insecure-registries": ["192.168.0.24:5000"]
  }
  
  //라즈베리파이에서 freenom으로 부터 가져온 도메인 링크
  {
   "insecure-registries": ["docker-registry.walter47.ga:5000"]
  }
  
  sudo systemctl restart docker
  ```

### 푸시

```
docker push docker-registry.walter47.ga:5000/hello
```

## 에러 모음

- docker info 할때 에러

  ```
  WARNING: No memory limit support
  WARNING: No swap limit support
  WARNING: No kernel memory limit support
  WARNING: No oom kill disable support
  WARNING: No cpu cfs quota support
  WARNING: No cpu cfs period support
  ```

  - https://blog.raveland.org/post/docker_raspian/ 로 추가설정필요

  ```
  cat /boot/cmdline.txt 
  sudo nano /boot/cmdline.txt
  //아래 내용대로 추가 cgroup_enable=memory swapaccount=1
  dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=PARTUUID=d5e34328-02 rootfstype=ext4 elevator=deadline fsck.repair=yes cgroup_enable=memory swapaccount=1 rootwait
  ```

- Get https://docker-registry.walter47.ga:5000/v2/: Service Unavailable

  - push할때 생기는 에러 - 로그확인 (raspberry pi에서)
  - 확인 결과 인증서가 제대로 설정이 안됨 - 인증서 경로 넣을 때 잘 넣을 것. /home/pi/Desktop/docker/certs 이런식으로 잘 넣어야 함

  ```
  docker logs docker-registry 
  ```

### 