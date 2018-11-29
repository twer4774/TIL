# Admin FCM API 소개

- 자체 백엔드 서비스를 FCM과 통합할 수 있음
- Firebase 서버 인증을 처리하는 동시에 메시지 보내기와 주제 구독 관리를 지원 함



## 메시지 보내기

- 최종 사용자 기기에 Fireabase 클라우드 메시징 메시지를 보낼 수 있음
- 개별 기기, 지정된 주제, 하나 이싱의 주제와 일치하는 조건문에 메시지를 보낼 수 있음
- Admin Node.js SDK는 기기 그룹에 메시지를 보내는 추가 메소드를 제공
- Admin FCM API를 사용해 다른 타겟 플랫폼에 맞는 메시지 페이로드를 구성할 수 있음
- 메시지 페이로드에 여러 플랫폼의 구성 옵션이 있는 경우 FCM 서비스에서는 메시지를 전달할 때 각 플랫폼에 맞게 메시지를 맞춤 설정 함
- Admin FCM API를 사용하려면 우선 서버에 Firebase Admin SDK 추가 필요. Firebase 프로젝트 ID로 Admin SDK 초기화 필요

### Node.js 이용

- 설치

```
npm install firebase-admin
```

- 이용

```js
var admin = require('firebase-admin');

var serviceAccount = require('path/to/serviceAccountkey.json');

admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    databaseURL: 'https://<DATABASE_NAME>.firebaseio.com'
});

//Google OAuth2
var refreshToken; //Get refresh token from OAuth2 flow

admin.initializeApp({
    credential: admin.credential.refreshToken(refreshToken),
    databaseURL: 'https://<DATABASE_NAME>.firebaseio.com'
});
```

- 개별 기기로 전송
  - 등록 토큰을 지정하여 개별 기기에 메시지를 보낼 수 있음(등록토큰: 최종 사용자 클라이언트 앱 인스턴스별로 클라이언트 FCM SDK가 생성하는 문자열)

## 주제 구독 관리

- Fireabase Admin SDKsms FCM주제에 대한 기기 구독 및 구독 취소를 위한 API를 제공
- 한번에 최대 1,000대의 기기 등록 토큰을 구독하거나 구독 취소 가능