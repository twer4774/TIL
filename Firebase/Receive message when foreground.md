# 포그라운드 앱에서 데이터 메시지 처리

- 앱이 포그라운드 상태일 때 APN이 아닌 FCM에서 데이터 전용 메시지를 직접 수신
- FCM서비스에 연결하고 FIRMessagingDelegate messaging:didReceiveMessage:로 메시지를 처리해야 함
- 연결하려면 AppDelegate에서 shouldEstablishDirectChannel 플래그를 YES로 설정
- 앱이 백그라운드로 전화되면 연결을 종료하고 포그라운드로 전환하면 다시 연결함
- Messaging:didReceiveMessage: 구현

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter, willPresent notification: UNNotification, withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
        let userInfo = notification.request.content.userInfo
        
        if let messageID = userInfo[gcmMessageIDKey]{
            print("Message ID: \(messageID)")
        }
        
        print(userInfo)
        
        completionHandler([.alert])
    }
    
    func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {
        let userInfo = response.notification.request.content.userInfo
        
        if let messageID = userInfo[gcmMessageIDKey]{
            print("Message ID: \(messageID)")
        }
        
        print(userInfo)
        
        completionHandler()
    }

```

