# Deep Link

- 다른 플랫폼(앱), 웹사이트 등에서 앱으로 데이터를 전달하는 방법
- 클릭 한번으로 앱으로 데이터를 전송할 수 있음
- 만약 해당 링크의 앱이 설치되지 않을 경우 앱스토어로 이동함



## Firebase Dynamic Deep Link

1. pod 설치

   ```
   pod 'Firebase/DynamicLinks'
   ```

2. Firebase 콘솔에서 프로젝트설정

   1. iOS 앱을 추가한다
   2. 추가한 앱에 번들ID, App StoreID(테스트 목적으로 itunes에서 복사가능), TeamID(개발자 사이트에서 확인가능)를 입력한다

3. 프로젝트 내에 Target - Info - URL Types를 추가한다

   1. URL Schemes에  Bundle ID 추가
   2. Capabilities 탭에서 Associated Domains를 Enable한다
   3. 2번의 도메인에 applinks를 넣는다
      https://p223v.app.goo.gl/ -> 이런 형식
      p223v는 app code 이며, app code는 firebase 프로젝트 메뉴에서 확인 가능하다

4. Dynamic link 만들기
   Firebase 콘솔에서 생성하기

5. iOS 앱에서 Dynamic link 다루기

   ```swift
   
   func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
           // Override point for customization after application launch.
           FIRApp.configure()
    
           return true
       }
   
   func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([Any]?) -> Void) -> Bool {
           if let incomingURL = userActivity.webpageURL {
               let handleLink = FIRDynamicLinks.dynamicLinks()?.handleUniversalLink(incomingURL, completion: { (dynamicLink, error) in
                   if let dynamicLink = dynamicLink, let _ = dynamicLink.url 
   {
                       print("Your Dynamic Link parameter: \(dynamicLink)")
                   } else {
                       // Check for errors
                   }
               })
               return handleLink!
           }
           return false
       }
       
       func handleDynamicLink(_ dynamicLink: FIRDynamicLink) {
           print("Your Dynamic Link parameter: \(dynamicLink)")
   ```

   