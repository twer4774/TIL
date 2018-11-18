# URL Scheme

- 미리 정해진 형식의 URL을 통해 다른 앱과 통신할 수 있는 수단

- URL Scheme을 통해 다른 앱의 실행을 요청하거나 간단한 데이터를 전달 할 수 있음

- Custom URL Scheme을 구현해 직접 URL Scheme을 정의하고 다른 앱으로 부터 전달 된 데이터 처리도 가능

- 앱으로 전달할 데이터의 형식은 프로토콜에 따라 달라짐

- ```
  프로토콜 : 앱으로 전달할 데이터
  ```

- URL Scheme사용 과정

  1. URL Scheme 문자열을 통해 URL 인스턴스 생성
  2. UIApplication 클래스의 canOpenURL(_:) 메소드를 통해 URL Scheme의 유효성 확인
  3. 유효한 URL Scheme으로 확인된 경우 openURL(:_) 메소드를 호출

### Built-in URL Scheme

- 기본으로 설치된 메일, 전화, 메시지, 지도 앱과 통신할 수 있는 내장 URL Scheme 제공

  - Apple URL Scheme Reference에서 확인

  | URL Scheme                                                   | 설명                                      |
  | ------------------------------------------------------------ | ----------------------------------------- |
  | http://웹사이트 URL<br />https://웹사이트 URL                | Safari 앱을 통해 웹사이트 표시            |
  | mailto:이메일 주소                                           | 메일 앱을 통해 새로운 메일 작성 화면 표시 |
  | tel:전화번호                                                 | 전화 연결                                 |
  | sms:전화번호                                                 | 문자 연결                                 |
  | http://maps.apple.com/?q=검색어<br />http://maps.apple.com/?\|\|=위도,경도 | 지도앱을 통해 지역 표시                   |
  | itms://itunes.apple.com/us/app/apple-store/앱ID              | APP Store앱을 통해 앱 정보 표시           |

```swift
func openURL(_ urlString: String){
    guard let str = urlString.replacingPercentEscapes(using: String.Encoding.utf8) else{
        return
    }
    
    guard let url = URL(string: str) else{ return }
    
    if(UIApplication.shared.canOpenURL(url)){
        if #available(iOS 10, *){
            UIApplication.shared.open(url, options: [:], completionHandler:{
                (success) in
                if success{
                    //Success
                }
            })
        } else {
            if UIApplication.shared.openURL(url){
                //Success
            }
        }
    } else {
        let alert = UIAlertController(title: "URL Schemes", message: "사용할 수 없는 ㅎURL Scheme입니다.", preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "확인", style: .cancel, handler: nil))
        present(alert, animated: true, completion: nil)
    }
}

@IBAction func openWebsite(_ sender: AnyObject){
    openURL("https://www.apple.com")
}
@IBAction func openPhone(_ sender: AnyObject){
    openURL("sms:010-0000-0000")
}
```



## Custom URL Scheme

- 앱에서 직접 URL Scheme을 처리하려면 Custom URL Scheme을 구현 해야 함
- 구현방법
  1. Info.plist파일에 URL types항목을 구성
  2. App Delegate를 통해 URL Scheme가 전달 될때 호출되는 메소드 구현