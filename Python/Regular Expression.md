# 파이썬 정규표현식과 XML

## 정규표현식

### 왜 필요한가?

예) 주민등록번호를 포함하고 잇는 텍스트가 잇는데, 모든 주민등록번호의 뒷자리를 *문자로 변경

정규표현식을 사용하지 않을 경우

1. 전체 텍스트를 공백 문자로 나눈다.(split)

2. 나누어진 단어들이 주민등록번호 형식인지 조사한다.

3. 단어가 주민등록번호 형식이라면 뒷자리를 '*'로 변환한다.

4. 나누어진 단어들을 다시 조합한다.

   ```python
   data = """
   park 800905-1049118
   kim  700905-1059119
   """
   
   result = []
   for line in data.split("\n"):
       word_result = []
       for word in line.split(""): #공백마다 나누기
           if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
               word = word[:6] + "-" + "*******"
           word_result.append(word)
      	result.append("".join(word_result)) #나눈 단어 조립
   print("\n".join(result))
   ```

정규식을 사용할 경우

```python
import re

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6}[-]\{7})")
print(pat.sub("\g<1>-*******", data))
```



## 정규 표현식의 기초, 메타문자

메타문자: 원래의 뜻이 아닌 특별한 용도로 사용되는 문자

```
.^$*+?{}[]\|()
```



## 문자클래스 [] : []사이의 문자들과 매치

[abc]라면 a,b,c중 한개의 문자와 매치 => a, before는 a,b,c 중 한개가 일치하므로 참
[a-c]와 [abc]는 동일
[0-5]와 [012345]는 동일
[a-zA-Z]: 알파벳 모두

\[0-9]: 숫자

^메타문자는 not의 의미 =>\[^0-9]는 숫자가 아닌 문자만 매치

| 정규 표현식 |                             설명                             |
| :---------: | :----------------------------------------------------------: |
|     \d      |              숫자와 매치, [0-9]와 동일한 표현식              |
|     \D      |         숫자가 아닌것과 매치,\[^0-9]와 동일한 표현식         |
|     \s      | whitespace문자와 매치, [\t\n\r\f\v]와 동일한 표현식<br />맨 앞의 빈 칸은 공백문자 |
|     \S      | whitespace 문자가 아닌 것과 매치, \[^\t\n\r\f\v]와 동일한 표현식 |
|     \w      | 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9]와 동일한 표현식  |
|     \W      | 문자+숫자가 아닌 문자와 매치, \[^a-zA-Z0-9]와 동일한 표현식  |

## Dot(.)

정규 표현식의 Dot(.) 메타 문자는 줄바꿈 문자인 \n를 제외한 모든 문자와 매치됨

a.b => a와 b사이에 줄바꿈 문자를 제외한 어떤 문자가 들어가도 모두 매치 "a + 모든 문자 +b"

| 정규식 | 문자열 | 매치여부 |                             설명                             |
| :----: | :----: | :------: | :----------------------------------------------------------: |
|  a.b   |  aab   |    Y     | 가운데 a가 모든 문자를 의미하는 .과 일치하므로 정규식과 매치 |
|        |  a0b   |    Y     | 가운데 0이 모든 문자를 의미하는 .과 일치하므로 정규식과 매치 |
|        |  abc   |    N     | a와 b사이에는 어떤 문자라도 하나 있어야 함. a와 b사이에 문자가 없으므로 매치되지 않음 |

a[.]b => a와 b사이에 Dot(.)문자가 있으면 매치 ==> "a+Dot(.)문자+b"



## 반복(*)

cat*t => *문자 바로 앞에 있는 a가 0번 이상 반복되면 매치

| 정규식 | 문자열 | 매치여부 |                 설명                 |
| :----: | :----: | :------: | :----------------------------------: |
| cat*t  |   ct   |    Y     |        a가 0번 반복되어 매치         |
|        |  cat   |    Y     | a가 0번 이상 반복되어 매치(1번 반복) |
|        | caaat  |    Y     | a가 0번 이상 반복되어 매치(3번 반복) |

## 반복(+)

최소 1번 이상 반복될 때 사용. *가 반복 횟수 0부터라면 +는 반복횟수 1부터인 것

ca+t => +문자 바로 앞에 있는 a가 1번 이상 반복되면 매치

