# 문제
~~~
8 * 8 좌표평면에 나이트가 있다.  
나이트는 L자 형태로만 이동 가능하다.  
1. 수평으로 두칸 이동 뒤 수직으로 한칸 이동  
2. 수직으로 두칸 이동 뒤 수평으로 한칸 이동  
나이트의 위치가 주어졌을때, 이동할 수 있는 경우의 수를 출력하시오  
행의 위치는 1~8로 표현, 열의 위치는 a~h로 표현  
  
입력  
a1  
  
출력  
2
~~~

# 풀이
```
point = { "a":"1", "b":"2", "c":"3", "d":"4", "e":"5", "f":"6", "g":"7", "h":"8"}  
  
start = input()  
start_x = int(point[start[0]]) # 입력된 알파벳 숫자로 매핑  
# print( (int(ord(start[0])) - int(ord('a'))) +1) # 참고. 유니코드 이용. 'a' = 97 입력된 알파벳 숫자로 매핑  
start_y = int(start[1])  
  
moves = [ (2,1), (2,-1), (-2,1), (-2,-1),  
          (1,2), (1,-2), (-1,2), (-1,-2)]  
  
count = 0  
for i in moves:  
    next_x = start_x + i[0]  
    next_y = start_y + i[1]  
    if(1 <= next_x <= 8) and (1 <= next_y <= 8):  
        count = count + 1  
  
print(count)
```
