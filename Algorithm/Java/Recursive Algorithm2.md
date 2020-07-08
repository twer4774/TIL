# Recursive Algorithm2(재귀 알고리즘)

재귀 알고리즘을 비재귀적으로 구현하는 방법

### 재귀알고리즘

```java
import java.util.Scanner;

//재귀 함수 이해하기

public class Recur {
    //재귀함수
    static void recur(int n){
        if (n > 0 ){
            recur(n - 1);
            System.out.println(n);
            recur(n - 2);
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("정수 입력: ");
        int x = stdIn.nextInt();

        recur(x);

    }//main
}
```

- ### 하향식 분석

```
1. recur(3)을 실행
2. 4를 출력
3. recur(2)
```

- 2에서 4를 바로 출력하지 않고, 1에서 recur(3)의 재귀를 완료한 다음 출력됨

- ### 상향식 분석

```
1. recur(0) 실행
2. 1을 출력
3. recur(-1) 실행
--- recur(2) ---
4. recur(1) 실행
5. 2를 출력
6. recur(0) 실행
```

- 1, 3에서는 출력할 내용이 없음 따라서 2에서의 1만 출력
- 4, 6에서는 출력할 내용이 없음 따라서 5에서의 2만 출력 

## 재귀 알고리즘의 비재귀적 표현

### 꼬리 재귀 제거

메서드의 꼬리에서 재귀 호출하는 메서드 recur(n - 2)라는 말은 '인자로 n -2를 전달하여 recur 메서드를 호출한다'

=> n의 값을 n - 2로 업데이트하고 메서드의 시작 지점으로 돌아감

```java
//꼬리 재귀 제거(비재귀적으로 재귀함수 구현)
    static void recur(int n){
        while( n > 0 ){
            recur(n - 1); //문제 : 여기서 나오는 재귀를 제거하기 쉽지 않음
            System.out.println(n);
            n = n - 2;
        }
    }
```

- '문제' 주석에 있는 재귀를 제거하기 쉽지 않음 - 계산된 값을 임시로 저장할 공간이 필요함
- Stack 이용
- 스택을 이용한 비재귀적 recur

```java
  //스택을 이용한 비재귀적구현
    static void recur(int n){
        IntStack s = new IntStack(n);
        
        while(true){
            if(n>0){
                s.push(n);
                n = n - 1;
                continue;
            }
            if(s.isEmpty() != true) { //스택이 비어있지 않다면
                n = s.pop();
                System.out.println(n);
                n = n - 2;
                continue;
            }
            break;
        }
    }
```