| 정규식 | 문자열 | 매치 여부 |                 설명                 |
| :----: | :----: | :-------: | :----------------------------------: |
| cat+t  |   ct   |     N     |    a가 0번 반복되어 매치되지 않음    |
|        |  cat   |     Y     | a가 1번 이상 반복되어 매치(1번 반복) |
|        | caaat  |     Y     | a가 1번 이상 반복되어 매치(3번 반복) |



## 반복({m,n},?)

{}로 반복횟수 고정 가능

### 1. {m}

ca{2}t => a가 2번 반복되면 매치 ==> c+a(반드시 2번 반복)+t

| 정규식 | 문자열 | 매치여부 |               설명               |
| :----: | :----: | :------: | :------------------------------: |
| ca{2}t |  cat   |    N     | a가 1번만 반복되어 매치되지 않음 |
|        |  caat  |    Y     |     a가 2번 반복되어 매치됨      |

### 2.{m,n}

cat{2,5}t => a가 2~5번 반복되면 매치 ==> c+a(2~5번반복)+t

|  정규식   | 문자열  | 매치여부 |               설명               |
| :-------: | :-----: | :------: | :------------------------------: |
| cat{2,5}t |   cat   |    N     | a가 1번만 반복되어 매치되지 않음 |
|           |  caat   |    Y     |     a가 2번 반복되어 매치됨      |
|           | caaaaat |    Y     |     a가 5번 반복되어 매치됨      |

### 3.? 

{0,1}을 의미함

ab?c => b가 0~1번 사용되면 매치

| 정규식 | 문자열 | 매치여부 |         설명          |
| :----: | :----: | :------: | :-------------------: |
|  ab?c  |  abc   |    Y     | b가 1번 사용되어 매치 |
|        |   ac   |    Y     | b가 0번 사용되어 매치 |



## 파이썬에서 정규 표현식을 지원하는 re 모듈

파이썬이 설치될때 자동으로 설치되는 기본 라이브러리

```python
import re
p = re.compile('ab*')
```

## 정규식을 이용한 문자열 검색

|   메서드   |                             목적                             |
| :--------: | :----------------------------------------------------------: |
|  match()   |       문자열의 처음부터 정규식과 매치되는지 조사한다.        |
|  search()  |     문자열 전체를 검색하여 정규식과 매치되는지 조사한다.     |
| findall()  | 정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴한다. |
| finditer() | 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 리턴한다. |

```python
import re
p = re.compile('[a-z]+')

#match
m = p.match("python")
print(m) #<_sre.SRE_Match object at 0x01F3F9F8> 정규식에 부합하므로 객체를 리턴함
n = p.match("3 python")
print(n) #None

'''
파이썬 정규식 프로그램의 흐름
p = re.compile(정규 표현식)
m = p.match("조사할 문자열")
if m:
	print('Match found:', m.group())
else:
	print('No match')
'''

#search
m = p.search("python")
print(m) #<_sre.SRE_Match object at 0x01F3F9F8>

m = p.search("3 python")
print(m) #<_sre.SRE_Match object at 0x01F3F9F8>
#3이후의 python이라는 문자열과 매치된다.


#findall
result = p.findall("life is too short")
print(result)
#['life', 'is', 'too', 'short']

#finditer
result = p.finditer("life is too short")
print(result)
#<callable_iterator object at 0x01F5E390>
for r in result: print(r)
#<_sre.SRE_Match object at 0x01F3F9F8>
#<_sre.SRE_Match object at 0x01A4F1D8>
#<_sre.SRE_Match object at 0x01F5B4C8>
```



### match 객체의 메서드

-어떤 문자열이 매치되었는가?

-매치된 문자열의 인덱스는 어디부터 어디까지인가?

| 메서드  |                          목적                          |
| :-----: | :----------------------------------------------------: |
| group() |               매치된 문자열을 리턴한다.                |
| start() |         매치된 문자열의 시작 위치를 리턴한다.          |
|  end()  |          매치된 문자열의 끝 위치를 리턴한다.           |
| span()  | 매치된 문자열의 (시작, 끝)에 해당되는 튜플을 리턴한다. |

```python
import re
p = re.compile('[a-z]+')
m = p.match("python")
m.group() #'python'
m.start() #0
m.end() #6
m.span() #(0,6)

m = p.search("3 python")
m.group() #'python'
m.start() #2
m.end() #8
m.span() #(2,8)
```



### 컴파일 옵션

