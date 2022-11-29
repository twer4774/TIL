# 문제
~~~
두 배열의 원소 교체  
두 배열 A, B는 N개의 원소로 구성되어 있으며 모두 자연소이다.  
최대 K번의 A와 B의 요소를 바꿀 때,  
A의 모든 원소의 합이 최대가 되도록 한다.  
  
입력 조건  
- 첫 번째 줄에 N, K가 공백으로 구분되어 입력된다. (1 <= N <= 100,000, 0 <= K <= N)  
- 두 번째 줄에 배열 A의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.  
- 세 번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.  
  
출력 조건  
- 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최대값 출력  
  
입력 예시  
5 3  
1 2 5 4 3  
5 5 6 6 5  
  
출력 예시  
26
~~~

# 풀이
``` java
public class ElementSwap {  
  
    public static void main(String[] args) throws IOException {  
        Scanner sc = new Scanner(System.in);  
  
        System.out.println("N, K 입력: ");  
        int n = sc.nextInt();  
        int k = sc.nextInt();  
  
        System.out.println("A, B 배열 입력");  
        Integer[] a = new Integer[n];  
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));  
        StringTokenizer st = new StringTokenizer(br.readLine());  
        for (int i = 0; i < n; i++) {  
            a[i] = Integer.parseInt(st.nextToken());  
        }  
  
        Integer[] b = new Integer[n];  
        StringTokenizer st2 = new StringTokenizer(br.readLine());  
        for (int i = 0; i < n; i++) {  
            b[i] = Integer.parseInt(st2.nextToken());  
        }  
  
        br.close();  
  
  
        Arrays.sort(a);  
        Arrays.sort(b, Collections.reverseOrder());  
  
        for (int i = 0; i < k; i++) {  
  
            // A의 원소가 B의 원소보다 작은 경우 원소 교체  
            if(a[i] < b[i]){  
                int temp = a[i];  
                a[i] = b[i];  
                b[i] = temp;  
            }  
            // A의 원소가 B의 원소보다 크거나 같을 경우 반복문 탈출  
            else break;  
  
            }  
  
        long result = 0;  
        for (int i= 0; i < n; i++) {  
            result += a[i];  
        }  
  
        System.out.println(result);  
    }  
}
```