# Codable

- 외부표현(JSON등)으로 변환할 수 있는 타입

- ```swift
  typealias Codable = Decodable & Encodable
  ```

- Encodable: 자신을 외부표현으로 인코딩할 수 있는 타입

- Decodable: 자신을 외부표현으로 디코딩할 수 있는 타입

```swift
/* JSON 인코딩 
	1. JSONEncoder 선언
	2. 인스턴스 -> encode -> Data타입
	3. Data타입 -> String타입
*/
struct Person : Codable{
    var name: String
    var age : Int
}

let encoder = JSONEncoder()
encoder.outputFormatting = [.sortedKeys, .prettyPrinted] //JSON 출력 포맷
let walter = Person(name: "walter", age: 100)
let jsonData = try? encoder.encode(walter) //encode

if let jsonData = jsonData, let jsonString = String(data: jsonData, encoding: .utf8) {
    print(jsonString) //{"name":"walter", "age":100}
}


/* JSON 디코딩 
	1. JSONDecoder 선언
	2. String타입 -> Data타입
	3. Data타입 -> decode -> 인스턴스
*/

let decoder = JSONDecoder()
let jsonString = {"name":"walter", "age":100}
var data = jsonString.data(using: .utf8)

if let data = data, let myPerson = try? decoder.decode(Person.self, from: data){
    print(myPerson.name) //walter
    print(myPerson.age) //100
}
```

