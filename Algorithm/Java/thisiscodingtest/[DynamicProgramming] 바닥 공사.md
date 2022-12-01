# 문제
문제
~~~
바닥 공사  
  
N * 2 인 바닥을 1 * 2, 2 * 1, 2 * 2 덮개로 채우고자 한다.  
바닥을 채우는 모든 경우의 수를 구하는 프로그램 작성  
  
입력 조건  
- 첫째 줄에 N이 주어진다. (1 <= N <= 1,000)  
  
출력 조건  
- 첫째 줄에 2 * N 크기의 바닥을 채우는 방법의 수를 795,796으로 나눈 나머지를 출력한다.  
  
입력 예시  
3  
  
출력 예시  
5
~~~

# 풀이
``` java
public class FloorWork {  
  
    /*  
    점화식    
    ai = ai-1 + ai-2 *2     
    */  
    public static void main(String[] args) {  
        Scanner sc = new Scanner(System.in);  
  
        int n = sc.nextInt();  
  
        int[] d = new int[1001];  
  
        d[1] = 1; // 한 가지 경우  
        d[2] = 3; // 세 가지 경우 (1*2)*2 , (2*1)*2, (2*2)  
  
        for(int i=3; i <= n; i++){  
            d[i] = (d[i-1] + 2*d[i-2]) % 796796;  
        }  
  
        System.out.println(d[n]);  
    }  
}
```