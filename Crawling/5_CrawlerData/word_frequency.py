import sys
import os
from glob import glob
from collections import Counter
from konlpy.tag import Kkma

def main():
    #명령라인 매개변수로 지정한 디렉터리 내부의 파일을 읽고 빈출단어 출력
    #첫번째 매개변수로 WikiExtractor의 출력 디렉터리 지정
    input_dir = sys.argv[1]
    kkma = Kkma()

    #빈출 단어 저장을 위한 Counter객체 생성
    frequency = Counter()
    count_proccessed = 0

    #glob()으로 와일드카드 매치 파일 목록을 추출하고 매치한 모든 파일 처리
    for path in glob(os.path.join(input_dir, '*', 'wiki_*')):
        print('Processing {0}...'.format(path), file=sys.stderr)
        #파일을 엶
        with open(path) as file:
            #파일 내부의 모든 기사에 반복을 돌림
            for content in iter_docs(file):
                #페이지에서 명사 리스트 추출
                tokens = get_tokens(kkma, content)
                #Counter의 update() 메서드로 리스트 등의 반복 가능 객체를 지정하면
                #리스트에 포함된 값의 출현 빈도를 세어줌
                frequency.update(tokens)
                #10,000개의 글을 읽을때마다 간단하게 출력
                count_proccessed += 1
                if count_proccessed % 10000 == 0:
                    print('{0} documents were processed.'.format(count_proccessed), file=sys.stderr)

            #모든 기사의 처리가 끝나면 상위 30개의 단어 출력
            for token, count in frequency.most_common(30):
                print(token, count)

def iter_docs(file):
    #파일 객체를 읽어들이고 기사 내용(<doc ... </doc>)을 꺼내는 제너레이터함수
    for line in file:
        if line.startswith('<doc '):
            #시작 태그를 찾으면 버퍼 초기화
            buffer = []
        elif line.startswith('</doc>'):
            #종료 태그를 찾으면 버퍼의 내용을 결한한 뒤 yield 함
            content = ''.join(buffer)
            yield content
        else:
            #시작 태그/종료 태그 이외의 줄은 버퍼에 추가
            buffer.append(line)

def get_tokens(kkma, content):
    #문장 내부에 출현한 명사 리스트 추출
    tokens = []
    node = kkma.pos(content)
    for (taeso, pumsa) in node:
        #고유 명사와 일반 명사만 추출
        if pumsa in ('NNG', 'NNP'):
            tokens.appned(taeso)
    return tokens

if __name__ == '__main__':
    main()