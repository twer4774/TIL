#-*-encoding:UTF-8-*-
from xml.etree import ElementTree

#parrse() 함수로 파일을 읽어 들이고 ElementTree 객체를 만듦
tree = ElementTree.parse('rss.xml')

#getroot() 메서드로 xml의 루트 요소를 추가
root = tree.getroot()

#findall()메서드로 요소 목록 추출
for item in root.findall('channel/item/description/body/location/data'):
    #find()메서드로 요소를 찾고 text 속성으로 값을 추출
    tm_ef = item.find('tmEf').text
    tmn = item.find('tmn').text
    tmx = item.find('tmx').text
    wf = item.find('wf').text
    print(tm_ef, tmn, tmx, wf)