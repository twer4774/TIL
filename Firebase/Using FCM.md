# FCM 사용

- Podfile 생성 후 설치할 pod 파일 추가 및 설치

```
pod init

nano Podfile

//아래의 pod 추가
pod 'Firebase/Core'
pod 'Firebase/Messaging'

pod install
```



## Firebase 콘솔에서 APN 설정

FCM에서 메시지를 보내기 위해서는 인증키 또는 인증서를 이용하는 방법으로 나뉨

- 이번에는 인증서를 이용하는 방법을 사용
  - 인증서는 develop과 production 두가지를 준비해야 함
  - 키 체인에서 인증서 지원 - 인증기관에서 인증서 요청으로 2개의 인증서를 만듦
  - https://developer.apple.com/account 에서 App IDs으로 들어가 설정 한 후 Push Notification에서 develop버전과 production 버전을 생성해 만듦
  - Firebase 설정에서 프로젝트 - iOS앱 구성의 인증서 부분에 각각의 인증서들을 업로드 시킴

## 등록 토큰 액세스

- 기본적으로 FCM SDK는 앱을 처음 시작할때 클라이언트 앱 인스턴스용 등록 토큰을 생성
- APN기기 토큰과 마찬가지로 이 토큰을 사용하여 알림 메시지를 앱의 이 특정 인스턴스로 타겟팅할 수 있음
- FCM SDK는 FIRMessageDelegate을 통해 messaging:didReceiveRegistrationToken:을 호출함
  - iOS가 일반적으로 앱 시작 시 APN 기기 토큰을 전달하는 것과 마찬가지로, FCM은 앱이 시작될 때마다 FIRMessaging 대리자의 messaging:didReceiveRegistrationToken 콜백을 통해 등록 토큰을 제공
  - 토큰이 변경된 경우 FCM SDK는 토큰을 발급 받음
  - 위의 두가지 모두 messaging:didReceiveRegistrationToken:을 호출함
  - 등록 토큰이 변경되는 경우
    - 새 기기에서 앱 복원
    - 사용자가 앱 삭제/재설치
    - 사용자가 앱 데이터 소거

## 메시지 대리자 설정

- 앱 시작 시 등록 토큰을 받으려면 클래스에서 메시지 대리자 프로토콜을 구현
- [FIRApp configure]를 호출한 후 대리자 속성에 제공
- 애플리케이션 대리자가 메시지 대리자 프로토콜을 준수하는 경우 application:didFinishLaunchingWithOptions:에서 대리자를 자기 자신으로 설정 가능
  - Messaging.emssaging().delegate = self

## 현재 등록 토큰 수신

- 등록 토큰은 메소드인 messaging:didReceiveRegistrationToken:을 통해 전달
- 일반적으로 앱 시작 시 FCM 토큰을 사용하여 이 메소드를 한번 호출함
  - 새 등록 토큰이라면 애플리케이션 서버에 전송 - 새 토큰인지 여부를 판단하는 서버 로직 구현을 추천 함
  - 등록 토큰을 주제에 구독 처리 함 - 신규 구독 또는 사용자의 앱 재설치 같은 상황에서만 필요

```swift
 func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
   let token = Messaging.messaging().fcmToken
        print("FCM token: \(token)")   
 }
```



## 토큰 생성 모니터링

- 토큰이 업데이트 될 때마다 알림을 받으려면 메시지 대리자 프로토콜을 준수하는 대리자를 제공

```swift
 func messaging(_ messaging: Messaging, didReceiveRegistrationToken fcmToken: String) {
        print("Firebase registration token: \(fcmToken)")
     
     //여기에 필요하다면, 토큰을 서버로 보내는 코드 작성
     
    }
```

- 대리자 메소드를 제공하는 대신 kFIRMessagingRegistrationTokenRefreshNotification이라는 NSNotification을 수신 대기할 수도 있음
- 토큰 속성은 항상 현재 토큰 값을 갖게 됨
- 재구성 사용중지됨: APN 토큰과 등록 토큰 매핑
- 매소드 재구성을 사용 중지했다면 APN 토큰을 명시적으로 FCM 등록 토큰에 매핑해야 함
- didRegisterForRemoteNotificationsWithDeviceToken 메소드를 재정의하여 APN토큰을 검색한 후 APNSToken 속성을 사용 함

```swift
   func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
        let token = Messaging.messaging().fcmToken
        print("FCM token: \(token)")
        
        Messaging.messaging().apnsToken = deviceToken
    }
```

- FCM 등록 토큰이 생성된 후 재구성이 사용 설정되었을 때와 동일한 메소드를 사용하여 토큰에 액세스하고 새로고침 이벤트를 수신 대기 할 수 있음

## APN설정

> iOS 10 이상을 실행하는 기기에서는 앱 실행이 끝나기 전에 대리자 객체를 [`UNUserNotificationCenter`](https://developer.apple.com/reference/usernotifications/unusernotificationcenter?language=objc) 객체에 할당하여 디스플레이 알림을 수신하고 [`FIRMessaging`](https://firebase.google.com/docs/reference/ios/firebasemessaging/interface_f_i_r_messaging?authuser=0) 객체에 할당하여 데이터 메시지를 수신해야 합니다. 예를 들어 iOS 앱의 `applicationWillFinishLaunching:` 또는 `applicationDidFinishLaunching:` 메소드에서 할당해야 합니다.

```swift
import Firebase
import UserNotifications

class AppDelegate: UIResponder, UIApplicationDelegate, UNUserNotificationCenterDelegate, MessagingDelegate { //UNUserNotificationCenterDelegate, MessagingDelegate 추가
    
   func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
	    FirebaseApp.configure()
    	Messaging.messaging().delegate = self
       
      return true
   }
   
  func application(_ application: UIApplication, willFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
      if #available(iOS 12, *){
          UNUserNotificationCenter.current().delegate = self

          let authOptions: UNAuthorizationOptions = [.alert, .badge, .sound]
          UNUserNotificationCenter.current().requestAuthorization(options: authOptions) { (_, _) in

                                                                                        }
      } else {
          let settings: UIUserNotificationSettings = UIUserNotificationSettings(types: [.alert, .badge, .sound], categories: nil)
          application.registerUserNotificationSettings(settings)
      }

      application.registerForRemoteNotifications()

      return true
  }   
}
```



## 알림 메시지 전송

1. 기기에 앱을 설치하고 실행
2. 백그라운드 상태로 앱 전환
3. 알림작성기를 열고 새 메시지 선택(성장-Cloud Messaging에 있음)
4. 메시지 본문을 입력
5. 메시지 타겟으로 단일 기기 선택
6. FCM등록 토큰 필드에 이 가이드의 앞 섹션에서 확인한 등록 토큰을 입력함