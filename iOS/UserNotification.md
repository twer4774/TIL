# UserNotification 로컬 알림

- iOS 10부터 UserNotification프레임 워크 사용
- 로컬 알림과 서버 알림의 차이는 단순히 구분 값에 의해 나누어짐
- import UserNotifications
- 대표 객체
  - UNMutableNotificationContent
    - 메시지등 알림 콘텐츠를 담는 역할
    - 타이틀, 서브 타이틀, 알림 메시지 설정
    - 배지, 사운드 설정
    - UNNotificationContent(수정은 불가능하고 읽기만 가능함 => 기존 등록된 알림 콘텐츠 읽을 때 이용)
  - UNTimeIntervalNotificationTrigger
    - 알림 발송 조건을 관리
    - 발생 시각, 반복 여부
    - "몇 분 후"등과 같이 시간 간격을 설정하여 알림메시지 발송가능(입력값: 초단위)
  - UNNotificationRequest
    - 알림 요청객체
  - UNUserNotificationCenter
    - 실제 발송을 담당하는 센터
    - 싱글턴 방식으로 동작 => current()메소드를 통해 참조 정보만 가져올 수 있음

```swift
//AppDelegate.swift
import UserNotifications

//앱이 켜질때 실행. 화면을 보여주기 전에 호출되는 메소드
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]? = nil) -> Bool{
    if #available(iOS 11.0, *){
        let notiCenter = UNUserNotificationCenter.current()
       
        notiCenter.requestAuthorization(options: [.alret, .badge, .sound]) { (didAllow, e) in}
    } else {
        let setting = UIUserNotificationSettings(types: [.alert, .badge, .sound], categories: nil)
        application.registerUserNotificationSettings(setting)
    }
    return true
}

//앱이 활성화 상태를 잃었을 때 실행되는 메소드
func applicationWillResignActive(_ appliation: UIApplication){
    if #available(iOS 10.0, *){
	//알림 동의 여부 확인
        UNUserNotificationCenter.current().getNotificationSettings{ settigns in
        if settings.authorizationStatus == UNAuthorizationStatus.authorized{
		//알림 콘텐츠 객체
		let nContent = UNMutatbleNotificationContent()
		nContent.badge = 1
		nContent.title = "로컬 알림 메시지"
		nContent.subtitle = "서브 타이틀"
		nContent.body = "바디"
		nContent.sound = UNNotificationSound.default()
        //로컬 알림과 함께 전달하고 싶을 값이 있을 때 사용 => 커스텀 형식
        //앱 델리게이트에서 처리
		nContent.userInfo = ["name":"홍길동"]

                                                                       
		//발송 조건 객체 => 하루 중 특정 시각을 지정하여 반복 가능
		let trigger = UNTimeIntervalNotificationTrigger(timeInterval: 5, repeats: false)
		//알림 요청 객체 
		let request = UNNotificationRequest(identifier: "wakeup", content: nContent, trigger: trigger)
		//노티피케이션 센터에 추가
		UNUserNotificationCenter.current().add(request)
			} else {
				print("사용자가 동의하지 않음")	
			}
            
        }
    } else {
	}
}
```



## 받은 알림 처리하기

- 푸시 알람에서 어떤 알림 메시지를 클릭해 앱을 실행했는지 구분
- 델리게이트 패턴 이용

```swift
//알림 메시지 클릭시 앱 델리게이트에서 이벤트 전달 받음
@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate, UNUserNotificationCenterDelegate{
    
}
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]? = nil) -> Bool{
   if #available(iOS 11.0, *){
    let notiCenter = UNUserNotificationCenter.current()    
    notiCenter.requestAuthorization(options: [.alret, .badge, .sound]) { (didAllow, e) in}
    notiCenter.delegate = self //추가
   } else {
       
   }
}
```

- 앱이 실행되는 도중에 알림 메시지가 도착할 경우 userNotificationCenter(_:willPresent:withCompletionHandler:)메소드 자동 호출 => 메소드 구현 필요
- 알림 메시지 클릭할 경우 userNotificationCenter(_:didRecevie:withCompletionHandler:)메소드 자동 호출 => 앱이 실행 중이던 미실행 상태이던 상관없이 동일하게 호출 됨

```swift
//앱 실행 도중에 알림 메시지가 도착한 경우
@available(iOS 10.0, *)
func userNotificationCenter(_ center: UNUserNotificationCenter, willPresent notification: UNNotification, withCopletionHandler completionHandler: @escaping (UNNotification PresentationOptions) -> Void){
    if notification.request.identifier == "wakeup"{
        let userInfo = notification.request.content.userInfo
        print(userInfo["name"]!)
    }
    
    //알림 배너 띄워주기
    completionHandler([.alert, .badge, .sound])
}

//사용자가 알림 메시지를 클릭했을 경우
@available(iOS 10.0, *)
func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void){
    if response.notification.request.identifier == "wakeup" {
        let userInfo = response.notification.request.content.userInfo
        print(userInfo["name"]!)
    }
    completionHandler()
}
```



#### 