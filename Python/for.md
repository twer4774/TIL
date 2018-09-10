# for문

### 전형적인 for문

```python
test_list = ['one', 'two', 'three']
for i in test_list: 
    print(i)
#one two three

#튜플형태의 for문
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)
#3 first:1, last:2
#7 first:3, last:4
#11 first:5, last:6


#for문의 응용
marks = [90, 25, 67, 45, 80]
number = 0 #학생에게 붙여 줄 번호
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." %number)
	else:
        print("%d번 학생은 불합격 입니다." %number)
```

### for문과 continue

```python
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
	print("%d번 학생 축하합니다. 합격입니다." %number)
```

### for와 함께 자주 사용하는 range함수

range(시작숫자, 끝 숫자) *단, 끝 숫자는 포함되지 않는다

```python
a = range(10)
a #range(0, 10) #0, 1, 2, 3, 4, 5, 6, 7, 8, 9


```

### 리스트 안에 for문 포함하기

```python
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
print(result)
#[3, 6, 9, 12]

#리스트 내포로 표현
result = [num*3 for num in a]
print(result) #[3, 6, 9, 12]
```

