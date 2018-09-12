# 사용자 입력과 출력

## 사용자 입력

```python
#input의 사용: 입력되는 모든것을 문자열로 취급
a = input()
#Life is too short, you need python
a #Life is too short, you need python

#프롬프트를 띄워서 사용자 입력 받기: 질문 내용을 터미널에 표시함
number = input("숫자를 입력하세요")
#숫자를 입력하세요:

```

## print 

print문의 다양한 예

```python
#큰 따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
print("life" "is" "too short")
#lifeistoo short
print("life" + "is" + "too short")
#lifeistoo short

#문자열 띄워쓰기는 콤마로 한다.
print("life", "is", "too short")
#life is too short

#한줄에 결과값 출력하기
for i in range(10):
    print(i, end = '')
#0 1 2 3 4 5 6 7 8 9
```

