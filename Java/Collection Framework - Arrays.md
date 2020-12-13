# Collection Framework - Arrays

### 배열의 복사 - copyOf(), copyOfRange()

- copyOf() - 배열의 전체 복사
- copyOfRange() - 배열의 지정된 범위 복사. 범위의 끝은 포함되지 않음

```java
int[] arr = {0, 1, 2, 3, 4};
int[] arr2 = Arrays.copyOf(arr, arr.length); //arr2 = [0, 1, 2, 3, 4]
int[] arr3 = Arrays.copyOf(arr, 3); //arr3 = [0, 1 ,2]
int[] arr4 = Arrays.copyOf(arr, 7); //arr4 = [0, 1, 2, 3, 4, 0, 0]
int[] arr5 = Arrays.copyOfRange(arr, 2, 4); //arr5 = [2, 3]
int[] arr6 = Arrays.copyOfRange(arr, 0, 7); //arr6 = [0, 1, 2, 3, 4, 0, 0]
```

### 배열 채우기 - fill(), setAll()

- fill() - 배열의 모든 요소를 지정된 값으로 채움
- setAll() - 배열을 채우는데 사용할 함수형 인터페이스를 매개변수로 받음
  - 함수형 인터페이스를 구현한 객체를 매개변수로 지정하던가 람다식으로 지정해야 함

```java
int arr = new int[5];
Arrays.fill(arr, 9); //arr = [9, 9, 9, 9, 9]
Arrays.setAll(arr, () -> (int)(Math.random()*5)+1); //arr = [1, 5, 2, 1, 1]
```

### 배열의 정렬과 탐색  - sort(), binarySearch()

- sort() - 배열의 정렬
- binarySearch() - 요소 검색. 인덱스를 반환하며, 중복 값이 있을때는 어떤 값이 반환되는지는 랜덤
  - 반드시 정렬된 상태에서 이용할것. 정렬되지 않은 상태일 경우 잘못된 결과를 반환

```java
int[] arr = {3, 2, 0, 1, 4};
int idx = Arrays.binarySearch(arr, 2); 
//정렬된 상태가 아니므로 binarySearch는 잘못된 값을 반환 => idx = -5

Arrays.sort(arr);
System.out.println(Arrays.toString(arr)); //[0, 1, 2, 3, 4]
int idx = Arrays.binarySearch(arr, 2); //idx = 2 올바른 결과 반환
```

### 문자열의 비교와 출력 - equals(), toString()

- equlas()는 일차원 배열에서만 사용
- eepEquals()는 다차원 배열에서 사용

```java
String[][] strD = new String[][] { {"aaa", "bbb"}, {"AAA", "BBB"} };
String[][] strD2 = new String[][] { {"aaa", "bbb"}, {"AAA", "BBB"} };

//다차원 배열이므로 deepEquals를 이용해야 함
System.out.println(Arrays.equals(strD, strD2)); //false
System.out.println(Arrays.deepEquals(strD, strD2)); //true
```

- toString()은 일차원 배열에서 사용
- deepToString()은 다차원 배열에서 사용
  - 모든 요소를 재귀적으로 접근해서 문자열을 구성함

```java
int[] arr = {0 1, 2, 3, 4};
int[][] arr2D = { {11,12}, {21,22} };

System.out.println(Arrays.toString(arr)); //[0, 1, 2, 3, 4]
System.out.println(Arrays.deepToString(arr2D)); //[[11, 12], [21, 22]]
```

### 배열을 List로 반환 - asList(Object… a)

- asList로 배열을 List로 변환할 수 있지만, List의 크기를 변경할 수 없음(추가, 삭제 불가. 내용 변경은 가능)

```java
List list = Arrays.asList(new Integer[]{1,2,3,4,5}); //list = [1, 2, 3 ,4, 5]
List list = Arrays.asList(1,2,3,4,5); //list = [1, 2, 3 ,4, 5]
list.add(6) ; //예외발생  

//만약, 크기를 변경(추가, 삭제)할 수 있는 리스트가 필요하다면
List list = new ArrayList(Arrays.asList(1, 2, 3, 4, 5)); 
```

