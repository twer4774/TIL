# SwiftyJSON

https://github.com/SwiftyJSON/SwiftyJSON

- 기본 swift 코드

```swift
if let statusesArray = try? JSONSerialization.jsonObject(with: data, options: .allowFragments) as? [[String: Any]],
    let user = statusesArray[0]["user"] as? [String: Any],
    let username = user["name"] as? String {
    // Finally we got the username
}
```

- SwiftyJSON을 이용한 코드

```swift
let json = JSON(data: dataFromNetworking)
if let userName = json[999999]["wrong_key"]["wrong_name"].string{
    
} else {
    print(json[999999]["wrong_key"]["wrong_name"])
}
```

## 사용

```swift
import SwiftyJSON
let json = JSON(data: dataFromNetworking)
let json = JSON(jsonObject)
if let dataFromString = jsonString.data(using: .utf8, allowLossyConversion: false) {
    let json = JSON(data: dataFromString)
}

//Subscript
let name = json[0].double
let arrayNames = json["users"].arrayValue.map({$0["name"].stringValue})
let name = json["name"].stringValue

//Getting a string using a path to the element
let path: [JSONSubscriptType] = [1,"list",2,"name"]
let name = json[path].string
//Just the same
let name = json[1]["list"][2]["name"].string
let name = json[1,"list",2,"name"].string

//Loop
//dictionary
for (key,subJson):(String, JSON) in json{
    
}

//array
for (index,subJson):(String, JSON) in json{
    
}
```

- SwiftyJSON의 장점
  - 배열에서 응용프로그램 충돌이 발생하지 않음(index out-of-bounds)
  - 딕셔너리가 이유없이 nil로 할당 되지 않음
  - 배열이나 딕셔너리가 아닌 "인식할 수 없는 셀렉터"예외로 앱이 중단 되지 않음



