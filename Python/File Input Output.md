# 파일 읽고 쓰기

## 파일 생성하기

```python
f = open("새파일.txt", 'w')
f.close()
#f.close()는 파일 객체를 닫아주는 역할을 하는데, 파이썬은 프로그램을 종료할 때 자동으로 닫아주기는 하지만 쓰기모드로 열었던 파일을 종료시에 닫을 때 오류가 발생하므로 직접 닫아 주는 것이 좋다. 

#with open(filename, 'r') as f: 구문으로 파일을 다루는 작업 종료시 자동으로 종료되게 할 수 있다.
```

| 파일 열기 모드 |                           설명                           |
| :------------: | :------------------------------------------------------: |
|       r        |           읽기 모드 - 파일을 읽기만 할 때 사용           |
|       w        |           쓰기 모드 - 파일에 내용을 쓸 때 사용           |
|       a        | 추가 모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용 |
|       rb       |                   바이너리 모드로 읽기                   |
|       wb       |                   바이너리 모드로 쓰기                   |
|       ab       |            바이너리 모드로 파일 마지막에 추가            |

## 쓰기모드로 출력값 적기

```python
#writedata.py
f = open("새파일.txt", 'w')
for i in range(1, 11): #1부터 10까지 i에 대입
    data = "%d번째 줄입니다.\n" %i
    f.write(data) #data를 파일 객체 fdp Tjfk
f.close()
```



## 프로그램의 외부에 저장된 파이을 읽는 여러가지 방법

```python
#readline() 함수 이용하기
f = open("새파일.txt", 'r')
lien = f.readline()
print(line)
f.close()
#모든 라인을 읽어 오고 싶을때
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

#readlines()함수 이용하기
#각각의 줄을 요소로 리스트 형식으로 반환
lines = f.readlines()
for line in lines:
    print(line)
f.close()

#read() 함수 이용하기
#파일의 내용 전체를 문자열로 리턴
data = f.read()
print(data)
f.close()
```



## 파일에 새로운 내용 추가하기

```python
#adddata.py
f.open("새파일.txt", 'a')
for i in range(11, 20): #11부터 19까지 i에 대입
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()
```



## 파일 데이터 처리하기

```python
#데이터 처리하기
#연도별 출생아 수 계산하기
def countBirths():
    ret = [] #(연도, 출생아 수) 튜플이 요소인 리스트로 구성될 변수
    for y in range(1880, 2016):
        count = 0 #연도별 출생아 수
        filename = 'names/yob%d.txt'%y
        with open(filename,'r') as f:
            data = f.readlines()
            for d in data:
                if d[-1] == '\n': #마지막 문자가 \n 이면 \n을 제외한 문자열을 d에 재지정
                    d = d[:-1]

                birth = d.split(',')[2] #세번째 요소가 출생아
                count += int(birth)
            ret.append((y,count))
    return ret
result = countBirths()

with open('birth_by_year.csv', 'w') as f: #엑셀에서 불러올 수 있는 파일로 만듦
    for year, birth in result:
        data = '%s,%s\n' %(year,birth)
        print(data)
        f.write(data)


#연도별 성별 출생아 수 계산하기
def countBirthsBySex():
    ret2 = []
    for y in range(1880, 2016):
        count_f = 0 #여자아기 출생아 수
        count_m = 0 #남자아기 출생아 수
        filename = 'names/yob%d.txt' %y

        with open(filename, 'r') as f:
            data2 = f.readlines()
            for d in data2:
                if d[-1] == '\n':
                    d = d[:-1]

                tmp = d.split(',')
                sex = tmp[1]
                birth = tmp[2]

                if sex == 'F':
                    count_f += int(birth)
                else:
                    count_m += int(birth)
        ret2.append((y, count_f, count_m))
    return ret2

result = countBirthsBySex()
with open('birth_by_sex.csv', 'w') as f:
    for y, bf, bm in result:
        data2 ='%s, %s, %s\n' %(y,bf,bm)
        print(data2)
        f.write(data2)


#연도별 인기있는 상위 10개 성별 출생아 이름 구하기
from os.path import exists

def getTop10BabyName(year):
    nameF = {}
    nameM = {}

    filename3 = 'names/yob%s.txt' %year
    if not exists(filename3):
        print('[%s]파일이 존재하지 않습니다'%filename3)
        return None

    with open(filename3, 'r') as f:
        data3 = f.readlines()
        for d in data3:
            if d[-1] == '\n':
                d = d[:-1]

            tmp = d.split(',')
            name = tmp[0]
            sex = tmp[1]
            birth = tmp[2]

            if sex == 'F':
                ret = nameF
            else:
                ret = nameM

            if name in ret:
                ret[name] += int(birth)
            else:
                ret[name] = int(birth)
        retF = sorted(nameF.items(), key=lambda  x:x[1], reverse=True)
        retM = sorted(nameM.items(), key=lambda  x:x[1], reverse=True)

        for i, name in enumerate(retF):
            if i>9:
                break
            print('TOP_%d 여자아가이름: %s' %(i+1, name))

        for i, name in enumerate(retM):
            if i>9:
                break
            print('TOP_%d 남자아가이름:%s' %(i+1, name))

y = input('인기순 상위 10개 이름을 알고 싶은 출생년도를 입력하세요(예2001):')
getTop10BabyName(y)

```

