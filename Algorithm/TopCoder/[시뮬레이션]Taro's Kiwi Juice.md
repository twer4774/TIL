# [시뮬레이션]Taro's Kiwi Juice

> 타로의 키위주스 문제
> 병에 키위 주스를 재분배하려고 하며, 0 부터 M-1까지 M회 조작
> i번째의 조작은 타로가 병 fromId[i] 부터 병 toId[i]에 키위 주스를 넣는 것을 의미
> fromId[i]가 비었거나, toId[i]가 꽉 차 있는 순간 타로는 더 이상 키위 주스를 넣지 않음
> N개의 요소를 가진 정수 배열 int[]를 리턴
> 배열의 i번째 요소는 모든 주스를 쏟는 작업이 완료되고 i번째 병에 남아 있는 키위 주스의 양
>
> ```
> capcities={20, 20}
> bottoles={5, 8}
> fromId={0} / toId={1}
> Returns: {0, 13}
> *
> capciteis={30, 20, 10}
> bottoles={10, 5, 5}
> fromId={0, 1, 2} / toId={1, 2, 0}
> Returns: {10, 10, 0}
> ```

## 내 풀이

- temp를 두어 bottles[toId[i]]에 저장할 값을 임시로 저장
- bottles[fromId[i]]의 값을 계산
  - temp를 둔 이유 : bottles[toId[i]] 또는 bottles[fromId[i]]의 값은 계속 바뀌므로 계산할 때 마다 새로운 값으로 계산이 되어버림

```java
public class TaroKiwiJuice {

    /**
     * 주스는 병의 용량을 넘을 수 없음
     * @param capacities 병의 용량
     * @param bottles 주스의 양
     * @param fromId 현재 주스가 들어있는 병들 배열
     * @param toId 주스를 옮길 병들 배열
     * @return 주스를 옮긴 작업 뒤의 결과
     *
     * capcities={20, 20}
     * bottoles={5, 8}
     * fromId={0} / toId={1}
     * Returns: {0, 13}
     *
     * capciteis={30, 20, 10}
     * bottoles={10, 5, 5}
     * fromId={0, 1, 2} / toId={1, 2, 0}
     * Returns: {10, 10, 0}
     */
    public static int[] thePouring(int[] capacities, int[] bottles, int[] fromId, int[] toId){

        int[] result = {};
        //from에서 to로 키위주스를 비운다.
        for (int i = 0; i < fromId.length; i++) {
            int temp = 0;
            //capacities[i]와 용량 비교
                //fromId[i]+toId[i] > capacities[i] (용량이 넘칠 때)
            if(bottles[fromId[i]]+bottles[toId[i]] > capacities[toId[i]]){
                //용량 capacities[i]까지 부음
                temp = bottles[fromId[i]]+bottles[toId[i]] - capacities[toId[i]];
                bottles[fromId[i]] = bottles[fromId[i]]+bottles[toId[i]] - capacities[toId[i]];
                bottles[toId[i]] = temp;
            } else {
                //fromId[i]+toId[i] <= capacities[i]
                bottles[toId[i]] = bottles[fromId[i]]+bottles[toId[i]];
                bottles[fromId[i]] = 0;

            }

            System.out.println(i+"번째:");
            for (int b: bottles){
                System.out.println(b);
            }
        }

        result = bottles;

        return result;
    }

    public static void main(String[] args) {
        int[] capacities = {20, 20};
        int[] bottles = {5, 8};
        int[] fromId = {0};
        int[] toId = {1};

        int[] capacities2 = {30, 20, 10};
        int[] bottles2 = {10, 5, 5};
        int[] fromId2 = {0, 1, 2};
        int[] toId2 = {1, 2, 0};
        thePouring(capacities,bottles,fromId,toId);
        thePouring(capacities2,bottles2,fromId2,toId2);
    }
}
```



## 풀이

```java
public class TaroKiwiJuice {

    /**
     * 주스는 병의 용량을 넘을 수 없음
     * @param capacities 병의 용량
     * @param bottles 주스의 양
     * @param fromId 현재 주스가 들어있는 병들 배열
     * @param toId 주스를 옮길 병들 배열
     * @return 주스를 옮긴 작업 뒤의 결과
     */
    public static int[] thePouring(int[] capacities, int[] bottles, int[] fromId, int[] toId){

        for (int i = 0; i < fromId.length; i++) {
            int f = fromId[i];
            int t = toId[i];
            //용량 - 주스의 양 = 여유 공간
            int space = capacities[t] - bottles[t];

            //여유공간(space)가 현재 주스의 양보다 크거나 같다면
            if (space >= bottles[f]){
                int vol = bottles[f];
                //주스를 옮길 주스병에 +vol(=현재 주스의 양)
                bottles[t] += vol;
                bottles[f] = 0;
            } else {
                //여유 공간이 현재 주스의 양 보다 작다면
                int vol = space;
                bottles[t] += vol;
                bottles[f] -= vol;
            }
        }
        return bottles;
    }

    public static void main(String[] args) {
        int[] capacities = {20, 20};
        int[] bottles = {5, 8};
        int[] fromId = {0};
        int[] toId = {1};

        int[] capacities2 = {30, 20, 10};
        int[] bottles2 = {10, 5, 5};
        int[] fromId2 = {0, 1, 2};
        int[] toId2 = {1, 2, 0};
        thePouring(capacities,bottles,fromId,toId);
        thePouring(capacities2,bottles2,fromId2,toId2);
    }
}
```



## 응용

- 조건문을 적게 사용할 것
  - if문 대신 Math.min 등의 값으로 최솟값 찾기
- 옮길 주스의 양과 기존 주스 병의 남은 용량을 비교하면 둘 중 작은 것이 이동량이 됨
  - 기존 주스에 이동량을 추가
  - 옮길 주스에 이동량을 제거

```java
class KiwiJuiceEasy{
  public int[] thePouring(int[] capacities, int[] bottles, int[] fromId, int[] toId){
    for(int i = 0; i < fromId.length; i++){
      int f = fromId[i];
      int t = toId[i];
      
      //bottles[fromId[i]]와 capacties[toId[i]]-bottles[toId[i]] 중 작은 값을 vol로 둠
      //옮길 주스의 양과 기존 주스병의 남은 용량을 비교하여 작은 것이 이동량이 됨
      int vol = Math.min(bottles[f], capacities[t]-bottles[t]);
      
      //옮길 주스에 이동량 제거
      bottles[f] -= vol;
      //기존 주스에 이동량 추가
      bottles[t] += vol;
    }
    
    return bottles;
  }
}
```

