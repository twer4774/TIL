# 문제
~~~
행에서 가장 작은 숫자를 비교하여 가장 큰 숫자를 뽑는 게임  
  
입력  
3 3  
3 1 2  
4 1 4  
2 2 2  
  
출력  
2 => 1,2행에서 가장 작은 숫자는 1, 3행에서 가장 작은 숫자가 2 인데, 2가 가장 크므로 가장 큰 숫자인 2를 출력한다.  
  
  
입력2  
2 4  
7 3 1 8  
3 3 3 4  
  
출력2  
3 -> 1행에서 가장 작은 숫자 1, 2행에서 가장 작은 숫자 3 -> 3 출력  
~~~


# 풀이
``` python
  
# N, M 입력  
print('N, M을 공백으로 구분하여 입력받기')  
n, m = map(int, input().split())  
  
  
result = 0  
  
print('행렬 입력 받기')  
for i in range(n):  
    data = list(map(int, input().split()))  
  
    min_value = min(data)  
  
    # min_value와 result 중 더 큰 숫자 넣기  
    result = max(min_value, result)  
  
print(result)
```