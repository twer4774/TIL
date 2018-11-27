# FCM에서 APN 구성

- Firebase 클라우드 메시징 APN인터페이스는 Apple 푸시 알림 서비스(APN)를 사용해 백그라운 상태인 앱을 포함한 iOS앱으로 최대 4KB의 메시지를 전송할 수 있음
- 필요 조건
  - Apple개발자 계정의 Apple 푸시 알림 인증키 => FCM은 이 토큰을 사용해 앱 ID로 식별되는 애플리케이션에 푸시 알림을 보냄
  - 해당 앱 ID의 프로비저닝 프로필



## APNs 설정과정 

- https://github.com/twer4774/TIL/blob/master/iOS/APNs.md 참고