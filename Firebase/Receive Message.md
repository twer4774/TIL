# iOS앱에서 메시지 수신

- FCM APN인터페이스를 통해 메시지 수신
- 알림 작성기를 사용해 즉시 사용자 세그먼트로 알림 전송 또는 애플리케이션 서버에서 APN인터페이스를 통해 알림 페이로드가 포함된 메시지를 보낼 수 있음
- FCM APN 인터페이스를 통해 수신된 메시지를 처리하면 일반적인 사용 사례를 대부분 해결할 수 있음
- 업스트림 메시지 전송 또는 포그라운드 앱에서도 데이터 수신 가능

## FCM APN 인터페이스를 통해 수신된 메시지 처리

- 알림을 탭하면 앱이 열리고, AppDelegate의 didReceiveRemoteNotification콜백에 알림내용 전달

```swift
func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable: Any]) {
    print(userInfo)
}

func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable: Any],
                 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
    print(userInfo)

  completionHandler(UIBackgroundFetchResult.newData)
}

```

