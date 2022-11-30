문제
```
부품찾기  
N개의 부품을 파는 매장에서 M개의 부품을 대량구매한다.  
M개의 부품이 모두 가게에 있는지 확인하는 프로그램 작성  
  
입력 조건  
- 첫째 줄에 정수 N이 주어진다.(1<=N<=1,000,000)  
- 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다.  
- 셋째 줄에는 정수 M이 주어진다.(1<=M<=100,000)  
- 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다.  
  
출력 조건  
- 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes, 없으면 no 출력  
  
입력 예시  
5  
8 3 7 9 2  
3  
5 7 9  
  
출력 예시  
no yes yes
```

# 풀이1. 이진탐색
``` java
public class FindParts {  
  
    public static void main(String[] args) {  
  
        Scanner sc = new Scanner(System.in);  
  
        System.out.println("n 입력");  
        int n = sc.nextInt();  
  
        Integer[] arrayN = new Integer[n];  
        for (int i = 0; i < n; i++) {  
            arrayN[i] = sc.nextInt();  
        }  
  
        System.out.println("m 입력");  
        int m = sc.nextInt();  
  
        Integer[] arrayM = new Integer[m];  
        for (int i = 0; i < m; i++) {  
            arrayM[i] = sc.nextInt();  
        }  
  
  
        // 정렬  
        Arrays.sort(arrayN);  
        Arrays.sort(arrayM);  
  
        // 이진탐색으로 풀기  
        StringBuilder sb = new StringBuilder();  
        for (int i = 0; i < m; i++) {  
            int target = arrayM[i];  
  
            if (binarySearch(arrayN, target, 0, n)) {  
                sb.append("yes ");  
            } else {  
                sb.append("no ");  
            }  
        }  
  
        System.out.println(sb.toString());  
    }  
  
    private static boolean binarySearch(Integer[] array, int target, int start, int end){  
  
        if(start > end){  
            return false;  
        }  
  
        int mid = (start + end) / 2;  
  
        if(array[mid] == target){  
            return true;  
        }  
        // 타겟이 중간 값 보다 작으면 왼쪽에서 검색  
        else if (array[mid] > target){  
            return binarySearch(array, target, start, mid-1);  
        }  
        // 타겟이 중간 값 보다 크면 오른쪽에서 검색  
        else{  
            return binarySearch(array, target, mid+1, end);  
        }  
    }  
}
```


# 풀이2. 계수정렬
``` java
public class FindParts {  
  
    public static void main(String[] args) {  
  
        Scanner sc = new Scanner(System.in);  
  
        System.out.println("n 입력");  
        int n = sc.nextInt();  
  
        Integer[] arrayN = new Integer[n];  
        for (int i = 0; i < n; i++) {  
            arrayN[i] = sc.nextInt();  
        }  
  
        System.out.println("m 입력");  
        int m = sc.nextInt();  
  
        Integer[] arrayM = new Integer[m];  
        for (int i = 0; i < m; i++) {  
            arrayM[i] = sc.nextInt();  
        }  
  
  
        // 정렬  
        Arrays.sort(arrayN);  
        Arrays.sort(arrayM);  
  
  
        // 계수정렬로 풀이        
        System.out.println(countSort(arrayN, arrayM));  
    }  
    
    // 계수정렬로 풀기  
    private static String countSort(Integer[] arrayN, Integer[] arrayM){  
        StringBuilder sb = new StringBuilder();  
  
        int maxNum = arrayN[arrayN.length-1];  
  
        int[] tempArray = new int[maxNum+1];  
  
        // 부품 가게에 부품 표시  
        for (int n : arrayN) {  
            tempArray[n] = 1;  
        }  
  
        // 구매자가 찾는 부품이 있는지 확인  
        for (int m : arrayM){  
            if(tempArray[m] == 1){  
                sb.append("yes ");  
            } else {  
                sb.append("no ");  
            }  
        }  
  
        return sb.toString();  
    }  
}
```