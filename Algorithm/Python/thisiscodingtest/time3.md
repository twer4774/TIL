# 문제
~~~
[완전탐색] 시각  
정수 N이 입력되면 00시 00분 00초 ~ N시 59분 59초의 시각 중 3이 하나라도 포함된 모든 경우의 수를 출력하시오  
  
입력  
5  
  
출력  
11475
~~~

# 풀이
``` python

print("N 입력")  
n = int(input())  
  
# 모든 경우의 수  
result = 0  
  
for i in range(n+1):  
    for j in range(60):  
        for k in range(60):  
  
            # 문자열에 3이 포함되면 카운트 증가  
            if '3' in str(i) + str(j) + str(k):  
                result = result + 1  
  
print(result)
```