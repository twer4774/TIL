# Complexity (복잡도)

- 알고리즘의 성능을 객관적으로 평가하는 기준

  1. 시간 복잡도 : 실행에 필요한 시간을 평가한 것
  2. 공간 복잡도 : 기억영역과 파일 공간이 얼마나 필요한가를 평가한 것

- 선형 검색 시간의 복잡도

- ```java
   static int linearSearch(int[] arr, int n, int key){
  1        int i = 0;
  
          //while문을 사용한다. n번째 항목까지 실패시 -1 반환
  2        while(true){ //true이므로 무한반복
  3        if( arr[i] == key ) 
  4  					return i; //검색 성공
  5           i++;
          }
  6				return -1; //검색 실패
      }
  ```

  - 1, 4, 6은 한번만 실행 O(1)
  - 배열의 끝에 도달했는지 판단하는 2와 key값의 비교를 하는 3의 평균 실행횟수는 n/2 => O(n) n에 비례하는 횟수만큼 실행하는 경우

   ==> O(n)의 복잡도를 가짐

- 복잡도 계산 공식

- ```
  O(f(n)) + O(g(n)) = O(max(f(n), g(n)))
  ```

- 이진 검색의 시간 복잡도

```java
	static int binarySearch(int[] arr, int n, int key){
1        int pl = 0; //검색 범위의 첫 인덱스
2        int pr = n - 1; //검색 범위의 마지막 인덱스

        do{
3           int pc = (pl + pr) / 2; //중앙 요소의 인덱스
4            if(arr[pc] == key){
5                return pc; //검색 성공
6            } else if (arr[pc] < key) {
7                pl = pc + 1; //검색 범위를 뒤쪽 절반으로 좁힘
            } else {
8                pr = pc - 1; //검색 범위를 앞쪽 절반으로 좁힘
            }
9        }while( pl <= pr );

10        return -1; //검색 실패
```

- 1, 2, 5, 10 => O(1)

- 3, 4, 6, 7, 8, 9 => log n => O(log n)

  ==> O(log n)의 복잡도

- 복잡도의 대소 관계

```
1 logn  n nlogn n^2 n^3 n^k 2^n
```

