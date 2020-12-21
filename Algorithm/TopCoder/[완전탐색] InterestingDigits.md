# [완전탐색] InterestingDigits

> 재밌는 수학
>
> 숫자 3과 9는 10진수에서 각 자릿수의 합이 각 3과 9의 배수가 됨
>
> 118 * 3 = 354  —> 3+5+4 = 12 (3의배수)
>
> 75 * 9 = 675 —> 6+7+5 = 18 (9의배수)
>
> n진법이 주어졌을 때, 위와 같은 성질을 가진 수를 오름차순으로 모두 리턴

## 내 풀이

- n진법-1의 약수 구하기
- 합동식(뭔지 모르고 진법과 예제 리턴값을 비교했을때 그냥 n진법-1의 약수를 찾으면 되겠구나 했는데 이런 증명이 있었음)
  - 1과 base의 차가 n으로 나누어 떨어지면 어떤 자릿수라도 base로 나눈 나머지가 동일하다는 성질
- 처음에는 base-1을 먼저 arrayList에 추가하고 나머지 약수들을 구한 뒤 정렬을 실행
  - Collections.sort(arryList);
  - base-1을 처음에 넣지 않고 for문으로 넣게되면 정렬 할 필요 없어짐

```java
import java.util.ArrayList;
import java.util.Arrays;

public class InterestingDigits {

    public static int[] digits(int base){
        
        //내 풀이법 : n진수-1의 약수들
        
        ArrayList<Integer> arrayList = new ArrayList<Integer>();

        for (int i = 2; i < base; i++) {
            //나머지가 0이면 base-1의 약수
            if ((base-1)%i == 0){
                //약수이면 arrayList에 추가
                arrayList.add(i);
            }
        }

        System.out.println("arrayList size : " + arrayList.size());

      	//Collections.sort(arrayList); //base-1을 처음에 넣지 않으면 정렬할 필요 없음
      
        int[] result = new int[arrayList.size()];

        //int[]로 변환 방법1
//        for (int i = 0; i < arrayList.size(); i++) {
//            result[i] = arrayList.get(i);
//        }

        //int[]로 변환 방법2
        result = arrayList.stream().mapToInt(i -> (int) i).toArray();

        for (int i : result) {
            System.out.println(i);
        }


        return result;
    }
    public static void main(String[] args) {
        digits(10); //{3, 9}
        digits(3); //{2}
        digits(9); //{2, 4, 8}
        digits(26); //{5, 25}
        digits(30); //{29}
    }
}
```

