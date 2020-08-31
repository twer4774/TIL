# 블랙잭(Black Jack - Brute Force)

> ## 문제
>
> 카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 블랙잭은 카지노마다 다양한 규정이 있다.
>
> 한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.
>
> 김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.
>
> 이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
>
> N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.
>
> ## 입력
>
> 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는다.
>
> 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.
>
> ## 출력
>
> 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.
>
> 
>
> ## 예제 입력 1 복사
>
> ```
> 5 21
> 5 6 7 8 9
> ```
>
> ## 예제 출력 1 복사
>
> ```
> 21
> ```
>
> ## 예제 입력 2 복사
>
> ```
> 10 500
> 93 181 245 214 315 36 185 138 216 295
> ```
>
> ## 예제 출력 2 복사
>
> ```
> 497
> ```
>
> 
>
> ## 출처
>
> [Contest ](https://www.acmicpc.net/category/45)> [Croatian Open Competition in Informatics ](https://www.acmicpc.net/category/17)> [COCI 2011/2012 ](https://www.acmicpc.net/category/19)> [Contest #6](https://www.acmicpc.net/category/detail/73) 1번
>
> - 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
> - 빠진 조건을 찾은 사람: [bupjae](https://www.acmicpc.net/user/bupjae)
> - 문제의 오타를 찾은 사람: [eric00513](https://www.acmicpc.net/user/eric00513) [joonas](https://www.acmicpc.net/user/joonas) [otter66](https://www.acmicpc.net/user/otter66)
>
> ## 알고리즘 분류
>
> - [브루트포스 알고리즘](https://www.acmicpc.net/problem/tag/125)

## 풀이

- 브루트포스법을 이용해서 하나씩 순회함
- 주의할 점은 순회횟수
  - i는 전체 길이의 -2
  - j는 전체 길이의 -1
  - k는 전체길이 만큼

```java
import java.util.Scanner;
public class Main {
   
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int m = scan.nextInt();
        int[] cards = new int[n];
        for (int i = 0; i < n; i++) {
            cards[i] = scan.nextInt();
        }
        
        int answer = 0;
        int max=0;

        //3장을 뽑아서 m과 가장 가까운 숫자를 찾아야 함
        for (int i = 0; i < cards.length-2; i++) {
            for (int j = i+1; j < cards.length-1; j++) {
                for (int k = j+1; k < cards.length; k++) {
                    int temp = cards[i] + cards[j] + cards[k];
                    if(temp > max && temp <= m){
                        max = temp;
                    } 
                }
            }

        }
        answer = max;
        System.out.println(answer);
    }
}
```

