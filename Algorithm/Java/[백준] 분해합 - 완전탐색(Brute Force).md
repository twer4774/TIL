## 문제

어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.
자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

## 입력
첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

## 출력
첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.

### 입력 예
216
### 출력 예
198

# 풀이
- 완전탐색 이용
- 생성자 중에 가장 작은 값 찾기
``` java
import java.io.*;  
  
public class Decomposition {  
  
    public static void main(String[] args) throws IOException{  
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));  
  
        // 생성자  
        int N = Integer.parseInt(br.readLine());  
  
        System.out.println(operation(N));  
    }  
  
    private static int operation(int N){  
        int answer = 0;  
  
        // N까지의 숫자 중 분해합이 되는 가장 작은 자연수 찾기. 없으면 0 반환  
        for (int i = 0; i < N; i++) {  
            int number = i;  
            int sumNumber = 0;  
            while(number != 0) {  
                sumNumber = sumNumber + (number % 10);  
                number = number / 10;  
            }  
  
            // 분해합인 경우 answer로 변경  
            if( (i + sumNumber) == N){  
                answer = i;  
                break; // 가장 작은 수를 찾아야하므로 for문을 벗어난다.  
            }  
        }  
  
        return answer;  
    }  
  
}
```