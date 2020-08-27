#  Primary Number (소수찾기) - 에라토스테네스 체

> - 소수 찾기
>
> - darklight
>
>   sublimevimemacs
>
>   Java 
>
> ###### 문제 설명
>
> 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
>
> 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
> (1은 소수가 아닙니다.)
>
> ##### 제한 조건
>
> - n은 2이상 1000000이하의 자연수입니다.
>
> ##### 입출력 예
>
> | n    | result |
> | ---- | ------ |
> | 10   | 4      |
> | 5    | 3      |
>
> ##### 입출력 예 설명
>
> 입출력 예 #1
> 1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환
>
> 입출력 예 #2
> 1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환
>
> 

## 풀이(맨 아래 통과 코드 있음)

- 테스트는 통과했으나, 효율성에서 엉망인 코드 - 점수 : 68/100

```java
class Solution {
    public int solution(int n) {
        int answer = 0;
        boolean pri = true;
        
        for(int i = 2; i <= n/2+1; i++){
            for(int j = 2; j < i; j++){
                //소수는 1을제외 하고, 1과 자기 자신으로만 나누어지는 수
                //자기 자신이 아닌 다른 수로 나누어지는지 확인
                if(i%j == 0){
                    //소수가 아니다
                    pri = false;
                    break;
                } 
                pri = true;
            }
            if(pri == true){
                answer = answer + 1;
            }
        }
        
        return answer;
    }
}
```

### ArrayList 이용

- 테스트는 모두 통과, 효율 0점 -> 크기가 주어지니까 배열로 바꿔 보자

```java
package com.company;


import java.util.ArrayList;
/**
 * 에라토스테네스의 체 이용
 */
public class PrimeNumber {


    public static int solution(int num) {
        int answer = 0;
        //숫자의 배열
        ArrayList<Integer> numArr = new ArrayList<>();
        //num의 갯수만큼 배열을 생성한다.
        for( int i = 0; i < num+1; i++){
            numArr.add(i);
        }

        for (int j = 0; j < numArr.toArray().length; j++) {
            numArr.get(j);
        }


        //num 이하의 소수를 찾고
        for (int k = 2; k < numArr.size(); k++) {
            //0이면 소수가 아닌것
            if (numArr.get(k) == 0) {
                continue;
            }

            for (int m = k + k; m < numArr.size(); m = m + k) {
                //소수의 배수 만큼씩 제거한다.(0으로 바꾼것이 제거한다는 의미)
                numArr.set(m, 0);
            }
        }

        //0이아닌 갯수 파악
        for (int a = 0; a < numArr.size(); a++) {
            System.out.println("배열의 확인 : " + numArr.get(a));
            if (numArr.get(a) != 0) {
                answer = answer + 1;
            }
        }
        System.out.println("answer : " + answer);
        //1을 제외해야하므로 -1
        answer = answer -1;
        return answer;
    }

    public static void main(String[] args) {
        solution(71);
    }

}

```

### 배열을 이용한 풀이 - 테스트, 효율성 모두 통과

- ArrayList로 처음 구현했을 때, 문제에서 크기를 정해주기 때문에 배열을 이용하는것이 더 효율이 좋을것 같아서 수정을했다
- 예상대로 효율성 테스트도 모두 통과하게 됨

```java

class Solution {
    public int solution(int num) {
        int answer = 0;
       //숫자의 배열
        int[] numArr = new int[num+1];
        //num의 갯수만큼 배열을 생성한다.
        for( int i = 0; i < num+1; i++){
            numArr[i] = i;
        }
        
        //num 이하의 소수를 찾고
        for (int k = 2; k < numArr.length; k++) {
            //0이면 소수가 아닌것
            if (numArr[k] == 0) {
                continue;
            }

            for (int m = k + k; m < numArr.length; m = m + k) {
                //소수의 배수 만큼씩 제거한다.(0으로 바꾼것이 제거한다는 의미)
                numArr[m] = 0;
            }
        }

        //0이아닌 갯수 파악
        for (int a = 0; a < numArr.length; a++) {
            
            if (numArr[a] != 0) {
                answer = answer + 1;
            }
        }
        System.out.println("answer : " + answer);
        //1을 제외해야하므로 -1
        answer = answer -1;
        return answer;
    }
}
```

