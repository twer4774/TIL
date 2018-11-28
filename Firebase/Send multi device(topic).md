# 여러 기기에 메시지 보내기

- Firebase 클라우드 메시징은 메시지를 여러 기기로 타겟팅하는 방법 2가지를 제공
  - 주제 메시징: 특정 주제를 구독하는 여러 기기에 메시지를 보낼 수 있음

    -  FCM 주제 메시징을 사용하면 게시/구독 모델을 기반으로 특정 주제를 구독하는 여러 기기에 메시지를 보낼 수 있음
    - 필요에 따라 주제 메시지를 작성하면 FCM에서 라우팅 처리하여 올바른 기기에 정확히 전달 됨
      - 지역 일기예보 앱 사용자 - 기상 특보 주제를 구독하여 해당 지역에서 발령되는 태풍 경보를 수신 가능
      - 스포츠 앱 사용자 - 응원하는 팀의 경기 점수 실황을 자동으로 업데이트 수신 가능

    - 주제와 관련된 주의사항
      - 각 앱에 지원하는 주제 및 구독에는 제한이 없음
      - 뉴스, 날씨 등 공객적으로 제공되는 정보에 적합
      - 지연 시간이 아닌 처리량 위주로 최적화 됨. 기기가 1대이거나 적은 수일 경우 빠르고 안전하게 전달하려면 등록토큰으로 메시지를 타겟팅 하는 것이 좋음
      - 사용자를 기준으로 여러 기기에 메시지를 보내야 한다면 기기 그룹 메시징 이용

  - 기기 그룹 메시징: 그룹에 속한 기기에서 실행되는 여러 앱 인스턴스에 단일 메시지를 보낼 수 있음

    - 그룹에 속한 기기에 실행되는 앱의 여러 인스턴스에 단일 메시지를 보낼 수 있음
    - 그룹의 모든 기기는 공통의 '알림키'를 공유 => FCM이 그룹의 모든 기기에 메시지를 전달하는데 사용
    - Admin SDK를 사용하거나 앱 서버에서 XMPP또는 HTTP 프로토콜을 구현하면 기기 그룹 메시징을 이용할 수 있음(단, 알림 키에 허용되는 최대 구성원 수는 20명)
    - 기기 그룹 관리(그룹 만들기, 삭제, 기기 추가 또는 삭제는 보통 앱 서버를 통해 수행함)
      1. 그룹에 추가할 각 기기마다 등록 토큰을 부여
      2. 그룹 식별을 위한 notification_key를 만듦 => 앱 서버나 Android 클라이언트 앱에서 알림키를 만들 수 있음

- FCM용 HTTP 또는 XMPP프로토콜을 사용하여 주제 메시지를 보내는 방법 및 iOS 앱에서 메시지를 수신하고 처리하는 방법을 중점적으로 설명



## 서버에서 주제 구독 관리

- Intance ID API를 활용하여 서버 쪽에서 기본적인 주제 관리 작업을 수행할 수 있음

  - Instance ID: 앱마다 고유의 ID 할당 - Firebase 모듈에 내장되어 있음. 아래는 설명 참조용

    - 핵심기능

      - 보안 토큰 생성 
      - 앱 인증 확인: 응용 프로그램 패키지 이름을 확인하고 유효한 서명이 있는지 확인
      - 앱 디바이스가 활성상태인지 확인: 앱이 설치된 장치가 마지막으로 사용 된 시점
      - 앱 식별 및 추적: 전 세계의 모든 앱 인스턴스에서 고유하므로 데이터베이스가 이를 활용해 앱 인스턴스를 식별함

    - 인스턴스 ID 수명주기

      1. 인스턴스 ID 서비스는 InstanceID 앱이 온라인 상태 일 때 문제를 발생시킴. Instance ID는 공개/비밀 키 쌍으로 디바이스에는 개인 키를 저장하고 공개키는 Instance ID 서비스에 보관 함
      2. getID()메소드를 호출하면 Instance ID 요구함. 앱을 지원하는 서버가 있으면 앱이 서버에 저장할 수 있음
      3. 앱은 필요에 따라 getToken()메소드를 사용해 Instance ID 서비스에서 토큰을 요청할 수 있으며 앱은 사용자의 서버에 토큰을 저장할 수도 있음
      4. 토큰은 안전하지만 사용자가 디바이스에서 앱을 제거하고 다시 설치할 때 토큰을 교체해야함. 앱은 Instance ID 서비스의 토큰을 새로고침 요청에 응답하기 위해 리스너를 구현해야 함

    - iOS 구현

      - CocoaPods이용 - 버전이 올라가면서 Firebase 모듈안에 삽입 됨. => 설치 필요없음

      ```
      pod init
      pod 'FirebaseInstanceId'
      pod install
      ```

      - Token 생성

      ```swift
      func token(withAuthorizedEntity authorizedEntity: String, scope: String, options: [AnyHashable : Any]? = nil, handler: @escaping InstanceIDTokenHandler)
      
      /*
      authorizedEntity: 토큰에 의해 허가된 객체
      scope: authorizedEntity에 대한 승인 된 작업
      options: 토큰요청과 함께 보낼 추가 옵션에 대한 값. apns_token은 didRegisterForRemoteNotificationWithDeviceToken메소드로 부터 얻어짐
      handler: 정보를 가져오는데 성공했을 시에 token을 리턴하고 아니면 nil을 리턴함
      */
      ```

      - Token 과 Instance ID 관리

      ```objective-c
      //Delete token
      func deleteToken(withAuthorizedEntity authorizedEntity: String, scope: String, handler: @escaping InstanceIDDeleteTokenHandler)
      
      //getID
      func getID(handler: @escaping InstanceIDHandler)
      //deleteID
      func deleteID(handler: @escaping InstanceIDDeleteHandler)
      ```



## 클라이언트 앱에서 주제 구독

- 클라이언트 앱에서 기존 주제를 구독하거나 새 주제를 만들 수 있음
- 클라이언트 앱에서 Firebase 프로젝트에 아직 없는 새 주제 이름을 구독하면 FCM에서 이 이름으로 새 주제가 만들어지고, 이후에 다른 클라이언트에서 그 주제를 구독할 수 있음
- FIRMessaging 클래스에서 주제 메시징 기능 처리
- 주제를 구독하려면 애플리케이션의 기본 스레드에서 subscribeToTopic:topic을 호출함
- FCM은 스레드 안전을 지원하지 않음

## 주제 메시지 수신 및 처리

- FCM은 다른 다운스트림 메시지(서버->클라이언트)와 동일한 방식으로 주제 메시지를 전송
- 간단하게 알림작성기에서 FCM 보내는 방법

```swift
 func messaging(_ messaging: Messaging, didReceiveRegistrationToken fcmToken: String) {
       Messaging.messaging().subscribe(toTopic: "/topics/dog")
}
```

## 보내기 요청 작성

```swift
'TopicA' in topics && ('TopicB' in topics || 'TopicC' in topics)
//TopicA 및 TopicB
//TopicA 및 TopicC
//메시지 수신
```

- 조건식에는 최대 5개의 주제를 포함할 수 있음

