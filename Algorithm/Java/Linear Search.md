# Linear Search(선형검색, 순차검색)

무작위로 늘어놓은 데이터 모임에서 검색을 수행

- 원하는 키 값을 갖는 요소를 만날 때까지 맨 앞부터 순서대로 요소를 검색
- 검색이 끝나는 경우
  1. 검색할 값을 발견하지 못하고 배열의 끝을 지나간 경우 - 실패
  2. 검색할 값과 같은 요소를 발견한 경우 - 성공
  3. 위의 두가지 결과값이 필요한 경우 비용발생 -> 보초법이용(sentinel method)

- while문 이용

```java
import java.util.Scanner;

//선형 검색
public class LinearSearch {
    //찾으려는 key 값과 요소의 값을 비교하여 검색
    static int linearSearch(int[] arr, int n, int key){
        int i = 0;

        //while문을 사용한다. n번째 항목까지 실패시 -1 반환
        while(true){ //true이므로 무한반복
            if( i == n ) return -1; //실패
            if( arr[i] == key ) return i; //검색 성공
            i++;
        }

    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        //num 길이의 배열 생성
        System.out.println("배열의 길이: ");
        int num = stdIn.nextInt();
        int[] arr = new int[num];

        //배열에 요소값 넣기
        for (int i = 0; i < num; i++){
            System.out.println("x[" + i + "] :");
            arr[i] = stdIn.nextInt();
        }

        //key 값 입력
        System.out.println("검색할 키 값");
        int key = stdIn.nextInt();

        int idx = linearSearch(arr, num, key); //배열의 인덱스 값 구하기. -1이면 검색 실패
        if (idx == -1){
            System.out.println("검색 실패");
        } else {
            System.out.println("arr[" + idx + "] 요소에 있음");
        }

    }//main
}
```

- for문 이용

```java
staic int linearSearch(int[] arr, int n, int key){
  for(int i = 0; i < n; i++){
    if(a[i] == key)
      return i; //검색 성공(인덱스를 반환)
    return -1; //검색 실패(-1반환)
  }
}
```

- while문을 쓰는것 보다는 for문을 쓰는것이 더 간결하다.
- while문에서 조건값을 true일때 무한 반복되는데 "특정 조건을 만족할때까지 반복문을 실행" 할 경우 주로 쓰인다
  - ex) 키보드로부터 입력받은 값이 quit이면 종료, 아니면 다른일 실행 => while문 & break 이용