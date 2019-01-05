# PropertyList

- Codable: iOS11부터 나온 새로운 프로토콜, JSON과 같은 외부 포맷과 타입을 서로 변환하는데 사용 => Apple은 NSDictionary와 NSArray를 deprecated 할 예정임
- iOS 12부터는 Userdefaults.standard에서 NSKeyedArchiver를 deprecated 함
- PropertyList는 NSKeyedArchiver의 대안책으로 이용됨

```swift
//Codable프로토콜 적용
struct MySettings: Codable{
    var someFlag: Bool
    var someString: String
    var someInt: Int
    
    /* 선택 사항 - 프로퍼티 리스트에 있는 이름과 다른 이름을 쓰고 싶다면, CodingKeys enum을 추가하면 됨
    private enum CodingKeys: String, CodingKey{
        case someFlag
        case someString
        case id = "someInt"
	}
    */
}

//프로퍼티리스트 이용
let settingsURL: URL = ... //location of plist file
var settings: MySettings?

if let data = try? Data(contentsOf: settingsURL){
    let decoder = PropertyListDecoder()
    settings = try? decoder.decode(MySettings.self, from: data)
}

/* 에러 관리를 위해 do...catch 블록 이용하는 방법
do{
	let data = try Data(contentsOf: settingsURL)
	let decoder = PropertyListDecoder()
	settings = try decoder.decode(MySettings.self, from: data)
} catch {
	//Handle error
	print(error)
}
*/

/* 만약 프로퍼티 리스트 파일의 최상위에 딕셔너리(기본값) 대신 배열이라면
tpyealias Settings = [MySettings]
var settings: Settings?

do{
	let data = try Data(contentsOf: settingsURL)
	let decoder = PropertyListDecoder()
	settigns = try decoder.decode(MySettings.self, from: data)
} catch {
	//Handle error
	print(error)
}
*/

//프로퍼티 리스트 작성
let someSettings = MySettings(someFlag: true, someString: "Apple", someInt: 42)
let encoder = PropertyListEncoder()
encoder.outputFormat = .xml
do{
    let data = try encoder.encode(someSettings)
    try data.write(to: settingsURL)
} catch {
    //Handle error
    print(error)
}
```

