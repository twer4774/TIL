# Set(집합)

명확한 조건을 만족하는 자료의 모임

- 중복된 값을 허용하지 않음
- 순서가 없음

### 부분집합과 진부분집합

- A = {1, 3} B = {1, 3, 5}
  - A는 B의 부분집합이며, 진부분집합
    - 부분집합 : A의 모든 요소가 B의 요소
    - 진부분집합 : A는 B에 부분집합 관계이지만, A와 B는 동일하지 않다
- A = {1, 3} B = {1, 3, 5}
  - A는 B의 부분집합이며, 진부분집합이 아니다
- A = {1, 3, 5} B= {1, 3, 5}
  - A와 B는 서로 부분집합

### 집합의 연산

- 합집합 : A와 B 두 집합을 합친 것 = 적어도 한쪽에 속하는 요소의 집합
- 교집합 : A와 B 두 집합 모두 가지고 있는 요소
- 차집합 : A - B => A의 요소에서 B의 요소들을 뺀 집합



### 배열로 집합 만들기

- 모든 요소가 같은 자료형으로 구성된 집합은 배열로 표현 가능
- 배열로 집합을 표현하려면, '집합의 요소 개수 = 배열의 요소 개수' 여야 한다.

```java
//int형 집합

public class IntSet {
    private int max;
    private int num;
    private int[] set;

    //생성자 - 집합 배열을 생성하는 역할 수행
    public IntSet(int capacity) {
        num = 0;
        max = capacity;
        try {
            set = new int[max]; //집합 배열 생성
        } catch (OutOfMemoryError e) { //배열 생성 실패
            max = 0;
        }
    }

    //집합의 최대 개수
    public int capacity() {
        return max;
    }

    //집합의 요소 개수
    public int size() {
        return num;
    }

    //집합에서 n을 검색
    public int indexOf(int n) {
        for (int i = 0; i < num; i++) {
            if (set[i] == n) {
                return i; // 검색 성공
            }
        }
        return -1;  //검색 실패
    }

    //집합에 n이 있는지 확인 - -1이 검색실패이므로, -1이 아니면 true(성공)
    public boolean contains(int n) {
        return (indexOf(n) != -1) ? true : false;
    }

    //집합에 n을 추가
    public boolean add(int n) {
        if (num >= max || contains(n) == true) { //가득 찼거나 이미 n이 존재
            return false;
        } else { //가장 마지막 자리에 추가
            set[num++] = n;
        }
        return true;
    }

    //집합에서 n을 삭제
    public boolean remove(int n) {
        int idx; //n이 저장된 요소의 인덱스

        if (num <= 0 || (idx = indexOf(n)) == -1) { //비어 있거나 n이 존재하지 않음
            return false;
        } else {
            set[idx] = set[--num]; //마지막 요소를 삭제한 곳으로 옮김
            return true;
        }
    }

    //집합 s에 복사
    public void copyTo(IntSet s) {
        int n = (s.max < num) ? s.max : num; //복사할 요소 개수
        for (int i = 0; i < n; i++) {
            s.set[i] = set[i];
        }
        s.num = n;
    }

    //집합 s를 복사
    public void copyFrom(IntSet s) {
        int n = (max < s.num) ? max : s.num; //복사할 요소 개수
        for (int i = 0; i < n; i++) {
            set[i] = s.set[i];
        }
        num = n;
    }

    //집합 s와 같은지 확인
    public boolean equalTo(IntSet s) {
        if (num != s.num){ //요소의 개수가 같지 않으면
            return false; //집합은 같지 않음
        }

        for (int i = 0; i < num; i++) {
            int j = 0;

            for (; j < s.num; j++) {
                if (set[i] == s.set[j]) {
                    break;
                }
            }

            if (j == s.num) { //set[j]는 s에 포함되지 않음
                return false;
            }
        }

        return true;
    }

    //합집합 복사
    public void unionOf(IntSet s1, IntSet s2) {
        copyFrom(s1); //집합 s1을 복사
        for (int i = 0; i < s2.num; i++) {
            add(s2.set[i]); //집합 s2의 요소를 추가
        }
    }

    //"{a b c}" 형식의 문자열로 표현
    public String toString() {
        StringBuffer temp = new StringBuffer("{ ");
        for (int i = 0; i < num; i++) {
            temp.append(set[i] + " ");
        }
        temp.append("}");
        return temp.toString();
    }
    public static void main(String[] args) {

    }//main
}
```