|   옵션명   | 약어 |                             설명                             |
| :--------: | :--: | :----------------------------------------------------------: |
|   DOTALL   |  S   |  줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.   |
| IGNORECASE |  I   |         대,소문자에 관계 없이 매치할 수 있도록 한다.         |
| MULTILINE  |  M   | 여러 줄과 매치할 수 있도록 한다. (^, $메타 문자의 사용과 관계가 있는 옵션) |
|  VERBOSE   |  X   | verbose 모드를 사용할 수 있도록 한다.(정규식을 보기 편하게 만들 수도 있고 주석 등을 사용할 수도 있다.) |

옵션사용시 re.DOTALL 과 re.S는 똑같음.

```python
import re
p = re.compile('a.b')
m = p.match('a\nb')
print(m) #None
#\n문자와도 매치되게 하려면 re.DOTALL 옵션

#DOTALL, S
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)
#<_sre.SRE_Match object at 0x01F3F9F8>

#IGNORECASE, I
p = re.compile('[a-z]', re.I)
p.match('python')
#<_sre.SRE_Match object at 0x01F3F9F8>
p.match('Python')
#<_sre.SRE_Match object at 0x01A3C9D8>
p.match('PYTHON')
#<_sre.SRE_Match object at 0x01C3B9F8>

#MULTILINE, M
#^(문자의 처음), $(문자의 마지막)을 의미. '^python'인 경우 문자열의 처음은 항상 python으로 시작해야 매치가 됨
import re
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three
"""
print(p.findall(data))
#['python one'] 첫번째 라인만 매치가 됨
#만약 p = re.compile("^python\s\w+", re.MULTILINE)으로 옵션을 붙인다면
#['python one', 'python two', 'python three']가 출력됨

#VERBOSE, X
#정규식을 주석 또는 라인단위로 구분
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
#정규식이 복잡할 경우, 주석을 적고 여러줄로 표현하는 것이 가독성이 좋음
charref = re.compile(r"""
&[#]					#Start of a numeric entity reference
(
	0[0-7]+				#Octal form
	|[0-9]+				#Decimal form
	|x[0-9a-fA-F]+		#Hexadecimal form
	)
	;					#Trailling semicolon
""",re.VERBOSE)

```

### 백슬래시 문제

파일 내에서 "\section" 이라는 문자열을 찾기위해 \section을 하면 \s가 이스케이프 문자로 인식되어버림

=> \\section으로 해야함.

p = re.compile('\\section')



# zero-width assertions(문자열소모가 없는 메타문자)

```python
#|: or과 동일한 의미
p = re.compile('Crow|Seervo')
m = p.match('CrowHello')
print(m)
#<_Sre.SRE_Match object; span=(0,4), match='Crow'>

#^: 문자열의 맨 처음과 일치함을 의미
#$: 문자열의 맨 마지막과 일치함을 의미
#\A: 문자열의 처음과 매치됨을 의미. ^와 동일한 의미지만, re.MULTILINE옵션을 사용할 경우 ^는 모든 라인, \A 전체문자열의 처음하고만 매치
#\Z: 문자열의 끝과 매치됨을 의미.
#\b: 단어 구분자. whitespace(공백)으로 구분된 단어만 매치
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
#<_Sre.SRE_Match object at 0x01F6F3D8>
#\B: \b와 반대, whitespace로 구분된 단어가 아닌경우에만 매치
p = re.compile(r'\Bclass\B')
print(p.search('the declassified algorithm'))
#<_Sre.SRE_Match object at 0x01F6F3D8>

```



### 그룹핑: 해당 문자열이 계속해서 반복되는지 조사하는 정규식 작성에 이용

```python
(ABC)+
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
#<_Sre.SRE_Match object at 0x01F6F3D8>
print(m.group(0)1234
#ABCABCABC
p = re.compiler(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
     
#이름 부분만 뽑아낼 때
p = re.compiler(r"(\w+)\s+\d\[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1)) #park
```



| group(인덱스) |              설명              |
| :-----------: | :----------------------------: |
|   group(0)    |       매치된 전체 문자열       |
|   group(1)    | 첫 번째 그룹에 해당되는 문자열 |
|   group(2)    | 두 번째 그룹에 해당되는 문자열 |
|   group(n)    | n 번째 그룹에 해당되는 문자열  |



```python
p = re.compiler(r"\(w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(2))
#010-1234-1234

#국번만 뽑을때 ()로 그룹을 나눔
p = re.compile(r"(\w+)\s+(\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(3)) #010
```



