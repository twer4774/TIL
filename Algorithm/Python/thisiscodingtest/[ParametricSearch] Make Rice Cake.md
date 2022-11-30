# 문제
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

# 풀이1. 순차탐색
- 만약 떡의 길이가 매우 긴 떡이 덩그러니 있다면 순차 탐색은 시간이 오래걸릴 수 있다.
	- 이진 탐색을 이용해 푼다.
``` python
def search(arr, m):  
    # 가장 길이가 긴 떡을 기준으로 삼는다.  
    h = arr[len(arr)-1]  
  
    while True:  
        if h <= 0:  
            break  
  
        result = 0  
        for i in range(len(arr)):  
            # 떡의 길이가 h보다 크면 떡을 자른다.  
            if arr[i] > h:  
                result += arr[i] - h  
  
        # 요청한 길의 떡을 만족하면 높이를 반환한다.  
        if result >= m:  
            return h  
  
        else:  
            h -= 1  
  
  
print('N, M 입력')  
n, m = map(int, input().split())  
  
print('떡 길이 리스트 입력')  
arr = list(map(int, input().split()))  
  
arr.sort()  
  
print(search(arr, m))
```

# 풀이 2.  파라메트릭 서치
- ParametricSearch : 최적화 문제를 결정문제(예 or 아니오)로 변경하여 문제를 해결한다.
- 이진탐색을 이용한다.
``` python
def binary(arr, m, start, end):  
    result = 0  
    while(start <= end):  
        total = 0  
        mid = (start + end) // 2  
  
        for x in arr:  
            # 잘랐을 때의 떡의 양 계산  
            if x > mid:  
                total += x - mid  
  
        # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)  
        if total < m:  
            end = mid -1  
  
        # 떡의 양이 충분 한 경우 덜 자르기 (오른쪽 부분 탐색)  
        else:  
            result = mid  
            start = mid + 1  
  
    return result

print('N, M 입력')  
n, m = map(int, input().split())  
  
print('떡 길이 리스트 입력')  
arr = list(map(int, input().split()))  
  
arr.sort()  
  
print(binary(arr, m, 0, max(arr)))
```