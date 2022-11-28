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
``` python
print("N 입력")  
n = int(input())  
  
print("이름 성적 입력")  
grades = []  
for i in range(n):  
    inputs = input().split()  
    grades.append( (inputs[0], int(inputs[1])) )  
  
# key를 이용하여 점수를 기준으로 정렬  
grades = sorted(grades, key=lambda student: student[1])  
  
for s in grades:  
    print(s[0], end=' ')
```