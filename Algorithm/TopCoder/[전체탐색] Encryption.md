# [전체탐색] Encryption

> 전체 탐색
>
> TopCoder Security Agency
>
> 새로운 암호화 시스템 구축
>
> 숫자로 구성된 리스트를 입력 받으면, 요소 중 하나에 1을 더하고 모든 요소들을 곱한 값 중 가장 큰 값을 구함
> 

## 내풀이

- 이중 for문 이용 
- for문을 돌려서 요소의 값을 1 증가시킨 후 다시 원래대로 되돌림
- for문을 줄일 수 있는 방법은 없을까? => 가장 작은 숫자에 1을 더하기만 하면 됨

```java
public class TSAEncryption {

    static int[] inputList = {1, 2, 3}; //12
    static int[] inputList2 = {1, 3, 2, 1, 1, 3}; //36
    static int[] inputList3 = {1000, 999, 998, 997, 996, 995}; //986074810223904000
    static int[] inputList4 = {1, 1, 1, 1}; //2

    public static long encrypt(int[] numbers){
        long result = 0;
        long multiply = 1;

        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = numbers[i] + 1;
            for (int j = 0; j < numbers.length; j++) {
                multiply = multiply * numbers[j];

            }

            //원래 값으로 초기화
            numbers[i] = numbers[i] - 1;
            result = Math.max(multiply, result);
            multiply = 1;
        }

        System.out.println(result);
        return result;
    }

    public static void main(String[] args) {
        encrypt(inputList);
        encrypt(inputList2);
        encrypt(inputList3);
        encrypt(inputList4);
    }
}

/*
12
36
986074810223904000
2
*/
```



## 다른 풀이

- 가장 작은 수를 찾아 1을 더한 후 곱하면 가장 큰 수가 됨
- 증명
  - +1을하면 곱의 증가율이 (n+1)/n 
  - 따라서 n이 작으면 작을수록 값이 커짐

```java
public static long encrypt(int[] numbers){
        long result = 1;
        Arrays.sort(numbers);
        numbers[0]++;
        for (int i = 0; i < numbers.length; i++) {
            result = result * numbers[i];
        }

        System.out.println(result);
        return result;
    }
```

