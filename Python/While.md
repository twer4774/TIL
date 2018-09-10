# While문

반복해서 문장을 실행할 때 이용. 조건문이 참인 동안에 문장을 반복해서 수행한다.

```python
treeHit = 0 #나무를 찍은 횟수
while treeHit < 10: #나무를 찍은 횟수가 10보다 작은 동안 반복한다.
    treeHit = treeHit + 1 #나무를 찍은 횟수 1씩 증가
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit == 10: #나무를 열번 찍으면
        print("나무가 넘어갑니다.")
#나무를 1번 찍었습니다.
#나무를 2번 찍었습니다.
#...
#나무를 10번 찍었습니다.
#나무가 넘어갑니다.
```



### while문 직접 만들기

여러가지 선택지 중 하나를 선택해서 입력받는 예제

```python
prompt = """
	1. Add
	2. Del
	3. List
	4. Quit
	
	Enter number:"""

number = 0 #번호를 입력받을 변수
while number != 4: #입력받은 번호가 4가 아닌 동안 반복
    print(prompt)
    number = int(input()) #입력
```

### while문 강제로 빠져나가기

break

```python
coffe = 10 #자판기에 커피가 10개 있다.
money = 300 #자판기에 넣을 돈은 300원이다.
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffe = coffe -1 #while문을 한 번 돌 때 커피가 하나 줄어든다
    print("남은 커피의 양은 %d개 입니다." %coffee)
    if not coffe:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
```

### break문 이용해 자판기 작동 과정 만들기

```python
#coffe.py
coffee =10
while True:
    money = int(input("돈을 넣어주세요"))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." %(money-300))
        coffee = coffe -1
	else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개입니다." %coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

#coffe.py
#돈을 넣어주세요: 500
#거스름돈 200를 주고 커피를 줍니다.
```

### 조건에 맞지 않는 경우 맨 처음으로 돌아가기

continue

```python
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue #a를 2로 나누었을 때 나머지가 0이면 맨처음으로 돌아간다
	print(a)
    
#1 3 5 7 9 
```

