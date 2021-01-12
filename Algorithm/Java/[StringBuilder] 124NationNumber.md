# [StringBuilder] 124NationNumber (124나라의 숫자)

> - 124 나라의 숫자
> - darklight
>
> - sublimevimemacs
>
> - Java 
>
> ###### 문제 설명
>
> 124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.
>
> 1. 124 나라에는 자연수만 존재합니다.
> 2. 124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
>
> 예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.
>
> | 10진법 | 124 나라 | 10진법 | 124 나라 |
> | ------ | -------- | ------ | -------- |
> | 1      | 1        | 6      | 14       |
> | 2      | 2        | 7      | 21       |
> | 3      | 4        | 8      | 22       |
> | 4      | 11       | 9      | 24       |
> | 5      | 12       | 10     | 41       |
>
> 자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.
>
> ##### 제한사항
>
> - n은 500,000,000이하의 자연수 입니다.
>
> ------
>
> ##### 입출력 예
>
> | n    | result |
> | ---- | ------ |
> | 1    | 1      |
> | 2    | 2      |
> | 3    | 4      |
> | 4    | 11     |

## 내 풀이

- 진법 변환과 문자열 처리를 합친 문제
- 문자열을 다루기 위해 String보다 StringBuilder를 이용하는 것이 좋음
- 3으로 나누어서 진법 변환 문제처럼 풂
  - 진법 변환시 거꾸로 읽어 가므로, 마지막에 reverse() 이용

```java
class Solution {
    public String solution(int n) {
        String answer = "";
        
        //문자열을 자유롭게 다루기 위해서는 String보다는 StringBuffer, StringBuilder를 사용. StringBuffer는 멀티쓰레드에서 동기화 문제가 있어서 StringBuilder 추천
        StringBuilder sb = new StringBuilder();

        while(0 < n) {
            //3으로 나눈 값을 저장
            int remainder = n%3;
            n = n/3;
            //6일 경우 생각하면 쉬움
            if(0 == remainder) {
                n = n -1;
                //나머지가 0이면 4를 강제로 주입시켜 줌
                remainder = 4;
            }

            sb.append(remainder);
        
        } //while
        
        //거꾸로 출력(이진수 등 계산할때 거꾸로 올라가면서 적어야 함)
        answer = sb.reverse().toString();
        
        return answer;
    }
}
```

![image-20210111141536821](/Users/wonik/Library/Application Support/typora-user-images/image-20210111141536821.png)

## 다른 사람의 풀이

- 내가 풀고 싶었던 방식으로 1, 2, 4의 값을 미리 배열에 저장하고 불러 오는 방식 이용
  - 4, 1, 2 로 배열 저장한 것이 주요. 왜 정직하게 1, 2, 4로 넣을려고 했을까...
- Comment : 바이너리 트리에서 경로 따라가며 레이블링 하던 것처럼, 자식을 3개 갖는 ternary tree를 따라가며 레이블링 하는 것입니다

```java
public static String solution(int n){
        String[] num = {"4","1","2"};
        String answer = "";

        while(n > 0){
            answer = num[n % 3] + answer;
            n = (n - 1) / 3;
        }

        System.out.println(answer);
        return answer;
    }
```

