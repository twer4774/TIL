## 딕셔너리를 사용하는 방법

- 딕셔너리에서 Key로 Value 얻기

```python
grade = {'pey': 10, 'julliet': 99}
grade['pey']  #10
```

- 딕셔너리를 만들때 주의할 사항

- - key를 중복해서 사용해서는 안된다. 어떤 Key와 Value값이 무시될지 모른다.
  - 튜플은 Key로 사용 가능하지만, 리스트는 Key로 이용할 수 없다. => Key가 변하는지 변하지 않는지의 차이
  - Value에는 리스트를 포함해 사용 가능하다

## 딕셔너리 관련 함수들

1. Key 리스트 만들기(keys)

```python
a = {'name': 'pey', 'hone': '0109993323', 'birth': '1118'}
a.keys()  #dict_keys(['name', 'phone', 'births'])
for k in a.keys():
print(k)
# phone
# birth
# name
```

2. dic_keys 객체를 리스트로      변환

```python
list(a.keys())  #['phone', 'birth', 'name']
```

3. Value 리스트 만들기(values)

```python
a.values() # dict_values(['pey' '0119993323', '1118'])
```

4. Key, Value 쌍 얻기(items) => 튜플로 반환

```python
a.items()  # dict_items(['name', 'pey'), ('phone', '011999332'), ('birth', '1118')])
```

5. key: Value 쌍 모두 지우기(clear)

```python
a.clear()
a  #{}
```

6. Key로 Value얻기(get)

```python
a.get('name')  # 'pey'
#*a['name']으로 한 것과 결과는 동일. 
#다만, get을 할 경우 사전에 없는 Key값을 가져오면 None을 반환함. a['name']은 오류를 반환함
a.get('foo','bar') #'bar' get(x, '디폴트값') 해당하는 값이 없으면 디폴트 값 반환함
```

7. 해당 Key가 딕셔너리 안에 있는지 조사하기(in)

```python
'name' in a  #True
```