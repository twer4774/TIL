# Alamofire

참고 사이트 : https://outofbedlam.github.io/swift/2016/02/04/Alamofire/

- Swift 기반의 HTTP 네트워킹 라이브러리
- 설치

```
pod init
nano Podfile
pod 'Alamofire'
pod install
```

- 기능
  - 체이닝 가능한 Request/Response 메서드
  - URL/JSON/plist 파라미터 인코딩
  - 파일/데이터/스트림/멀티파트 폼 데이터 업로드
  - Request 또는 Resume 데이터를 활용한 다운로드
  - NSURLCredential을 통한 인증
  - HTTP 리스폰스 검증
  - TLS 인증서와 공개 키 Pinning
  - 진행 상태 클로저와 NSProgress
  - cURL 디버깅 출력
  - 광범위한 단위 테스트 보장
  - 비동기 네트워크 연동
  - 완벽한 문서화

## 사용법

- Request 만들기

```swift
import Alamofire
Alamofire.request(.GET, "http://ax.itunes.apple.com/WebObjects/MZStoreServices.woa/ws/RSS/topsongs/limit=25/json")
```

- Response 수신

```swift
let urlStr = "http://ax.itunes.apple.com/WebObjects/MZStoreServices.woa/ws/RSS/topsongs/limit=25/json"
let url = URL(string: urlstr)!

Alamofire.request(url).responseJSON{ (dataResponse: DataResponse<Any>) in
            if let result = dataResponse.value as? [String:Any],
                let feed = result["feed"] as? [String: Any],
                let entry = feed["entry"] as? [ [String: Any] ]{
                for one in entry{
                    var song = SongInfo()
                    
                    if let titleNode = one["title"] as? [String : AnyObject],
                        let title = titleNode["label"] as? String{
                        song.title = title
                    }
                    
                    if let imageNode = one["im:image"] as? [ [String: AnyObject] ],
                        let image = imageNode[0]["label"] as? String{
                        song.image = image
                    }
                    
                    self.songs.append(song)
                }
                self.tableView.reloadData()
            }
        }

//또는 method를 이용해야하는 경우
 Alamofire.request(urlStr, method: .post, parameters: ["user":"test2", "password":"1234"], encoding: JSONEncoding.default, headers: ["Content-Type":"application/json"]).validate().responseJSON { (dataResponse: DataResponse<Any>) in
            if let result = dataResponse.value as? [String:Any]{
                if let data = result["data"] as? [String: AnyObject]{
                    print(data)
```

## Response 처리

- 서버로부터 리스폰스를 수신할 때 여러 리스폰스를 처리할 수 있음
  - response()
  - responseData()
  - responseString(encoding: NSStringEncoding)
  - responseJSON(options: NSJSONReadingOptions)
  - responsePropertyList(options: NSPropertyListReadOptions)

```swift
//리스폰스 핸들러
Alamofire.request(.GET, "https://httpbin.org/get", parameters: ["foo": "bar"])
         .response { request, response, data, error in
             print(request)
             print(response)
             print(data)
             print(error)
          }

//데이터 리스폰스 핸들러
Alamofire.request(.GET, "https://httpbin.org/get", parameters: ["foo": "bar"])
         .responseData { response in
             print(response.request)
             print(response.response)
             print(response.result)
          }

//스트링 리스폰스 핸들러
Alamofire.request(.GET, "https://httpbin.org/get")
         .responseString { response in
             print("Success: \(response.result.isSuccess)")
             print("Response String: \(response.result.value)")
         }

//JSON 리스폰스 핸들러
Alamofire.request(.GET, "https://httpbin.org/get")
         .responseJSON { response in
             debugPrint(response)
         }

//복수 리스폰스 핸들러 연결
Alamofire.request(.GET, "https://httpbin.org/get")
         .responseString { response in
             print("Response String: \(response.result.value)")
         }
         .responseJSON { response in
             print("Response JSON: \(response.result.value)")
         }
```



## HTTP 메서드

```swift
//이 값들은 Alamofire.request() 첫번째 인자로 사용됨
public enum Method: String{
    case HEAD, OPTIONS, GET, POST, PUT, DELETE, TRACE, CONNECT, PATCH
}
```

## HTTP 파라미터

- GET

```swift
Alamofire.request(.GET, "https://httpbin.org/get", parameters: ["foo": "bar"])
// https://httpbin.org/get?foo=bar
```

- POST

```swift
let parameters = [
    "foo": "bar",
    "baz": ["a", 1],
    "qux": [
        "x": 1,
        "y": 2,
        "z": 3
    ]
]

Alamofire.request(.POST, "https://httpbin.org/post", parameters: parameters)
// HTTP body: foo=bar&baz[]=a&baz[]=1&qux[x]=1&qux[y]=2&qux[z]=3
```

- HTTP 파라미터 인코딩

