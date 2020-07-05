# Class

- 임의의 데이터형을 자유로이 조합하여 만들 수 있는 자료구조

- ```java
  class XYZ{
    int x;
    long y;
    double z;
  }
  
  XYZ a; //XYZ형의 클래스 형 변수 a 선언
  a = new XYZ(); //XYZ형의 클래스 인스턴스(실체)를 생성
  
  XYZ a = new XYZ(); //위의 명령 두개를 한번에 함
  ```

- 클래스의 종류

  - 공개클래스 : public을 붙여 선언한 클래스로 다른 패키지에서 사용할 수 있는 공개 클래스
  - final클래스 : 접근 제한자 final을 붙여 선언한 클래스로, 서브 클래스를 가질 수 없음
  - 서브클래스 : extends A를 이용하여 A 클래스를 상속한 클래스
  - 인터페이스 구현 : implements 명령어 사용
  - 추상클래스 : abstract를 붙임. 불완전 클래스이므로 인스턴스를 만들 수 없음. 실체가 없는 클래스 - 실체는 서브클래스에서 정의
  - 중첩 클래스 : 클래스 또는 인터페이스 안에 선언한 클래스는 중첩 클래스가 됨

- 신체검사 데이터

```java
package chap02;

import java.util.Scanner;

//신체검사 데이터용 클래스 배열에서 평균 키와 시력의 분포를 구함

public class PysicalExamination {

    static final int VMAX = 21; //시력 분포 90.0에서 0.1 단위로 21개)

    static class PhyscData{
        String name;
        int height;
        double vision; //시력

        //생성자
        PhyscData(String name, int height, double vision){
            this.name = name;
            this.height = height;
            this.vision = vision;
        }
    }

    //키의 평균값을 구함
    static double aveHeight(PhyscData[] dat){
        double sum = 0;

        for(int i = 0; i < dat.length; i++){
            sum += dat[i].height;
        }

        return sum / dat.length;
    }

    //시력 분포를 구함
    static void distVision(PhyscData[] dat, int[] dist){
        int i = 0;

        dist[i] = 0;
        for(i = 0; i < dat.length; i++){
            if(dat[i].vision >= 0.0 && dat[i].vision <= VMAX / 10.0)
                dist[(int)(dat[i].vision * 10)]++;
        }
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        PhyscData[] x = {
                new PhyscData("박현규" , 162, 0.3),
                new PhyscData("함진아" , 174, 0.8),
                new PhyscData("최윤미" , 172, 0.2),
                new PhyscData("홍현의" , 162, 0.3),
                new PhyscData("이수진" , 171, 1.3),
                new PhyscData("김영준" , 172, 0.7),
                new PhyscData("박용규" , 169, 0.8),
        };
        int[] vdist = new int[VMAX]; //시력 분포

        System.out.println("신체검사 리스트");
        System.out.println("이름       키   시력");
        System.out.println("---------------------");
        for(int i = 0; i < x.length; i++){
            System.out.printf("%-8s%3d%5.1f\n", x[i].name, x[i].height, x[i].vision);
        }

        System.out.printf("\n평균 키: %5.1fcm\n", aveHeight(x));

        distVision(x, vdist);

        System.out.println("\n시력분포");
        for(int i = 0; i < VMAX; i++){
            System.out.printf("%3.1f~: %2d명\n", i / 10.0, vdist[i]);
        }

    }//main
}
```

```
//결과
신체검사 리스트
이름      키   시력
---------------------
박현규     162  0.3
함진아     174  0.8
최윤미     172  0.2
홍현의     162  0.3
이수진     171  1.3
김영준     172  0.7
박용규     169  0.8

평균 키: 168.9cm

시력분포
0.0~:  0명
0.1~:  0명
0.2~:  1명
0.3~:  2명
0.4~:  0명
0.5~:  0명
0.6~:  0명
0.7~:  1명
0.8~:  2명
0.9~:  0명
1.0~:  0명
1.1~:  0명
1.2~:  0명
1.3~:  1명
1.4~:  0명
1.5~:  0명
1.6~:  0명
1.7~:  0명
1.8~:  0명
1.9~:  0명
2.0~:  0명
```

