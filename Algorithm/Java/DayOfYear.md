# DayOfYear 

- 그 해에서 몇일째인지 계산
- 윤년을 포함하여 계산됨

```java
package chap02;
import java.util.Scanner;

//그 해 경과 일 수를 구함 (윤년도 포함되어 계산) - 그 년도에 몇일짜인지 계산

public class DayOfYear {

    //각 달의 일 수
    static int[][] mdays = {
            {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}, //평년
            {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31} //윤년
    };

    //서기 year는 윤년인가? (윤년: 1/ 평년: 0) 윤년은 4로 나누어떨어면서 100으로 나누어 떨어지지 않거나 400으로 나누어떨어지는 년도
    static int isLeap(int year){
        return (year % 4 == 0 && year % 100 != 0 || year % 400 == 0) ? 1 : 0;
    }

    //서기 y년 m월 d일의 그 해 경과 일 수를 구함
    static int dayOfYear(int y, int m, int d){
        int days = d;

        for (int i = 1; i < m; i++){ //1월~(m-1)월의 일 수를 더함
            days += mdays[isLeap(y)][i - 1]; //y는 윤년이면 1, 평년이면 0 위에 mdays의 배열
        }
        return days;
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int retry;

        System.out.println("그 해 경과 일수를 구합니다.");

        do{
            System.out.println("년 :"); int year = stdIn.nextInt();
            System.out.println("월 :"); int month = stdIn.nextInt();
            System.out.println("일 :"); int day = stdIn.nextInt();

            System.out.printf("그 해 %d일째입니다.\n", dayOfYear(year, month, day));

            System.out.println("한번 더 할까요? (1.예/0.아니오)");
            retry = stdIn.nextInt();

        } while(retry == 1);
    }//main
}

```

```
//결과
년 :
2004
월 :
10
일 :
3
그 해 277일째입니다.
```

- 입력한 년도에서 남은 날을 계산

```java
import java.util.Scanner;
// 연내의 남은 일 수를 구합니다.

class LeftDayOfYear_02_09 {
	// 각 달의 일 수
	static int[][] mdays = { { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 }, // 평년
			{ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 }, // 윤년
	};

	// 서기 year년은 윤년인가? (윤년：1／평년：0)
	static int isLeap(int year) {
		return (year % 4 == 0 && year % 100 != 0 || year % 400 == 0) ? 1 : 0;
	}

	// 서기 y년 m월 d일의 연내의 남은 일 수를 구합니다.
	static int leftDayOfYear(int y, int m, int d) {
		int days = d; // 일수

		for (int i = 1; i < m; i++) // 1월~(m-1)월의 일 수를 더함
			days += mdays[isLeap(y)][i - 1];
		return 365 + isLeap(y) - days;
	}

	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		int retry; // 한 번 더？

		System.out.println("연내의 남은 일 수를 구합니다.");

		do {
			System.out.print("년：");
			int year = stdIn.nextInt(); // 년
			System.out.print("월：");
			int month = stdIn.nextInt(); // 월
			System.out.print("일：");
			int day = stdIn.nextInt(); // 일

			System.out.printf("연내의 남은 일 수는 %d일입니다.\n", leftDayOfYear(year, month, day));

			System.out.print("한번 더 할까요? (1.예/0.아니오)：");
			retry = stdIn.nextInt();
		} while (retry == 1);
	}
}
```

