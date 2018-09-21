# 튜플

하나의 튜플에 여러가지 값 저장가능. 단, 선언 후 추가 삭제 등의 변경 불가

(<튜플 아이템1>, <튜플 아이템2>, ...)

tupleValue.0   tupleValue.1 로 인덱스 연결

튜플 값 바인딩 - 독립적인 사용 가능

```swift
let tupleValue: (String, Character, Int, Float, Bool) = ("a", "b", 1, 2.5, true)
let (a, b, c, d, e) = tupleValue
print(a) //a   print(b) b  print(c+2) //3  print(d*2) //5
```

 

튜플을 사용하면 좋은 경우

- 프로그램이 실행되는 동안, 값이 절대 변하지 않아야 하는 상수 성격
             값이 바뀔 가능성을 근본적으로 제거
- 서로 다른 타입들을 집단 자료형으로 주고 받을 때

> *for ~ in 구문 사용불가

 

### 함수나 메서드에서의 튜플이용

```swift
func getTupleValue() -> (String, String, Int){
	return ("t", "v", 100)
}

//함수가 반환하는 튜플을 튜플 상수로 바인딩
let (a, b, c) = getTupleValue()
// a => "t"
// b => "v"
// c => 100
```

 

 

