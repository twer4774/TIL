# Dynamic Programming

- 특정 범위의 값을 구하기 위해 다른 범위에서 계산한 값을 이용하는 방법 = 과거에 구한 해를 이용해 새로운 해를 구함
- 분할 정복 알고리즘과 차이
  - 분할 정복 : 큰 과제를 소규모 과제로 분할하여 정복하는 방법
  - 동적 프로그래밍 : 큰 과제를 소규모과제로 분할하여 정복하지만, 이전에 정복한 값을 이용하여 함수 호출을 줄임
- 단점 : 다른 알고리즘과 다르게 직관적으로 생각하기 쉽지 않음
- 메모이제이션 이용
  - 이전 값을 저장할 때 사용되는 저장기법
  - HashMap 등을 주로 사용함
- 동적 프로그래밍을 사용할 수 있는 조건
  - 작은 문제가 반복적으로 일어나는 경우
  - 작은 문제의 답이 항상 같은 경우
- 대표적으로 피보나치 구현에서 사용할 수 있음
  - Boyer-Moore 문자열 매칭 알고리즘에서도 Skip Table을 이용한 것도 동적프로그래밍 기법이라고도 할 수 있음

## 피보나치 구현

```java
import java.util.HashMap;

public class Fibonacci {

    static int count = 0; //함수 호출 카운터
    static int num = 10; //피보나치 수
    static int result = 0; //결과 값

    static double start, end = 0; //성능측정

    public static void main(String[] args) {
        //일반 피보나치
        start = System.currentTimeMillis();
        result = basicFibo(num);
        end = System.currentTimeMillis();

        /**
         * 기본 피보나치
         */
        System.out.println("기본 피보나치");
        System.out.println("num : " + num + " 결과 : " + result);
        System.out.println("함수 호출 카운터 : " + count + " 수행시간 : " + (end-start) + "ms");
        System.out.println();


        /**
         * 동적 프로그래밍 피보나치
         */
        count = 0;
        result = 0;

        HashMap<Integer, Integer> dp = new HashMap<>();
        start = System.currentTimeMillis();
        result = dpFibo(dp, num);
        end = System.currentTimeMillis();
        System.out.println("동적프로그래밍 피보나치");
        System.out.println("num : " + num + " 결과 : " + result);
        System.out.println("함수 호출 카운터 : " + count + " 수행시간 : " + (end-start) + "ms");

    }

    private static int basicFibo(int num) {
        count++;

        if(num == 0){
            return 0;
        } else if(num <= 2){
            //num이 1 또는 0이면 피보나치 수는 1
            return 1;
        } else {
            return basicFibo(num-1) + basicFibo(num-2);
        }

    }

    private static int dpFibo(HashMap<Integer, Integer> dp, int num) {
        count++;

        //이미 계산한 값이 있으면 그 값을 가지고 이용
        if (dp.containsKey(num)) {
            return dp.get(num);
        } else if(num==0) {
            return 0;
        } else if(num <= 2){
            //num이 1 또는 0이면 피보나치 수는 1
            return 1;
        } else {
            //새로운 피보나치 계산을 dp에 저장함
            int val = dpFibo(dp, num-1) + dpFibo(dp, num-2);
            dp.put(num, val);

            return val;
        }

    }

}
```

- 결과

```
기본 피보나치
num : 10 결과 : 55
함수 호출 카운터 : 109 수행시간 : 0.0ms

동적프로그래밍 피보나치
num : 10 결과 : 55
함수 호출 카운터 : 17 수행시간 : 0.0ms
```

