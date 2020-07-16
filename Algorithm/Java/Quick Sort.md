# Quick Sort(퀵정렬)

가장 빠른 알고리즘 중 하나로 널리 사용됨

### 배열을 두 그룹으로 나누기

- pivot - p / 왼쪽 끝의 요소 - pl / 오른쪽 끝의 요소 - pr

- 그룹을 나누려면 pl을 오른쪽으로, pr을 왼쪽으로 스캔해야 함

  1. arr[pl] >= x가 성립하는 요소를 찾을 때까지 pl을 오른쪽으로 스캔
  2. arr[pr] <= x가 성립하는 요소를 찾을 때까지 pr을 왼쪽으로 스캔

- 위의 조건을 충족하는 값들이 나타나면 두 값을 교환 후 다시 반복

- pl, pr이 서로 스캔하다가 p를 기준으로 서로 교차된다면 그룹을 나누는 과정이 종료됨

- 예

- | 0 (pl) | 1     | 2    | 3    | 4 (p) | 5     | 6     | 7    | 8 (pr) |
  | ------ | ----- | ---- | ---- | ----- | ----- | ----- | ---- | ------ |
  | 5      | 7     | 1    | 4    | 6     | 2     | 3     | 9    | 8      |
  | 5      | 7(pl) | 1    | 4    | 6     | 2     | 3(pr) | 9    | 8      |
  | 5      | **3** | 1    | 4    | 6     | 2     | **7** | 9    | 8      |
  | 5      | 3     | 1    | 4    | 6(pl) | 2(pr) | 7     | 9    | 8      |
  | 5      | 3     | 1    | 4    | **2** | **6** | 7     | 9    | 8      |

  6(p)를 기준으로 pl(2)과 pr(6)가 서로 교차되면 그룹을 나누는 과정이 종료됨

- 만일, pivot과 일치하는 값을 가지는 그룹이 만들어지는경우(pl과 pr이 스캔 조건을 충족하지 못하고 둘다 pivot에 있는 경우)

  - 동일한 요소를 교환하는 시도는 의미 없음 => 1회만 수행되므로 코드 수행시간에 영향이 없다. 
  - 만약 동일 요소를 교환하지 않고 매번 pl,pr의 위치가 같은지 검사하는 경우 시간이 오래 걸림

## 배열 나누기 실행

```java
import java.util.Scanner;

//배열을 나누는 예제


public class Partition {
    //배열요소 arr[idx1]과 arr[idx2]의 값을 바꿈
    static void swap(int[] arr, int idx1, int idx2){
        int temp = arr[idx1];
        arr[idx1] = arr[idx2];
        arr[idx2] = temp;
    }

    //배열을 나눔
    static void partion(int[] arr, int n){
        int pl = 0; //left cursor
        int pr = n - 1; //right cursor
        int x = arr[n / 2]; //pivot

        do{
            while(arr[pl] < x) pl++;
            while (arr[pr] > x) pr--;
            if( pl <= pr){
                swap(arr, pl++, pr--);
            }
        }while (pl <= pr);

        System.out.println("피벗의 값은 " + x );

        //------- 피벗 이하의 그룹
        System.out.println("피벗 이하의 그룹");
        for (int i = 0; i <= pl - 1; i++) {
            System.out.println(arr[i]);
        }

        //------- 피벗 일치하는 그룹
        if(pl > pr + 1){ 
            System.out.println("피벗과 일치하는 그룹");
            for (int i = pr + 1; i <= pl - 1; i++) { //arr[pr + 1] - arr[pl - 1]
                System.out.println(arr[i]);
            }
        }

        //------- 피벗 이상의 그룹
        System.out.println("피벗 이상의 그룹");
        for (int i = pr + 1; i < n; i++) {
            System.out.println(arr[i]);
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("배열을 나눕니다");
        System.out.println("요소수 : ");
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for (int i = 0; i < nx; i++) {
            System.out.println("x[" + i + "]: ");
            x[i] = stdIn.nextInt();
        }
        partion(x, nx);
    }//main
}
```



## 퀵 정렬

- Pivot을 기준으로 배열을 나누고 그 배열을 다시 pivot을 정하여 재나눔 함(재귀 이용)

- 요소의 개수가 1개인 그룹은 더이상 그룹을 나눌 피룡가 없으므로 요소의 개수가 2개 이상인 그룹만 나눔

  1. pr이 arr[0]보다 오른쪽에 있으면(left < pr) 왼쪽 그룹을 나눔
  2. pl이 arr[n-1]보다 왼쪽에 있으면(pl<right) 오른쪽 그룹을 나눔
  3. 가운데 그룹은 나눌 필요가 없어 분할 대상에서 제외

  위의 조건에 맞게 재귀 함수 구현(분할 정복)

