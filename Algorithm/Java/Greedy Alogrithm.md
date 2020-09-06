# Greedy Algorithm (그리디알고리즘, 탐욕법)

- 최적해를 구하는 상황에서 사용하는 방법
- 여러 선택지 중 현재 가장 좋다고 판단되는 것을 선택
- 항상 최상의 선택을 보장하진 않는다
- 대표적으로 동전지불 문제



## 백준 거스롬돈 문제

> ## 문제
>
> 타로는 자주 JOI잡화점에서 물건을 산다. JOI잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고, 언제나 거스름돈 개수가 가장 적게 잔돈을 준다. 타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.
>
> 예를 들어 입력된 예1의 경우에는 아래 그림에서 처럼 4개를 출력해야 한다.
>
> ![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/5585/1.png)
>
> ## 입력
>
> 입력은 한줄로 이루어져있고, 타로가 지불할 돈(1 이상 1000미만의 정수) 1개가 쓰여져있다.
>
> ## 출력
>
> 제출할 출력 파일은 1행으로만 되어 있다. 잔돈에 포함된 매수를 출력하시오.
>
> 
>
> ## 예제 입력 1 복사
>
> ```
> 380
> ```
>
> ## 예제 출력 1 복사
>
> ```
> 4
> ```
>
> 
>
> ## 출처
>
> [Olympiad ](https://www.acmicpc.net/category/2)> [일본정보올림피아드 ](https://www.acmicpc.net/category/100)> [일본정보올림피아드 예선 ](https://www.acmicpc.net/category/101)> [JOI 2008 예선](https://www.acmicpc.net/category/detail/553) 1번
>
> - 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon) [sbjwin](https://www.acmicpc.net/user/sbjwin)
> - 문제의 오타를 찾은 사람: [roeniss](https://www.acmicpc.net/user/roeniss) [sgchoi5](https://www.acmicpc.net/user/sgchoi5)
>
> ## 알고리즘 분류
>
> - [그리디 알고리즘](https://www.acmicpc.net/problem/tag/33)

## 풀이

```java
package com.company;

import java.util.Scanner;

/**
 * Greedy Algorithm
 * 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고, 언제나 거스름돈 개수가 가장 적게 잔돈을 준다.
 * 타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때,
 * 받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성
 */

/*
입력값 = 지불할 액수
출력값 = 동전의 갯수
 */
public class ChangeMoney {

    private static int standardMoney;
    private static int changes;
    private static int[] coins;
    private static int answer;
    private static int idx;

    public static void main(String[] args) {
        standardMoney  = 1000;
        coins = new int[]{500, 100, 50, 10, 5, 1};
        answer = 0;
        idx = 0;

        Scanner scan = new Scanner(System.in);
        int bill = scan.nextInt();

        changes = standardMoney - bill;
        greedy(changes);
        System.out.println(answer);
    }

    private static void greedy(int changes) {
        while(changes != 0){
            int change = changes / coins[idx];
            changes = changes - (change * coins[idx++]);
            answer = answer + change;
        }
    }
}
```



## 백준 동전0

## 문제

준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

## 출력

첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.



## 예제 입력 1 복사

```
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
```

## 예제 출력 1 복사

```
6
```

## 예제 입력 2 복사

```
10 4790
1
5
10
50
100
500
1000
5000
10000
50000
```

## 예제 출력 2 복사

```
12
```



## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

## 알고리즘 분류

- [그리디 알고리즘](https://www.acmicpc.net/problem/tag/33)

## 풀이

- 위의 예제와 같이 그리디를 쓰면 쉽게 해결 가능

```java
import java.util.Scanner;

public class Main {
    private static int[] coins;
    private static int N; //동전의 종류 갯수 - 여기서는 coins로 대체
    private static int K; // 지불할 금액
    private static int idx;
    private static int answer;

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        N = scan.nextInt();
        K = scan.nextInt();
        idx = N-1;
        answer = 0;
        coins = new int[N];
        for (int i = 0; i < N; i++) {
            coins[i] = scan.nextInt();
        }

        payMoney(K);
        System.out.println(answer);
    }

    private static void payMoney(int k) {
        while(k != 0){
            int pay = k / coins[idx];
            k = k - (pay * coins[idx--]);
            answer = answer + pay;
        }
    }
}
```

