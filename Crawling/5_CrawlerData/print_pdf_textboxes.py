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