```java
import java.util.Scanner;

//퀵 정렬

public class QuickSort {
    
    //배열 요소 arr[idx1] 과 arr[idx2]의 값을 바꿈
    static void swap(int[] arr, int idx1, int idx2) {
        int temp = arr[idx1];
        arr[idx1] = arr[idx2];
        arr[idx2] = temp;
    }
    
    //퀵 정렬
    static void quickSort(int[] arr, int left, int right) {
        //그룹을 재 분할하여 pivot을 기준으로 왼쪽에 있는 그룹과 오른쪽의 그룹을 조건에 맞게 정렬함
        int pl = left;
        int pr = right;
        int x = arr[((pl + pr) / 2)]; //pivot
        
        //퀵 정렬의 배열을 나누는 과정 출력
        System.out.printf("arr[%d]~arr[%d] : {", left, right);
        for (int i = left; i < right; i++) {
            System.out.printf("%d , ", arr[i]);
        }

        System.out.printf("%d}\n", arr[right]);
        
        do{
            while (arr[pl] < x) pl++;
            while (arr[pr] < x) pr--;
            if (pl <= pr) {
                swap(arr, pl++ , pr--);
            }
            
        } while ( pl < pr);
        
        //left가 pr보다 크면, 퀵정렬에 right는 pr 값이 됨
        if (left < pr) quickSort(arr, left, pr);
        //pl이 right보다 작으면, 퀵정렬에 left값은 pl이 됨
        if (pl < right) quickSort(arr, pl, right);
    }
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);

        System.out.println("퀵 정렬 요소수 : ");
        int nx = stdin.nextInt();
        int[] x = new int[nx];

        for (int i = 0; i < nx; i++) {
            System.out.println("x[" + i + "] :");
            x[i] = stdin.nextInt();
        }
        
        quickSort(x, 0, nx - 1);

        System.out.println("오름차순으로 정렬");
        for (int i = 0; i < nx; i++) {
            System.out.println("x[" + i + "]=" + x[i]);
        }
    }//main
}
```



## Pivot 선택하기

- Pivot의 선택방법은 실행 효율에 큰 영향
- 간단한 아이디어 - 첫요소, 가운데요소, 끝요소를 정렬 후 가운데 요소를 피벗값으로 정함
- 효율적인 아이디어
  1. 첫요소, 가운데요소, 끝요소를 정렬한다 
  2. 위의 정렬에서 구한 중간값과, 배열의 끝요소에서 두번째 값(n - 2)을 교환
  3. 끝에서 두번째 요소 값을 Pivot으로 정함
  4. arr[left]는 피벗 이하의 값이고, arr[right - 1]과 arr[right]는 피벗 이상의 값
- 이 방법은 나눌 그릅의 크기가 한쪽으로 치우치는 것을 피하면서도 나눌때 스캔 요소를 3개씩 줄일 수 있는 장점을 가짐

```java
package chap06;
import java.util.Scanner;
// 퀵정렬(머리/중앙/꼬리요소를 정렬하여 중앙값을 피벗으로 합니다. : 재귀버전)

class QuickSort {
	// 배열의 요소 a[idx1]과 a[idx2]를 교환
	static void swap(int[] a, int idx1, int idx2) {
		int t = a[idx1];
		a[idx1] = a[idx2];
		a[idx2] = t;
	}

	// x[a], x[b], x[c]를 sort (중앙값의 index를 반환)
	static int sort3Elem(int[] x, int a, int b, int c) {
		if (x[b] < x[a])
			swap(x, b, a);
		if (x[c] < x[b])
			swap(x, c, b);
		if (x[b] < x[a])
			swap(x, b, a);
		return b;
	}

	// 단순삽입정렬
	static void insertionSort(int[] a, int left, int right) {
		for (int i = left + 1; i <= right; i++) {
			int tmp = a[i];
			int j;
			for (j = i; j > left && a[j - 1] > tmp; j--)
				a[j] = a[j - 1];
			a[j] = tmp;
		}
	}

	// 배열을 나눔
	static void quickSort(int[] a, int left, int right) {
		if (right - left < 9)
			insertionSort(a, left, right);
		else {
			int pl = left; // 왼쪽 커서
			int pr = right; // 오른쪽 커서
			int x; // 피벗
			int m = sort3Elem(a, pl, (pl + pr) / 2, pr);
			x = a[m];
			swap(a, m, right - 1);
			pl++;
			pr--;

			do {
				while (a[pl] < x)
					pl++;
				while (a[pr] > x)
					pr--;
				if (pl <= pr)
					swap(a, pl++, pr--);
			} while (pl <= pr);
			if (pr - left < right - pl) {
				int temp;
				temp = left;
				left = pl;
				pl = temp;
				temp = right;
				right = pr;
				pr = temp;
			}
			if (left < pr)
				quickSort(a, left, pr);
			if (pl < right)
				quickSort(a, pl, right);
		}
	}

	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);

		System.out.println("퀵정렬 ");
		System.out.print("요솟수：");
		int nx = stdIn.nextInt();
		int[] x = new int[nx];

		for (int i = 0; i < nx; i++) {
			System.out.print("x[" + i + "]：");
			x[i] = stdIn.nextInt();
		}

		quickSort(x, 0, nx - 1); // 배열 x를 퀵정렬

		System.out.println("오름차순으로 정렬했습니다.");
		for (int i = 0; i < nx; i++)
			System.out.println("x[" + i + "]＝" + x[i]);
	}
}
```

- 시간 복잡도는 O(n log n) 이며, 최악의 시간복잡도는 O(n^2)