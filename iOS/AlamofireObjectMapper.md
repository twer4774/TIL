# AlamofireObjectMapper

https://github.com/tristanhimmelman/AlamoFireObjectMapper

- Alamofire를 확장한 형태

- JSON형태의 응답을 ObjectMapper를 이용해 swift 객체로 변환함

  - ObjectMapper: JSON을 클래스나 구조체의 모델 객체로 변환해주는 프레임워크

    - https://github.com/tristanhimmelman/ObjectMapper

    - 기능

      - JSON을 객체로 매핑
      - 객체를 JSON으로 매핑
      - 중첩된 객체(독립형, 배열 또는 사전)
      - 매핑 중 커스텀 변환
      - 구조체 지원
      - 변경할 수 없도록 지원

    - 기본

      - 매핑을 지원하기 위해 클래스나 구조체는 Mappable를 포함하는 프로토콜을 구현하기만 하면 됨

      - ```swift
        protocol Mappable{
        	init?(map: Map)
        	mutating func mapping(map: Map)
        }
        ```

      - <- 오퍼레이터로 변수에 JSON 객체를 매핑함

      ```swift
      class User: Mappable{
          var username: String?
          var age: Int?
          var weight: Double!
          var array: [Any]?
          var dictionary: [String : Any] = [:]
          var bestFreind: User?
          var friends: [User]?
          var birthday: Date?
          
          required init?(map: Map){
              
          }
          
          //Mappable
          func mapping(map: Map){
              username 	<- map["username"]
              age 		<- map["age"]
              weight 		<- map["weight"]
              array 		<- map["arr"]
              dictionary	<- map["dict"]
              bestFriend	<- map["best_friend"]
              friends		<- map["firends"]
              birthday	<- (map["birthday"], DateTransform())
          }
      }
      
      struct Temperatur: Mappable{
          var celsius: Double?
          var fahrenheit: Double?
          
          init?(map: Map){
              
          }
          
          mutaing func mapping(map: Map){
              celsius		<- map["celsius"]
              fahrenheit	<- map["fahrenheit"]
          }
      }
      
      ```

      - Mappable를 포함해 ObjectMapper는 쉽게 JSON으로 부터 가져올 수 있게 됨

      ```swift
      //JSONString을 모델 객체로 변환
      let user = User(JSONString: JSONString)
      
      //모델 객체를 JSONString으로 변환
      let JSONString = user.toJSONString(prettyPrint: true)
      
      //Mapper.swift 이용
      let user = Mapper<User>().map(JSONString: JSONString)
      let JSONString = Mapper().toJSONString(user, prettyPrint: ture)
      ```

## AlamofireObjectMapper 이용

```swift
//URL로 부터 받아온 날씨 데이터
{
    "location": "Toronto, Canada",    
    "three_day_forecast": [
        { 
            "conditions": "Partly cloudy",
            "day" : "Monday",
            "temperature": 20 
        },
        { 
            "conditions": "Showers",
            "day" : "Tuesday",
            "temperature": 22 
        },
        { 
            "conditions": "Sunny",
            "day" : "Wednesday",
            "temperature": 28 
        }
    ]
}
```

```swift
//AlamofireObjectMapper 이용
let URL = "https://raw.githubusercontent.com/tristanhimmelman/AlamofireObjectMapper/d8bb95982be8a11a2308e779bb9a9707ebe42ede/sample_json"
Alamofire.request(URL).responseObject { (response: DataResponse<WeatherResponse>) in
	let weatherResponse = response.result.value
	print(weatherResponse?.location)
                                       
	if let threeDayForecast = weatherResponse?.threeDayForecast{
	for forecast in threeDayForcast{
        	print(forecast.day)
			print(forecast.temperature)
		}
    }
}
```

- WeatherResponse객체는 ObjectMapper의 Mappable 프로토콜을 준수 함

```swift
import ObjectMapper

class WeatherResponse: Mappable{
    var location: String?
    var threeDayForecast: [Forecast]?
    
    required init?(map: Map){
        
    }
    func mapping(map: Map){
        location	<- map["location"]
        threeDayForecast <- map["three_day_forecast"]
    }
}

class Forecast: Mappable{
    var day: String?
    var temperature: Int?
    var conditions: String?
    
    required init?(map: Map){
        
    }
    func mapping(map: Map){
        day	<- map["day"]
        temperature	<- map["temperature"]
        conditions	<- map["conditions"]
    }
}
```

