# Convert Set to JSON

- Python에서 JSON모듈을 이용하면 List는 JSON으로 변환되지만, Set은 변환하지 못하여 에러가 난다.

- 해결 방법 -> JSON Encoder 구현
  - set을 list로 변환시켜 JSON으로 최종 반환

```python
from flask.json import JSONEncoder

#JSONEncoder클래스를 부모 클래스로 상속받는 CustomJSONEncoder 구현
class CustomJSONEncoder(JSONEncoder):
  def default(self, obj): #default 메소드 오버라이딩
    if isinstance(obj, set): #변경하려는 객체가 set이면 최종적ㅇ로 list로 반환
      return list(obj)
    
    #객체가 set이 아닌 경우는 본래 JSONEncoder 클래스의 default메소드 호출
    return JSONEncoder.default(self, obj)
  

#CustomJSONEncoder를 Flask의 디폴트 JSONEncoder로 지정
app.json_encoder = CustomJSONEncoder
```