## 그룹핑된 문자열 재참조하기

```python
p = re.compiler(r'(\b\w+)\s+\1') #(rmfnq)+""+그룹과 동일한 단어와 매치됨 => 2개의 동일한 단어가 연속적으로 사용되어야만 매치됨(\1은 재참조 메타문자로, 정규식의 그룹중 첫번째 그룹을 지칭함)
p.search('Paris in the the spring').group()
#the the
```

### 그룹핑된 문자열에 이름 붙이기

- 정규식 내에 그룹이 많아지면 혼란
- 정규식이 수정되면서 그룹이 추가, 삭제되면 인덱스도 변경해주어야함
- 인덱스가 아닌 이름으로 참조하기

```python
(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+) #?는 정규식의 확장구문 => 가독성이 떨어지지만 강력함을 기능을 강력하게 해준다.

p = re.compiler(r"(?P<nmae>\w+)\s+((\d+)[-]\d+[-]\d+)") #name이라는 그룹명으로 참조
m = p.search("park 010-1234-1234")
print(m.group("name")) #park

#그룹명을 이용하면 정규식 내에서 재참조하는것도 가능
p = re.compiler(r'(?P<word>\b\w+)\s+(?P=word)') #확장 구문으로 재참조
p.search('Paris in the the spring').group() #the the
```

### 전방 탐색

가장 어려워하는 부분이며, 정규식 안에 이 확장 구문이 사용되면 순식간에 암호문처럼 알아보기 어렵게 바뀐다.

```python
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group()) #http:
```

| 정규식  |       종류       |                             설명                             |
| :-----: | :--------------: | :----------------------------------------------------------: |
| (?=...) | 긍정형 전방 탐색 | ...에 해당되는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소모되지 않는다. |
| (?!...) | 부정형 전방 탐색 | ...에 해당되는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소모되지 않는다. |

### 긍정형 전방 탐색

```python
#긍정형 전방 탐색을 이용하면 http:의 결과를 http로 바꿀 수 있음
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group()) #http
```

```python
.*[.].*$ #파일명 + . + 확장자를 나타내는 정규식

#bat인 파일은 제외하는 조건 ^는 not을 의미
.*[.]([^b].?.?|.[^a]?.?|..?[^t])$ #확장자의 문자 개수가 2개여도 통과되는 정규식
```

### 부정형 전방 탐색

위의 예와 같이 파일을 제외하는 조건은 부정형 전방탐색이 유용하다.

```python
.*[.](?!bat$).*$ #확장자가 bat가 아닌 경우에만 통과
.*[.](?!bat$|exe$).*$ #확장자 bat, exe파일 제외
```

### 문자열 바꾸기

sub메서드를 이용하면 정규식과 매치되는 부분을 다른 문자로 쉽게 바꿀수 있음

```python
p = re.compile('(bule|white|red)')
p.sub('colour', 'blue socks and red shoes')
#colour socks and colour shoes #sub('바꿀문자열', '대상문자열') => blue,white,red문자열을 colour로 바꿈

#딱 한번만 바꾸고 싶은 경우 세번째 인자에 count값을 넘김
p.sub('colour', 'blue socks and red shoes', count=1)
#colour socks and red shoes #blue만 colour로 바꿈(1번만 실행되므로)
#subn이라는 메서드가 있는데, 이 메서드는 결과를 튜플형식으로 바꿔주는 역할을 한다.

#sub 메서드 사용 시 참조 구문 사용: '이름+전화번호' -> '전화번호+이름'으로 변경
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>", "park 010-1234-1234")
print(p.sub("\g<2> \g<1>", "park 010-1234-1234"))
#010-1234-1234 park
#010-1234-1234 park
      
      
#sub 메서드의 입력 인수로 함수 넣기: 16진수로 변경
def hexrepl(match):
	"Return the hex string for a decimal number"
    value = int(match.group())
    return hex(value)
p = re.compile(r'\d+')
p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
#Call 0xffd2 for printing, 0xc000 for user code

#Greedy vs Non-Greedy
s = '<html><head><title>Title</title>'
len(s) #32
print(re.match('<.*>',s).span())
#(0, 32)
print(re.match('<.*>',s).group())
#<html><head><title>Title</title>

#*의 탐욕 제거하기 가능한한 최소한의 반복을 수행하도록 도와주는 역할
print(re.match('<.*?>',s).group())
#<html>
```

