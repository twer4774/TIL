# 리치푸시(Push Extension)

단점으로는 서버와 협업이 필요하고 나아가서는 디자인/기획파트와 협의해야할 일이 생길수도 있습니다

- https://rhammer.tistory.com/270
- https://www.twilio.com/blog/2017/07/ios-usernotifications-in-swift.html
- iOS10부터 Notification Service Extension, Notification Content Extension
  - Notification Service Extension: 페이로드를 가로채 푸쉬에 띄우고자 하는 데이터를 재구성 하는 것 ->  이미지, 비디오 등 미디어를 다운로드하여 푸쉬에 첨부
    - 주의사항: 푸시 페이로드는 4KB로 용량 제한 -> 미디어는 url로 전달 -> 파일 다운로드(Service Extension)
  - Notification Content Extension:  푸시 알림 UI를 커스터마이징할 때 사용하는 것
    - 주의사항
      - View 크기를 적절히 조절해야함(NotificiationViewController - viewDidLoad에서 조절 가능)
      - 앱이 Not running 상태에서 푸시알림의 사이즈를 정하기 위해 info.plist에 값 세팅 필요
        USExtensionAttributes - UNNotificationExtensionInitialContentSizeRatio
- 타겟 생성으로 Service Extension, Content Extension 생성
- 작동 순서
  - 푸쉬 페이로드 도착 -> `didReceive(request: ...)`에서 이미지 다운로드 시작 -> 이미지 다운로드 완료 -> 푸쉬 컨텐츠에 이미지 추가 -> 사용자에게 푸쉬 노출





## 서버에서 해주어야 할 일

1. 페이로드 작성

   - ServiceExtension을 사용하기 위해서는 mutable-content 필드 필요

   ```
   {
       aps:{
           alert: { _ },
           mutable-content: 1
       }
       my-attachment: "https://example.com/photo.jpg"
   }
   ```

2. ContentExtension을 적용하기 위해서는 category 필드 필요

   info.plist에서 NSExtensionAttributes - UNNotificationExtensionCategory - item0: event-invite, item1: event-update 설정



