## 문제
~~~
떡볶이 떡 만들기  
절단기에 높이 H를 지정하면 줄지어진 떡을 한 번에 절단한다.  
H보다 긴 떡은 H만큼 잘린다.  
손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓 값을 구하는 프로그램 구하기  
  
입력 조건  
- 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다. (1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000)  
- 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M이므로 손님은 필요한 양만큼 떡을 사갈 수 있다.  
  
출력 조건  
- 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최대값을 출력한다.  
  
입력 예시  
4 6  
19 15 10 17  
  
출력 예시  
15
~~~

# 풀이
``` java
public class MakeRiceCake {  
  
    public static void main(String[] args) {  
        Scanner sc = new Scanner(System.in);  
  
        System.out.println("n, m 입력: ");  
        int n = sc.nextInt();  
        int m = sc.nextInt();  
  
        Integer[] arr = new Integer[n];  
  
        for (int i = 0; i < n; i++) {  
            arr[i] = sc.nextInt();  
        }  
  
        // 정렬  
        Arrays.sort(arr);  
  
        System.out.println(binary(arr, m, 0, arr[arr.length-1]));  
    }  
  
    private static int binary(Integer[] arr, int m, int start, int end){  
        int result = 0;  
  
        while(start <= end) {  
  
            int mid = (start + end) / 2;  
  
            int total = 0;  
  
            // 떡 길이의 합 구하기  
            for(int i : arr){  
                if(i > mid){  
                    total += (i - mid);  
                }  
            }  
  
            // 크기가 작으면 덜 잘라서 크기를 맞춘다. -> 왼쪽 부분 탐색  
            if(total < m){  
                end = mid-1;  
            }  
            // 크기가 m보다 크면 더 잘라야 한다. -> 오른쪽 부분 탐색  
            else{  
                result = mid; // 일단 크기는 저장해놓는다.  
                start = mid+1;  
            }  
  
        }  
        return result;  
    }  
}
```