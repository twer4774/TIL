# Full Search(완전탐색) - 수학포기자

> - 모의고사
>
> - darklight
>
>   sublimevimemacs
>
>   Java 
>
> ###### 문제 설명
>
> 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
>
> 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
> 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
> 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
>
> 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.
>
> ##### 제한 조건
>
> - 시험은 최대 10,000 문제로 구성되어있습니다.
> - 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
> - 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
>
> ##### 입출력 예
>
> | answers     | return  |
> | ----------- | ------- |
> | [1,2,3,4,5] | [1]     |
> | [1,3,2,4,2] | [1,2,3] |
>
> ##### 입출력 예 설명
>
> 입출력 예 #1
>
> - 수포자 1은 모든 문제를 맞혔습니다.
> - 수포자 2는 모든 문제를 틀렸습니다.
> - 수포자 3은 모든 문제를 틀렸습니다.
>
> 따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.
>
> 입출력 예 #2
>
> - 모든 사람이 2문제씩을 맞췄습니다.



## 풀이

- 가장 큰 수를 구해야 한다. 단, 큰수가 2개일수도 3개일수도 있다
  - java.lang.Math.max 함수가 있지만, 프로그래머스에 동작하지 않음
  - 노가다로 구현
- 자바의 일반 배열에서는 동적으로 값을 할당하기 어려워 ArrayList에 처음에 값을 넣어준뒤 마지막에 일반 Array로 반환했다.

```java
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] answers) {
       ArrayList<Integer> tempList = new ArrayList<Integer>();

        int[] user1 = {1, 2, 3, 4, 5}; //5
        int[] user2 = {2, 1, 2, 3, 2, 4, 2, 5}; //8
        int[] user3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}; //10

        int user1cnt = 0;
        int user2cnt = 0;
        int user3cnt = 0;


        for (int i = 0; i < answers.length; i++) {
            //user1
            if(answers[i] == user1[i%5]){
                user1cnt++;
            }
            //user2
            if (answers[i] == user2[i%8]) {
                user2cnt++;
            }
            //user3
            if (answers[i] == user3[i%10]) {
                user3cnt++;
            }

        }

        /**
         * 세 값의 크기를 확인해야 함
         * 1. 모두 같은 경우
         * 2. user1cnt가 제일 큰 경우
         *  2-1. user1cnt만 제일 큰 경우
         *  2-1. user1cnt와 user2cnt가 같은 경우
         *  2-2. user1cnt와 user3cnt가 같은 경우
         * 3. user2cnt가 제일 큰 경우
         *  3-1. user2cnt만 제일 큰 경우
         *  3-2. user2cnt와 user1cnt가 같은 경우 (2-1과 중복)
         *  3-3. user2cnt와 user3cnt가 같은 경우
         * 4. user3cnt가 제일 큰 경우
         *  4-1. user3cnt만 제일 큰 경우
         *  4-2. user3cnt와 user1cnt가 같은 경우 (2-2와 중복)
         *  4-3. user3cnt와 user2cnt가 같은 경우 (3-3과 중복)
         */

        //1
        if(user1cnt == user2cnt && user2cnt == user3cnt){
            tempList.add(1);
            tempList.add(2);
            tempList.add(3);
        }
        //2
        else if(user1cnt >= user2cnt && user1cnt >= user3cnt){
            //2-1
            if(user1cnt != user2cnt && user1cnt != user3cnt){
                tempList.add(1);
            }
            //2-2
            else if(user1cnt == user2cnt){
                tempList.add(1);
                tempList.add(2);
            }
            //2-3
            else if(user1cnt == user3cnt){
                tempList.add(1);
                tempList.add(3);
            }
        }
        //3
        else if(user2cnt >= user1cnt && user2cnt >= user3cnt){
            //3-1
            if(user2cnt != user1cnt && user2cnt != user3cnt){
                tempList.add(2);
            }
            //3-3
            else if(user2cnt == user3cnt){
                tempList.add(2);
                tempList.add(3);
            }
        }
        //4
        else if(user3cnt >= user1cnt && user3cnt >= user2cnt){
            //4-1
            tempList.add(3);

        }

        //ArrayList To Array
        int[] answer = new int[tempList.size()];
        for (int k = 0; k < answer.length; k++) {
            answer[k] = tempList.get(k).intValue();
        }

        return answer;
    }
}
```

## 결과

![image-20200828212914105](/Users/wonik/Library/Application Support/typora-user-images/image-20200828212914105.png)