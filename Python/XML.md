# 파이썬으로 XML처리하기

XML처리를 위한 파이썬 라이브러리 확인 사이트

http://wiki.python.org/moin/PythonXml

가장 많이 사용하는 라이브러리 : ElementTree => python2.5부터 통합됨

```xml
<note date="2180916">
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>Don't forget me this weekend!</body>
</note>
```

```python
from xml.etree.ElementTree import Element, dump

note = Element("note")
to = Element("to")
to.text = "Tove"

note.append(to)
dump(note)
#<note><to>Tove</to></note>
```

### SubElement

```python
#서브엘리먼트를 사용하면 편리하게 태그 추가 가능: 태그명과 태그의 텍스트 값을 한번에 설정 가능
from xml.etree.ElementTree import Element, SubElement, dump

note = Element("note")
to = Element("to")
to.text = "Tove"

note.append(to)
SubElement(note, "from").text = "Jani"

dump(note)
#<note><to>Tove</to><from>Jani</from></note>
```

### 애트리뷰트 추가하기

```python
from xml.etree.ElementTree import Element, SubElement, dump

note = Element("note")
to = Element("to")
to.text = "Tove"

note.append(to)
SubElement(note, "from").text = "Jani"
note.attrib["date"] = "20180916"

dump(note)

#앨리먼트 생성시 직접 애트리뷰트 값 추가방법도 있음
note = Element("note", date="20189=0916")
#<note date="20180916"><to>Tove</to><from>Jani</from></note>

#완성된 코드
form xml.etree.ElementTree import Element, SubElement, dump

note = Element("note")
note.attrib["date"] = "20180916"

to = Element("to")
to.text = "Tove"
note.append(to)

SubElement(note, "from").text = "Jadi"
SubElement(note, "heading").text = "Reminder"
SubElement(note, "body").text = "Don't forget me this weekend!"
dump(note)
#<note date="20180916"><to>Tove</to><from>Jani</from>...생략...</note>
```

### indent함수

정렬된 형태의 xml값으로 보기

```python
form xml.etree.ElementTree import Element, SubElement, dump

note = Element("note")
note.attrib["date"] = "20180916"

to = Element("to")
to.text = "Tove"
note.append(to)

SubElement(note, "from").text = "Jadi"
SubElement(note, "heading").text = "Reminder"
SubElement(note, "body").text = "Don't forget me this weekend!"

def indent(elem, level=0):
    i = "\n" + level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + " "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

indent(note)
dump(note)
```

xml결과

```xml
<note date = "20180916">
	<to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>Don't forget me this weekend!</body>
</note>
```



### 파일에 쓰기

write 메서드로 파일에 xml 쓰기

```python
from xml.etree.ElementTree import ElementTree
ElementTree(note).write("note.xml")
#note.xml파일이 생성됨
```



## XML문서 파싱하기

```python
from xml.etree.ElementTree import parse
tree = parse("note.xml")
note = tree.getroot()

#애트리뷰트 값 읽기
print(note.get("date")) #get메서드로 값을 읽어옴 #20180916
print(note.get("foo", "default")) #default
print(note.keys()) #keys는 모든 애트리뷰트의 키 값을 리스트로 리턴 #['date']
print(note.items()) #key와 value 쌍을 리턴 #[('date', '20180916')]
```

### XML 태그 접근하기

```python
from_tag = note.find("from")#첫번째 태그를 찾아서 리턴, 없으면 None
from_tags = note.findall("from") #note태그 하위에 from과 일치하는 모든 태그를 리스트로 리턴
from_text = note.findtext("from") #note태그 하위에 from과 일치하는 첫 번째 태그의 텍스트 값을 리턴

#특정 태그의 모든 하위 엘리먼트를 순차적으로 처리할 때는 아래의 메서드를 사용한다.
childs = note.getiterator()
childs = note.getchildren()
```

