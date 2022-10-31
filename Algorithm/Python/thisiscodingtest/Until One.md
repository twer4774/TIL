# 문제
~~~
1이 될때까지  
  
어떤 수 N, K가 주어졌을 때, N이 1이 되는 최소 횟수 구하기  
다음 두 가지 행동 중 선택적으로 반복하여 N을 1로 만든다.  
  
1. N에서 1 빼기  
2. N을 K로 나누기. 단, N이 K로 나누어 떨어지는 경우만 사용 가능  
  
입력  
17 4  
  
출력  
3 => 1번 한번, 2번 두번  
  
입력2  
25 5  
  
출력  
2 => 5로 두번 나눔
~~~

# 풀이
``` python
print("N, K 입력")  
n, k = map(int, input().split())  
  
count = 0  
  
while True:  
    # 2번 동작  
    if n % k == 0:  
        n = n/k  
    else:  
        n = n-1  
    count = count + 1  
  
    if n == 1:  
        break  
  
  
print(count)
```