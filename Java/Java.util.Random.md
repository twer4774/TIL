# Java.util.Random

```java
int num = (int) (Math.random() * 6) + 1;
int num = new Random().nextInt(6) + 1; //1~6사이의 정수 반환
```



### Math.random()을 사용한 유용한 메서드

```java
int[] fillRand(int[] arr, int from, int to){} //배열 arr을 from과 to범위의 값들로 채워서 반환
int[] fillRnad(int[] arr, int[] data){} //배열 arr을 배열 data에 있는 값들로 채워서 반환
int getRand(int from, int to){} //from과 to 범위의 정수(int)값을 반환. from과 to 모두 범위에 포함
```

- 데이터베이스에 넣을 더미 데이터 만들기

```java
import java.util.*;

class RandomEx{
  final static int RECORED_NUM = 10; //생성할 레코드의 수
  final static String TABLE_NAME = "TEST_TABLE";
  final static String[] CODE1 = {"010", "011", "017", "018", "019"};
  final static String[] CODE2 = {"남자", "여자"}; 
  final static String[] CODE3 = {"10대", "20대", "30대", "40대", "50대"}
  
  public static void main(String[] args){
    for(int i=0; i < RECORD_NUM; i++){
      System.out.println(" INSERT INTO " + TABLE_NAME
                         + " VALUES ("
                         + " '" + getRandArr(CODE1) + "'"
                         + ", '" + getRandArr(CODE2) + "'"	
                         + ", '" + getRandArr(CODE3) + "'"
                         + ", '" + getRand(100, 200) + "'" //100~200사이의 값 얻기
                         + "); "
                        );
    }
  }
  
  public static String getRandArr(String[] arr){
    return arr[getRand(arr.length-1)]; //배열에 저장된 값 중 하나를 반환
  }
  public static int getRand(int n) { return getRand(0, n);}
  public static int getRand(int from, int to){
    return (int)(Math.random()*(Math.abs(to-from)+1))+Math.min(from,to);
  }
}
```

