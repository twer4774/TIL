# 8-Queen problem(8퀸 문제)

재귀 알고리즘을 설명할 때 자주 나오는 문제이며, 가우스가 틀린 해답을 내놓아서 유명해짐

> 서로 공격하여 잡을 수 없도록 8개의 퀸을 8 * 8 체스판에 놓으세요
>
> 단, 퀸은 서 있는 지점에서 체스판의 어떤 지점으로든 여덟 방향으로 직선 이동이 가능합니다.

## 풀이 

분할 정복법(divide and conquer)을 이용한다. 문제를 세분화하고 작은 문제의 풀이를 결합 해 전체 문제를 풀이함

### 퀸 배치하기

##### 8개의 퀸을 배치하는 조합은 

64 * 63 * 62 * … * 57 = 178,462,987,637,760

##### 규칙 1 : 각 열에는 퀸을 1개만 배치한다.

8 * 8 * 8 * 8 * 8 * 8 * 8 * 8  = 16,777,216

##### 규칙 2 : 각 행에는 퀸을 1개만 배치한다.

##### 규칙 3 : 대각선에는 퀸을 1개만 배치한다.

### 가지 뻗기 - 8개의 퀸을 배치하는 조합(실행시간 오래걸림 - 모든 경우의 수 출력)

- 배열 pos는 퀸의 배치를 나타내며, i열에 놓인 퀸의 위치가 j행이면 pos[i]=j로 한다.

- set메서드를 정의
  - pos[i]에 0부터 7까지의 값을 순서대로 대입해 'i열에 퀸을 1개만 배치하는 8가지 조합을 만드는 재귀 메서드'

```java
//가지 뻗기 - 각 열에 1개의 퀸을 배치하는 조합을 재귀적으로 나열

public class QueenB {
    
    static int[] pos = new int[8]; //각 열의 퀸의 위치
    
    //각 열의 퀸의 위치를 출력
    static void print() {
        for (int i = 0; i < 8; i++){
            System.out.printf("%2d", pos[i]);
        }
        System.out.println();
    }
    
    //i열에 퀸을 놓음. 재귀함수 set구현
    static void set(int i){
        for (int j = 0; j < 8; j++){
            pos[i] = j; //퀸을 j행에 배치
            if(i==7){ //모든 열에 배치
                print();
            }else {
                set(i + 1); //다음 열에 퀸을 배치
            }
        }
    }
    public static void main(String[] args) {
        set(0); //0열에 퀸을 배치
    }//main
}
```

```
00000000
00000001
...
77777777
```

- 퀸의 모든 조합을 나타냄

### 분기 한정법

- 규칙2 각행에 퀸을 1개만 배치한다 적용

```java
//각 행, 열에 1개의 퀸을 배치하는 조합을 재귀적으로 나열

public class QueenBB {
    
    static boolean[] flag = new boolean[8]; //각 행에 퀸을 배치했는지 체크
    static int[] pos = new int[8]; //각 열의 퀸의 위치
    
    //각 열의 퀸의 위치를 출력
    static void print() {
        for (int i = 0; i < 8; i++){
            System.out.printf("%2d", pos[i]);
        }
        System.out.println();
    }
    
    //i열의 알맞은 위치에 퀸을 배치
    static void set(int i) {
        for (int j = 0; j < 8; j++) {
            if(flag[j] == false) { //j행에 퀸을 배치 하지 않았다면
                pos[i] = j; //퀸을 j행에 배치
                if( i == 7){ //모든 열에 배치한 경우
                    print();
                } else {
                    flag[j] = true;
                    set(i + 1);
                    flag[j] = false;
                }
            }
        }
    }
    public static void main(String[] args) {

    }//main
}
```

- flag라는 배열을 이용하여 같은 행에 중복하여 퀸이 배치되는 것을 방지
- j행에 퀸을 배치하면 flag[j] 값을 true로 하고, 배치되지 않은 상태의 값은 false로 함
- set 메서드를 재귀적으로 호출하면서 모든 배치를 마친다. 262,144개의 조합이 생략됨

### 8퀸 문제 풀이 구현(정답의 조합은 총 92가지)

```java
//8퀸 문제 풀이

public class EightQueen {
    static boolean[] flag_a = new boolean[8]; //각 행에 퀸을 배치했는지 체크
    static boolean[] flag_b = new boolean[15]; // / 방향에 퀸을 배치했는지 체크
    static boolean[] flag_c = new boolean[15]; // \ 방향에 퀸을 배치했는지 체크
    static int[] pos = new int[8]; //각 열의 퀸의 위치
    
    //각 열의 퀸의 위치 출력
    static void print(){
        for (int i = 0; i < 8; i++){
            System.out.printf("%2d", pos[i]);
        }
        System.out.println();
    }
    
    //i열의 알맞은 위치에 퀸을 배치
    static void set(int i){
        for (int j = 0; j < 8; j++){
            if(flag_a[j] == false &&                //가로(j)행에 아직 배치하지 않음
                    flag_b[i + j] == false &&       //대각선 /에 아직 배치하지 않음
                    flag_c[i -j + 7] == false){     //대각선 \에 아직 배치하지 않음
                pos[i] = j;                         //퀸을 j행에 배치
                if ( i == 7 ){                      //모든 열에 배치했다면
                    print();                        //위치 출력
                } else {
                    flag_a[j] = flag_b[i+j] = flag_c[i - j + 7] = true;
                    set(i + 1);
                    flag_a[j] = flag_b[i+j] = flag_c[i - j + 7] = false;
                }
            }
        }
    }
    public static void main(String[] args) {
        set(0); //0열부터 배치가 시작됨
    }//main
}
```

