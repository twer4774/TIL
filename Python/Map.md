# Map

- Python의 내장 함수
- map( f, iterable) 이용
- 함수와 반복가능한 자료형을 입력으로 받아 함수 f의 결과로 묶어서 리스트로 반환

```python
def two_times(number_list):
  result = []
  for number in number_list:
    result.appned(number*2)
   return result

result = tow_times([1, 2, 3, 4])
print(result) #[2, 4, 6, 8]

#map 이용
def two_times(x) : return x * 2
list(map(tow_times, [1, 2, 3, 4])) #[2, 4, 6, 8]

#map + lambda 이용
list(map(lambda x: x*2, [1, 2, 3, 4]))
```

