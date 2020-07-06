# Sentinel Method(보초법)

- 선형검색 방법 중 하나
- 일반적인 선형검색에서 두가지 경우의 결과를 생각 해야함
  1. 찾고자 하는 값이 없을때 (실패)
  2. 찾고자 하는 값이 있을때 (성공)
- 위의 두가지 경우로 나누었을때 비용이 발생한다.
- 이것을 줄인것을 보초법이라 하며 배열의 가장 마지막 요소에 찾고자하는 key값을 추가한다(보초를 세운다)
- 결과적으로 하나의 조건식만 판단하게 되므로 비용이 일반적인 linear search보다 50% 감소한다.

```java
import java.util.Scanner;

//선검색(보초법)
public class SentinelMethod {

    //요소수가 n인 배열에서 key와 같은 요소를 보초법으로 선형 검색한다.
    static int linearSerachSen(int[] arr, int n, int key){
        int i = 0;
        arr[n] = key; //보초값인 key를 n번째에 저장

        while (true){
            if(arr[i] == key) {
                break;
            }
            i++;
        }
        return i == n ? -1 : i;
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("배열의 길이: ");
        int num = stdIn.nextInt();
        int[] arr = new int[num+1]; //배열의 마지막에 보초값으 저장해야하므로 +1

        for (int i = 0; i < num; i++){
            System.out.println("arr[" + i + "] : ");
            arr[i] = stdIn.nextInt();
        }

        System.out.println("검색할 값 : "); //키 값 입력
        int key = stdIn.nextInt();

        int idx = linearSerachSen(arr, num, key);

        if (idx == -1){
            System.out.println("배열에 해당하는 값이 없습니다.");
        } else {
            System.out.println(key + "값은 arr[" + idx + "]에 있습니다.");
        }
    }//main
}
```

