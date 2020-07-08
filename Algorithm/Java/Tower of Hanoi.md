# Tower of Hanoi(하노이의 탑)

작은 원반이 위에, 큰 원반이 아래에 위치할 수 있도록 원반을 3개의 기둥 사이에서 옮기는 문제

- 모든 원반을 세 번째 기둥으로 최소의 횟수로 옮기면 됨
- 원반은 1개씩만 옮길 수 있고. 큰 원반을 작은 원반 위에 쌓을 수는 없

### 구현

- move 메서드의 매개변수는 no는 옮겨야 할 원반의 개수

  - 1. 바닥 원반을 제외한 그룹(원반[1] ~ 원반[no-1])을 시작 기둥에서 중간기둥으로 옮김
    2. 바닥 원반 no를 시작 기둥에서 목표 기둥으로 옮겼음을 출력
    3. 바닥 원반을 제외한 그룹(원반1] ~ 원반[no-1])을 중간 기둥에서 목표 기둥으로 옮김

    -> 1,3은 재귀호출에 의해 해결

- x는 시작 기둥, y는 목표 기둥

```java
import java.util.Scanner;

//하노이의 탑
// 기둥의 번호를 정수 1, 2, 3으로 나타내어 기둥의 합이 6이므로 기둥이 시작,목표 기둥 어느 것이더라도 중간 기둥은 6 - x - y로 구할 수 있음
public class Hanoi {
    //no개의 원반을 x -> y 옮김
    static void move(int no, int x, int y){
        if (no > 1){
            move(no - 1, x, 6 - x - y);
        }

        System.out.println("원반[" + no + "]을" + x + "기둥에서 " + y + "기둥으로 옮김");

        if (no > 1)
            move(no - 1, 6 - x - y, y);
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("하노이의 탑 원반의 개수 : ");
        int n = stdIn.nextInt();

        move(n, 1, 3);

    }//main
}
```

