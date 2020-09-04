# PartSum(분해합) - BruteForce

> ## 문제
>
> 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.
>
> 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
>
> ## 입력
>
> 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
>
> ## 출력
>
> 첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.
>
> 
>
> ## 예제 입력 1 복사
>
> ```
> 216
> ```
>
> ## 예제 출력 1 복사
>
> ```
> 198
> ```
>
> 
>
> ## 출처
>
> [ICPC ](https://www.acmicpc.net/category/1)> [Regionals ](https://www.acmicpc.net/category/7)> [Asia Pacific ](https://www.acmicpc.net/category/42)> [Korea ](https://www.acmicpc.net/category/211)> [Asia Regional - Seoul 2005](https://www.acmicpc.net/category/detail/1067) B번
>
> - 데이터를 추가한 사람: [kimtree97](https://www.acmicpc.net/user/kimtree97) [yjwr0528](https://www.acmicpc.net/user/yjwr0528)
>
> ## 링크
>
> - [ACM-ICPC Live Archive](https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1356)
> - [TJU Online Judge](http://acm.tju.edu.cn/toj/showp2502.html)
>
> ## 알고리즘 분류
>
> - [브루트포스 알고리즘](https://www.acmicpc.net/problem/tag/125)

## 풀이

- 배운점
  - 자릿수를 찾는데 String을 이용할 경우 length 함수를 이용할 수 있다
  - int형의 자릿수를 찾는데는 Math.log10(i)+1을 이용하면된다
- 브루트포스법을 이용
  - 0부터 실시하면 되지만, 오래걸리므로 최솟값을 만들어준다
    - 최솟값은 자릿수 * 9를 한다(9가 나타낼 수 있는 최대 수이므로)
- 생성자들 중 최솟값을 찾는문제이므로, 이미 answer에 값이 들어 있는경우(0이 아닌경우) 저장하지 않고 다음 숫자로 반복문을 넘긴다(continue)

```java

import java.util.Scanner;
public class PartitionSum {
    static int N; //분해합
    
    public static int partSum(int N){
        int answer = 0;
        //자릿수를 알기위해 log10 함수 이용
        int numDigit = (int)Math.log10(N)+1;

        //분해합을 만드는 최소의 생성자 찾기
        //한 자릿수의 최댓값은 9이므로, 자릿수 * 9의 만큼 뺀 값에서부터 브루트포스법 실시

        //예를들어 2자릿수의 분해합이 주어질 경우 최솟값은 N-18
        //N이 34라면
        //최솟값 : 34-18 = 16 => 16부터 부르트포스법을 실시해 34를 만드는 수 찾기

        int min = (N - (numDigit*9)) > 0 ? N - (numDigit*9) : N;
        System.out.println(min);
        for (int i = min; i < N; i++) {
            int temp = i;
            int partSum = 0;
            while(temp>0){
                partSum = partSum + temp%10;
                temp = temp/10;
            }
            //분해합의 결과가 N과 동일하다면 저장
            if((i+partSum) == N){
                //단, 이미 answer에 저장되어있는 경우 패스(최솟값이 저장된 경우)
                if(answer!=0){
                    continue;
                }
                answer = i;
            }
        }

        System.out.println(answer);
        return answer;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        N = scanner.nextInt();

        partSum(N);
    }
}
```

