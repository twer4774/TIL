# PDF에서 추출하기

- PDF는 어도비 시스템즈에서 개발한 문서전용 파일 형식
- PDF형식의 데이터는 다루기 어려움
  - 주의사항
    - 표 형식의 데이터를 그대로 추출하기 어려움
      - 단순한 문자열로 추출한뒤 가공처리해야 함
    - 이미지 밖에 없는 경우(스캔으로 이미지떠서 PDF로 만든경우)
      - 텍스트로 변환을 위해 OCR 소프트웨어 사용(Tessertact)
      - 파이썬에서는 PyOCR라이브러리 이용
    - 비밀번호를 모르면 추출 불가
    - 읽을 수 없는 경우
      - PDF파일의 사양은 굉장히 복잡하기 때문에 데이터 추출이 불가능한 경우도 있음

### PDFMiner.six로 PDF에서 텍스트 추출

- 설치

```
wget https://pypi.python.org/packages/source/p/pdfminer.six/pdfminer.six-20160202.zip
unzip pdfminer.six-20160202.zip
cd pdfminer.six-20160202
python3 setup.py install
```

- 사용

```python
pdf2txt.py jejuweb.pdf
제주대학교 웹진 관리 시스템

2017. 3. 16. 오후 3:22

'왔수다팀', 은상 등 수상

 글쓴이 : 홍보출판문화원

작성일 : 16-12-14 15:29     조회 : 252

미래창조과학부와 한국정보화진흥원이 공동 개최한 ‘K-ICT NET챌린지 캠프 시즌3 시상식’에서 제주대 왔수다팀(지
도교수:송왕철)이 ‘IoT를 활용한 관광 서비스’로 은상과 ㈜LG유플러스 통신사상을 동시에 수상했다고 14일 밝혔다.
```

```python
#print_pdf_textboxes.py
#python3 print_pdf_textboxes.py jejuweb.pdf
import sys

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer, LTTextBox
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage

def find_textboxes_recursively(layout_obj):
    #재귀적으로 텍스트박스를 찾고 리스트로 반환
    if isinstance(layout_obj, LTTextBox):
        return [layout_obj]
    #LTContainer를 상속 받는 개체는 자식요소가 포함한다는 의미이므로 재귀적으로 자식요소를 찾음
    if isinstance(layout_obj, LTContainer):
        boxes = []
        for child in layout_obj:
            boxes.extend(find_textboxes_recursively(child))
        return boxes
    #아무것도 없다면 빈 리스트 반환
    return []

#공유 리소스를 관리하는 리소스 매니저 생성
laparams = LAParams()
resource_manager = PDFResourceManager()

#페이지를 모으는 PageAggregator 객체 생성
device = PDFPageAggregator(resource_manager, laparams=laparams)

#Interpreter 객체 생성
interpreter = PDFPageInterpreter(resource_manager, device)

#파일을 바이너리 형식으로 읽음
with open(sys.argv[1], 'rb') as f:
    #PDFPage객체를 차례대로 추출
    for page in PDFPage.get_pages(f):
        #페이지 처리
        interpreter.process_page(page)
        #LTPage 객체 추출
        layout = device.get_result()
        #페이지 내부의 텍스트 박스를 리스트로 추출
        boxes = find_textboxes_recursively(layout)
        #텍스트 박스 왼쪽 위의 좌표부터 차례로 정렬
        #y좌표는 위에 있을수록 크므로 음수로 변환해 처리함
        boxes.sort(key=lambda b: (-b.y1, b.x0))
        for box in boxes:
            #읽기 쉽게 선을 출력
            print('-'*10)
            print(box.get_text().strip())
            
#결과
----------
제주대학교 웹진 관리 시스템
----------
2017. 3. 16. 오후 3:22
----------
'왔수다팀', 은상 등 수상
----------
글쓴이 : 홍보출판문화원
----------
작성일 : 16-12-14 15:29     조회 : 252
----------
미래창조과학부와 한국정보화진흥원이 공동 개최한 ‘K-ICT NET챌린지 캠프 시즌3 시상식’에서 제주대 왔수다팀(지
도교수:송왕철)이 ‘IoT를 활용한 관광 서비스’로 은상과 ㈜LG유플러스 통신사상을 동시에 수상했다고 14일 밝혔다.
```

