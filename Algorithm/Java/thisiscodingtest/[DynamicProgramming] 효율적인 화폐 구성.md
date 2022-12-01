# 문제
~~~
효율적인 화폐 구성  
  
N가지 종류의 화폐의  합이 M이 되도록 하는 프로그램  
  
입력 조건  
- 첫째 줄에 N, M이 주어진다. (1 <= N <= 100, 1 <= M <= 10,000)  
- 이후 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐 가치는 10,000보다 작거나 같은 자연수이다.  
  
출력 조건  
- 첫째 줄에 M원을 만들기 위한 최소한의 화폐 개수를 출력한다.  
- 불가능할 할때는 -1을 출력한다.  
  
  
입력 예시1  
2 15  
2  
3  
  
출력 예시1  
5  
  
입력 예시2  
3 4  
3  
5  
7  
  
출력 예시2  
-1
~~~

# 풀이예시
~~~
a(i-k) = (i-k)를 만들수 있는 최소한의 화폐 개수를 의미  
- a(i-k)를 만드는 방법이 존재하는 경우, ai = min(ai, a(i-k)+1)  
- a(i-k)를 만드는 방법이 존재하지 않는 경우, ai = 10,001  
  
예 N=3, K=7인 경우 화폐 단위가 2,3,5가 주어졌을 때  
[step0] 초기화 : 0 인덱스를 제외한 배열의 값을 10001로 초기화 => 0원은 화폐가 없을 때 만들어지므로 0[step1] 2원으로 만들 수 있는 인덱스 만들기  
- 2원으로 2(1), 4(2), 6(3)을 만들 수 있다.  
[step2] 3원으로 만들 수 있는 인덱스 만들기  
- 3원으로 3(1), 6(2)를 만들 수 있다. 이때 6은 2개가 더 적으므로 2로 갱신한다.  
- 2,3으로 5(1,1=>2), 7(2,1=>3)을 만들 수 있다.  
=> a5=a2+1  
[step3] 5원으로 만들 수 있는 인덱스 만들기  
- 5(1) 갱신  
- 2,5로 7(1,1=>2)로 갱신  
=> a7=a2+1  
  
==> 답은 2
~~~

# 풀이
``` java
public class MoneyComposition {  
  
  
    public static void main(String[] args) {  
        Scanner sc = new Scanner(System.in);  
        int n = sc.nextInt();  
        int m = sc.nextInt();  
  
        // 화폐종류  
        int[] arr = new int[n];  
        for (int i = 0; i < n; i++) {  
            arr[i] = sc.nextInt();  
        }  
  
        // 맵 초기화  
        int[] d = new int[m+1];  
  
        for (int i = 0; i < m+1; i++) {  
            d[i] = 99999;  
        }  
        d[0] = 0;  
  
  
        for(int money: arr){  
            for (int i = money; i <= m; i++) {  
                d[i] = Math.min(d[i], d[i-money]+1);  
            }  
        }  
  
  
        if(d[m] == 99999){  
            System.out.println(-1);  
        } else {  
            System.out.println(d[m]);  
        }  
  
    }  
}
```