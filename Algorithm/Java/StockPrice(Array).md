# StockPrice(주식가격)

> - 주식가격
>
> - darklight
>
>   sublimevimemacs
>
>   Java 
>
> ###### 문제 설명
>
> 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
>
> ##### 제한사항
>
> - prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
> - prices의 길이는 2 이상 100,000 이하입니다.
>
> ##### 입출력 예
>
> | prices          | return          |
> | --------------- | --------------- |
> | [1, 2, 3, 2, 3] | [4, 3, 1, 1, 0] |
>
> ##### 입출력 예 설명
>
> - 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
> - 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
> - 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
> - 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
> - 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.

## 풀이

- 스택/큐 카테고리로 분류된 문제인데, 배열로 풂
- j - i : 시간(간격)을 구할 수 있다

```java
class Solution {
    public int[] solution(int[] prices) {
        //배열의 크기 지정
        int[] answer = new int[prices.length];
        
        for (int i = 0; i < answer.length; i++) {
            for (int j = i+1; j < answer.length; j++) {
                
                //순차적으로 진행
                //prices[i]가 크면 j의 인덱스에 i인덱스를 뺀 값을 넣는다.
                if (prices[i] > prices[j]) {
                    answer[i] = j-i;
                    break;
                }
                
                //순차적으로 진행하다 마지막에 다다랐을 경우
                //j가 배열의 마지막 인덱스까지 왔다면 j인덱스 에서 i인덱스를 뺀 결과값을 넣는다.
                if (j==answer.length-1) {
                    answer[i] = j-i;
                }
            }
        }
        return answer;
    }
}
```

