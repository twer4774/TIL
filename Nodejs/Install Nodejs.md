# Node설치

## 관리자 권한 실행

실행시 관리자 권한이 없으면 동작할 수 없는 경우가 있으므로 항상 관리자 권한하에서 작업 수행

```
sudo su
apt update //현재 업데이트 가능한 패키지 확인
apt dist-upgrade //최신버전으로 업그레이드
apt install npm //Node.js를 설치하기 위해서 npm을 먼저 설치해야함
npm install -g n //node관리 프로그램인 n설치 //n은 노드의 버전을 쉽게 관리할 수 있는 프로그램 -g는 global설치
n ls //설치된 버전들 표시
n lts //최신버전 설치
n stable //안정버전 설치
n //사용할 버전 선택가능
n rm 6.9.0 //6.9.0버전 삭제
node -v //n명령어 대신 사용가능함
```

