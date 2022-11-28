# 문제
~~~
성적이 낮은 순서로 학생 출력하기  
N명의 학생의 이름과 성적이 주졌을 때 성적이 낮은 순으로 이름 출력  
  
입력 조건  
- 첫 번째 줄에 학생의 수 N이 입력된다 (1 <= N <= 100,000)- 두 번째 줄부터 N+1번째 줄에는 학생의 이름을 나타내는 문자열 A와 성적을 나타내는 B가 공백으로 구분되어 입력된다.  
- 문자열 A의 길이와 학생의 성적은 100이하의 자연수이다.  
  
출력 조건  
- 모든 학생의 이름을 성적이 낮은 순서대로 출력  
  
입력예시  
2  
홍길동 95이순신 77  
출력 예시  
이순신 홍길동
~~~

# 풀이
``` java
public class Grade {  
  
    public static void main(String[] args) {  
  
        System.out.println("학생 수 입력: ");  
        Scanner sc = new Scanner(System.in);  
  
        int n = sc.nextInt();  
  
  
        List<Student> studentList = new ArrayList<>();  
  
        for (int i = 0; i < n; i++) {  
  
            System.out.println("이름 성적 입력: ");  
            String name = sc.next();  
            int grade = sc.nextInt();  
  
            studentList.add(new Student(name, grade));  
  
        }  
  
        Collections.sort(studentList);  
  
        for (int i = 0; i < studentList.size(); i++) {  
            System.out.print(studentList.get(i).getName());  
        }  
    }  
}  
  
class Student implements Comparable<Student> {  
  
    String name;  
    int grade;  
  
    public Student(String name, int grade) {  
        this.name = name;  
        this.grade = grade;  
    }  
  
    public String getName() {  
        return name;  
    }  
  
    // 정렬 기준은 '점수가 낮은 순서'  
    @Override  
    public int compareTo(Student o) {  
        if(this.grade < o.grade){  
            return -1;  
        }  
  
         return 1;  
    }  
}
```