```swift
enum ParameterEncoding {
    case URL
    case URLEncodedInURL
    case JSON
    case PropertyList(format: NSPropertyListFormat, options: NSPropertyListWriteOptions)
    case Custom((URLRequestConvertible, [String: AnyObject]?) -> (NSMutableURLRequest, NSError?))

    func encode(request: NSURLRequest, parameters: [String: AnyObject]?) -> (NSURLRequest, NSError?)
    { ... }
}

//파라미터를 JSO으로 인코디앟여 서버로 POST 요청을 보내는 예
let parameters = [
    "foo": [1,2,3],
    "bar": [
        "baz": "qux"
    ]
]

Alamofire.request(.POST, "https://httpbin.org/post", parameters: parameters, encoding: .JSON)
// HTTP body: {"foo": [1, 2, 3], "bar": {"baz": "qux"}}
```

## HTTP 헤더

- 헤더가 계속 바뀌는 경우 유용한 방법
- 고정된 헤더를 반복하여 사용하는 경우에는 NSURLSessionConfiguration에 설정하여 NSURLSession이 NSURLSessionTask를 생성할 때 자동으로 적용되도록 하는 것이 좋음

```swift
//헤더가 계속 바뀌는 경우
let headers = [
    "Authorization": "Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==",
    "Content-Type": "application/x-www-form-urlencoded"
]

Alamofire.request(.GET, "https://httpbin.org/get", headers: headers)
         .responseJSON { response in
             debugPrint(response)
         }
```

## Cashing

- 시스템 프레임워크의 NSURLCache를 통해서 처리 됨

## 업로드

- Alamofire는 파일, 데이터, 스트림, 멀티파트 폼 데이터 형태의 업로드를 지원함

```swift
//파일 업로드
let fileURL = NSBundle.mainBundle().URLForResource("Default", withExtension: "png")
Alamofire.upload(.POST, "https://httpbin.org/post", file: fileURL)

//업로드 진행 상태
Alamofire.upload(.POST, "https://httpbin.org/post", file: fileURL)
         .progress { bytesWritten, totalBytesWritten, totalBytesExpectedToWrite in
             print(totalBytesWritten)

             // This closure is NOT called on the main queue for performance
             // reasons. To update your ui, dispatch to the main queue.
             dispatch_async(dispatch_get_main_queue()) {
                 print("Total bytes written on main queue: \(totalBytesWritten)")
             }
         }
         .responseJSON { response in
             debugPrint(response)
         }

//멀티파트 폼 데이터 업로드
Alamofire.upload(
    .POST,
    "https://httpbin.org/post",
    multipartFormData: { multipartFormData in
        multipartFormData.appendBodyPart(fileURL: unicornImageURL, name: "unicorn")
        multipartFormData.appendBodyPart(fileURL: rainbowImageURL, name: "rainbow")
    },
    encodingCompletion: { encodingResult in
        switch encodingResult {
        case .Success(let upload, _, _):
            upload.responseJSON { response in
                debugPrint(response)
            }
        case .Failure(let encodingError):
            print(encodingError)
        }
    }
)
```



## 다운로드

```swift
//파일 다운로드
Alamofire.download(.GET, "https://httpbin.org/stream/100") { temporaryURL, response in
    let fileManager = NSFileManager.defaultManager()
    let directoryURL = fileManager.URLsForDirectory(.DocumentDirectory, inDomains: .UserDomainMask)[0]
    let pathComponent = response.suggestedFilename

    return directoryURL.URLByAppendingPathComponent(pathComponent!)
}

//디폴트 다운로드 폴더 지정
let destination = Alamofire.Request.suggestedDownloadDestination(directory: .DocumentDirectory, domain: .UserDomainMask)
Alamofire.download(.GET, "https://httpbin.org/stream/100", destination: destination)

//진행상태와 함께 파일 다운로드
Alamofire.download(.GET, "https://httpbin.org/stream/100", destination: destination)
         .progress { bytesRead, totalBytesRead, totalBytesExpectedToRead in
             print(totalBytesRead)

             // This closure is NOT called on the main queue for performance
             // reasons. To update your ui, dispatch to the main queue.
             dispatch_async(dispatch_get_main_queue()) {
                 print("Total bytes read on main queue: \(totalBytesRead)")
             }
         }
         .response { _, _, _, error in
             if let error = error {
                 print("Failed with error: \(error)")
             } else {
                 print("Downloaded file successfully")
             }
         }code

//실패한 다운로드의 재시도 데이터에 접근
Alamofire.download(.GET, "https://httpbin.org/stream/100", destination: destination)
         .response { _, _, data, _ in
             if let
                 data = data,
                 resumeDataString = NSString(data: data, encoding: NSUTF8StringEncoding)
             {
                 print("Resume Data: \(resumeDataString)")
             } else {
                 print("Resume Data was empty")
             }
         }
```

