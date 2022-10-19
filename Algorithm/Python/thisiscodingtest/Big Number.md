# 문제
~~~  
큰 수의 법치  
주어진 배열에서 M 번 더하여 가장 큰 숫자 만들기  
단, 동일한 배열의 인덱스는 K 번 만큼만 연속해서 더할 수 있다. 연속하지만 않으면 중복하여 사용할 수 있다.  
(다른 인덱스의 동일한 숫자는 다른 것으로 간주한다)  
ex) 2,4,5,4,6 M=8, K=3  
6 + 6 + 6+ 5 + 6 + 6 + 6 + 5 = 46  
  
ex2) 3,4,3,4,3 M=7, K=2  
4 + 4 + 4 + 4 + 4 + 4 + 4 = 28  
  
결과  
N, M, K를 공백으로 구분하여 입력받기  
5 8 3  
N개의 수를 공백으로 구분하여 입력받기  
2 4 5 4 6  
46    
~~~~  
# 코드
``` python
# N, M, K를 공백으로 구분하여 입력받기  
# N : 배열의 크기 / M : 숫자가 더해지는 횟수 / K : 반복 가능 횟수  
print("N, M, K를 공백으로 구분하여 입력받기")  
n, m, k = map(int, input().split())  
  
# N개의 수를 공백으로 구분하여 입력받기  
print("N개의 수를 공백으로 구분하여 입력받기")  
data = list(map(int, input().split()))  
  
# 가장 큰 수를 K번 만큼 반복해서 더하고 그 다음 큰 수를 한 번 더한 후 다시 K번 만큼 큰 수를 더한다.  
# 정렬  
data.sort()  
first = data[n-1]  
second = data[n-2]  
  
result = 0  
  
while True:  
    for i in range(k): # k만큼 반복  
        if m == 0:  
            break  
        result += first  
        m -= 1 # 더하기 동작 후 -1  
    if m == 0:  
        break  
    result += second  
    m -= 1  
  
  
print(result)
```
# 코드2 수열의 법칙 이용
``` python
# N, M, K를 공백으로 구분하여 입력받기  
print("N, M, K를 공백으로 구분하여 입력받기")  
n, m, k = map(int, input().split())  
  
  
# N개의 수를 공백으로 구분하여 입력받기  
print("N개의 수를 공백으로 구분하여 입력받기")  
data = list(map(int, input().split()))  
  
data.sort()  
first = data[len(data) -1]  
second = data[len(data) -2]  
  
"""  
{6, 6, 6, 5} 반복되는 수열 형태이다.  
총 수열의 길이는 (k+1)"""  
  
# 가장 큰 수가 더해지는 횟수  
count = int(m / (k+1)) * k #6  
count += m % (k+1) #0 # 나누어 떨어지지 않는 경우를 고려. 떨어지지 않는 만큼 큰 수를 더 더해주어야한다.  
  
result = 0  
result += (count) * first  
result += (m - count) * second  
print(result)
```