# 옵셔널

스위프트가 잠재적 오류를 다루는 방법

nil을 사용할 수 있는 타입과 사용할 수 없는 타입을 구분하고, 사용할 수 있는 타입을 가리켜 옵셔널 타입이라고 부른다.

nil : 값이 없음을 의미하는 특수한 값

- 일반 자료형에는 nil값을 할당 할 수 없다.
- 옵셔널만 가능(optional)
             변환하고자 하는 값을 옵셔널 객체로 다시 한번 감싼 형태 optional(123)

## 옵셔널 타입 선언과 정의

자료형 뒤에 물음표(?)를 붙임

```swift
var optInt: Int? //선언
optInt = 3 //정의
```

## 옵셔널 값 처리

- 옵셔널은 연산 가능한 타입이 아님
             Int("123") + Int("123") => 연산불가능

- 옵셔널 언래핑
             optional("123") -> 옵셔널 해제 처리 -> 123      -> 값의 연산

- 옵셔널 해제 방법

- - 명시적 해제

  - - 강제해제

    - - 확실히 옵셔널 값이 nil이 아닌 경우에 이용

      - 강제해제 연산자 ! 이용

      - nil 값에 !이 붙으면 오류 발생

      - - 옵셔널값이 nil 인지 점검 필요

        - 오류 없이 옵셔널 타입을 안전하게 해제하는 방법

        - ```swift
          if intFromStr != nil {
          print("값 변환 성공 \(intFromStr!)")
          } else { 
          print("값 변환 실패") 
          }
          ```


- 비강제해제(옵셔널바인딩)

- - if 문 내에서 조건식 대신 옵셔널 값을 변,상수에 할당하는 구문

  - if 문 내에서의 옵셔널 바인딩 처리

  - - ```swift
      var str ="Swift"
      if let intFromStr = Int(str){
          print("(intFromStr)")
       } else { print("실패") }
      ```

- guard문을 이용한 옵셔널 바인딩

- - guard문의 특성상 함수나 메소드에서만 사용가능
                 guard문의 특성: 조건에 맞지 않으면 함수의 실행 종료
                 (앱은 거의 함수, 메소드로 이루어짐)

  - 이용하는 경우

  - - 실행의 흐름상 옵셔널 값이 해제되지 않으면, 더 이상 진행이 불가능할 정도로 큰 일이 생길때에만 사용

  - ```swift
    func intStr(str: String){
    guard let intFromStr = Int(str) else {
    	print("실패")
    	return
    }
    print("(intFromStr)") }
    ```

- 묵시적 해제

- - 컴파일러에 의한 자동해제

  - - 옵셔널 객체의 값을 비교할때 즉, 비교연산자 사용시에 컴파일러에 의해 자동으로 해제됨

    - ```swift
      let tempInt = Int("123")
      tempInt == 123  //true
      tempInt == Optional(123) //true
      tempInt! == 123  //true
      tempInt! == Optional(123) //true
      ```

  - !연산자를 이용한 자동해제(묵시적 해제)

  - - ```swift
      var str: String! = "swift Optional"
      print(str)
      ```

- 변수의 값에 nil이 될 가능성이 있다면 사용 불가

  사용하는 경우

- - 형식상 옵셔널로 정의해야 하지만, 실제로 사용할때는 절대 nil 값이 대입될 가능성이 없는 변수일때

  - - ```swift
      var value: Int! = Int("123")
      //클래스나 구조체에서 유용하게 사용됨 => 멤버변수의 선언과 초기화를 분리할 경우
      ```

 