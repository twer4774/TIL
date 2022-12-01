문제
~~~
개미전사  
  
일직선상에 존재하는 식량창고를 서로 인접하지 않게 약탈한다.  
최대한 많은 식량을 약탈하는 프로그램 구하기  
  
입력 조건  
- 첫째 줄에 식량창고의 개수 N이 주어진다. (3 <= N <= 100)  
- 둘째 줄에 공백으로 구분되어 각 식량창고에 저장된 식량의 개수 K가 주어진다. (0 <= K <= 1,000)  
  
출력 조건  
- 첫째 줄에 개미 전사가 얻을 수 있는 식량의 최댓값을 출력하시오  
  
입력 예시  
4  
1 3 1 5  
  
출력 예시  
8
~~~

# 풀이
``` java
public class AntWarrior {  
  
    /*  
	    k = 현재 창고 식량    
	    ai-1 = 현재 창고의 옆 창고    
	    ai-2 = 현재 창고의 건너편  
	    현재 창고의 옆 창고만 터느냐, 옆옆과 현재 창고를 터느냐의 점화식    
	    ai = max(ai-1, ai-2 + k)    
	*/  
    public static void main(String[] args) {  
        int[] d = new int[30001];  
  
        Scanner sc = new Scanner(System.in);  
  
        int n = sc.nextInt();  
  
        int[] array = new int[n];  
        for (int i=0; i < n; i++){  
            array[i] = sc.nextInt();  
        }  
  
  
        d[0] = array[0];  
        d[1] = Math.max(array[0], array[1]);  
        for (int i = 2; i < n; i++) {  
            d[i] = Math.max(d[i-1], d[i-2]+array[i]);  
        }  
  
        System.out.println(d[n-1]);  
    }  
  
}
```