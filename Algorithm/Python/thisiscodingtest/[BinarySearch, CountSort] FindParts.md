# 문제
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
``` python
def binary_search(array, target, start, end):  
    if start > end:  
        return 'no'  
  
    mid = (end + start) // 2  
  
    if array[mid] == target:  
        return 'yes'  
    # 타겟 값이 중간 값 보다 작으면 왼쪽에서 탐색  
    elif array[mid] > target:  
        return binary_search(array, target, start, mid-1)  
    # 타겟 값이 중간 값 보다 크면 오른쪽에서 탐색  
    else:  
        return binary_search(array, target, mid+1 , end)  
  
  
print("N 입력")  
n = int(input())  
print("N의 배열 입력")  
array_n = list(map(int, input().split()))  
array_n.sort()  
  
print("M 입력")  
m = int(input())  
print("M의 배열 입력")  
array_m = list(map(int, input().split()))  
array_m.sort()  
  
  
# 이진 탐색 풀이  
result = ""  
for i in range(m):  
    result += binary_search(array_n, array_m[i], 0, n-1)  
    result += ' '  
  
print(result)
```

# 풀이2. 계수정렬
``` python
# 계수정렬  
def count_sort(array_n, array_m):  
    result = ""  
    temp_array = [0] * (max(array_n) + 1)  
  
    # 부품 가게에 있는 부품 표시  
    for i in range(len(array_n)):  
        temp_array[array_n[i]] = 1  
  
    # 구매자가 찾는 부품이 가게 있는지 확인  
    for m in array_m:  
        if temp_array[m] == 1:  
            result += 'yes '  
        else:  
            result += 'no '  
  
    return result

print("N 입력")  
n = int(input())  
print("N의 배열 입력")  
array_n = list(map(int, input().split()))  
array_n.sort()  
  
print("M 입력")  
m = int(input())  
print("M의 배열 입력")  
array_m = list(map(int, input().split()))  
array_m.sort()

# 계수정렬 풀이  
result2 = count_sort(array_n, array_m)  
print(result2)
```
