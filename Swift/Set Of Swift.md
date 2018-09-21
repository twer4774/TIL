# 집합(Set)

같은 타입의 중복 없는 값 저장

내부적으로 Hash 연산의 결과값을 이용하여 데이터 저장

> *해시연산
>
> 임의의 입력된 메시지를 고정길이이의 데이터 크기로 변환하는 알고리즘
>
> 좋은 해시 알고리즘: MD5, SHA1, SHA256
>
> 복호화가 복잡하기 때문에, 복호화가 필요없는 암호화에 이용 

```swift
var genres: Set = ["Classsic", "Rock"] //집합 정의
//insert(_:) 추가   remove(_:) 삭제    removeAll() 모두 삭제
for g in genres.sorted(){ } //정렬된 결과 출력
```

## 기본집합연산

-intersection(_:) 교집합

-symmeticDifference(_:) 어느 한쪽에만 있는 아이템으로 새로운 집합 생성

-union(_:) 합집합

-subtract(_:) 차집합

 

## 부분집합과 포함관계 판단연산

-isSubSet(of:): 주어진 집합의 값 전체가 특정집합에 포함되는지 판단하여 true, false 반환

-isSuperSet(of:): 집합이 다른 집합의 상위 집합역할을 하는가 판단

-isDisjoint(with:): 아무런 공통값이 없을때, true   하나라도 공통이면 false

 

 

