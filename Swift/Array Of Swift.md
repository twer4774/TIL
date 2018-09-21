# Array

일련의 순서를 가지는 리스트 형식의 값 0부터 시작되는 인덱스

특징

- 배열에 저장할 데이터의 타입에는 제약이 없음
  단, 하나의 배열에 저장하는 아이템 타입은 모두 같아야 한다.
- 선언 시 저장할 아이템 타입을 명확히 정의해야 한다.
- 배열의 크기는 동적으로 확장 가능하다

```swift
*리터럴(Literal)
 값 자체를 의미. 변수나 상수에 담긴 형태가 아닌 저장되는 값 자체

let size = "180"  => 180이 리터럴

Int(size) => 변수 사용
```



## 배열의 순회 탐색 - for~ in 구문 이용

1. 배열의 길이를 직접 다루는 방식 -> size 이용

   ```swift
   배열의 길이 구하기 array.count
    let length = array.count
    for i in 0 ..< length {
       print("\(i)번째 원소는 \(array[i])")
    }
   ```

 \* 상수 length에 배열의 크기를 할당하는 이유
 직접적으로 for ~ in 구문에 array.count를 직접사용하면, for ~ in 구문을 반복할 때 마다 매번 조건식을 평가하는데 배열의 크기를 매번 다시 계산하게 된다. 이때 실행속도가 떨어지는 등 잠재적 문제의 소지가 될 수 있다.

2. 배열의 순회 특성을 이용하는 방식 -> 이터레이터 이용

   ```swift
    for row in array{
         print("배열원소는 \(row)")
     }
   ```


## 배열의 동적 선언과 초기화

```swift
//Array<아이템 타입>()
var cities = Array<String>() //빈 배열로 초기화
var cities: Array<String> //단순히 배열 선언
cities = Array() //배열 초기화(메모리 공간 할당)

//아이템 타입
var cities = String //배열 선언&초기화
var cities:[String] //배열 선언
cities = String or [] //배열 초기화
```



## 배열 아이템 동적 추가

```swift
//apppend(_:): 배열의 맨 뒤에 추가
//insert(_:at): 원하는 위치에 직접 추가
insert("seoul", at:1)
//append(contentsOf:): 여러인자(배열)추가
append(contentsOf:[data001, data002, ...])
```

> *NSArray, NSMutableArray
>
> 타입이 명확하게 정해지지 않은 불특정형 집합 데이터나 여러종류의 값이 섞여 잇는 집합 데이터를 처리할 때 이용
>
> NSArray - 수정이 필요없는 배열
>
> NSMutableArray - 수정이 필요한 배열

 



 