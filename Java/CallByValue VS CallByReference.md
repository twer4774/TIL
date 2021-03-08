# CallByValue VS CallByReference

결론 : 자바는 CallByValue를 사용한다

- 함수의 호출 방식에는 CallByValue(값에 의한 호출)와 CallByReference(주소에 의한 호출)가 존재
  - 자바는 CallByReference가 없음

- SwapEX

```java
//Call By Value
public class SwapTest {

    public static void swap(int x, int y){
        int temp = x;
        x = y;
        y = temp;
    }
    public static void main(String[] args) {
        int x = 10;
        int y = 20;

        System.out.println("before swap x : " + x + " , y : " + y);
        swap(x, y);
        System.out.println("after swap x : " + x + " , y : " + y); /* x: 10 y: 20 */
    }
}


//Call By Reference - 자바에서 지원하지 않으므로 어거지로 만듦
public class SwapTest {

    int value;
    SwapTest(int value){
        //this : 자신의 메모리 공간을 가리킴
        this.value = value;
    }

    public static void swap(SwapTest x, SwapTest y){
        SwapTest temp = x;
        x.value = y.value;
        y.value = temp.value;
    }
    public static void main(String[] args) {
        SwapTest x = new SwapTest(10);
        SwapTest y = new SwapTest(20);


        System.out.println("before swap x : " + x.value + " , y : " + y.value);
        swap(x, y);
        System.out.println("after swap x : " + x.value + " , y : " + y.value); /* x: 20 y: 10 */
    }
}

//효율적인 Swap방법 => 배열 이용 => 되는 이유: 배열을 선언하면 Heap영역에 메모리 공간이 할당 됨
public class SwapTest {

    public static void swap(int[] arr){
        int temp = arr[0];
        arr[0] = arr[1];
        arr[1] = temp;
    }
    public static void main(String[] args) {
        int[] arr = {10, 20};
        
        System.out.println("before swap x : " + arr[0] + " , y : " + arr[1]);
        swap(arr);
        System.out.println("after swap x : " + arr[0] + " , y : " + arr[1]); /* arr[0]: 20 arr[1]: 10 */
    }
}
```

