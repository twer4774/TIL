# 그래프로 시각화하기

- 파이썬에서 그래프를 그릴 때 matplotlib라이브러리 사용

```
pip3 install matplotlib
```

```python
>>> import matplotlib.pyplot as plt
>>> plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
[<matplotlib.lines.Line2D object at 0x118ec5f60>]
>>> plt.show()
#그래프 표시됨
```

```python
#plot_advanced_graph.py
import matplotlib

#랜더링 백엔드로 데스크톱 환경이 필요없는 Agg 사용
matplotlib.use('Agg')

#한국어 렌더링 폰트 지정
matplotlib.rcParams['font.sans-serif'] = 'NanumGothic,AppleGothic'

import matplotlib.pyplot as plt

#plot()의 세번째 매개벼수로 계열 스타일을 나타내는 문자열 지정
#'b'는 파란색, 'x'는 x 표시마커, '-'는 마커를 실선으로 연결
plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 'bx-', label='첫 번째 함수')

plt.plot([1, 2,3, 4, 5], [1, 4, 9, 16, 25], 'ro--', label='두 번째 함수')

plt.xlabel('X값')
plt.ylabel('Y값')
plt.title('샘플')
#elgend()함수로 범례 출력. best는 적당한 위치에 출력하라는 뜻
plt.legend(loc='best')

#x축 범위를 0-6으로 지정. ylim()함수를 사용하면 y축 범위 지정 가능
plt.xlim(0, 6)

#그래프를 그리고 파일로 저장함
plt.savefig('advanced_graph.png', dpi=300)
```



### CSV파일을 읽어들여 그래프 그리기

- pandas로 읽어 들임
- matplotlib로 그래프 그림
- 책에 나와있는 gugik.xlsx 파일은 예전파일이라서 지금 쓰려면 사이트에 가서 이것저것 조작을 많이해야함 => gugik2.xlsx파일로 생성함(예전파일 형식으로 만듦. 단 데이터가 81년도 부터 없어 2000년부터 실행해 두 그래프의 시점이 다르다.)

```python
#plot_historical_data.py
from datetime import datetime
import pandas as pd

import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['font.sans-serif'] = 'NanumGothic,AppleGothic'
import matplotlib.pyplot as plt

def main():
    #환율 정보 읽기
    df_exchange = pd.read_csv('DEXKOUS.csv', header=1, names=['DATE', 'DEXKOUS'], skipinitialspace=True, index_col=0)
    years = {}
    output = []
    for index in df_exchange.index:
        year = int(index.split('-')[0])
        if(year not in years) and (1981 < year < 2014):
            if df_exchange.DEXKOUS[index] != ".":
                years[year] = True
                output.append([year, float(df_exchange.DEXKOUS[index])])
    df_exchange = pd.DataFrame(output)


    #고용률 통계 구하기
    df_jobs = pd.read_excel('gugik2.xlsx')
    output = []
    stacked = df_jobs.stack()[7] #행과 열 뒤집기

    for index in stacked.index:
        try:
            if 2001 <= int(index) <= 2014:
                output.append([int(index), float(stacked[index])])
        except:
            pass
    s_jobs = pd.DataFrame(output)
    

    #첫번째 그래프
    plt.subplot(2, 1, 1)
    plt.plot(df_exchange[0], df_exchange[1], label='원/달러')
    plt.xlim(1981, 2014)
    plt.ylim(500, 2500)
    plt.legend(loc='best')

    #두번째 그래프
    print(s_jobs)
    plt.subplot(2, 1, 2)
    plt.plot(s_jobs[0], s_jobs[1], label='고용률(%)')       
    plt.xlim(1981, 2014)
    plt.ylim(0, 100)
    plt.legend(loc='best')
    plt.savefig('historical_data.png', dpi=300)

if __name__ == '__main__':
    main()
    
#결과는 png파일로 나옴
```

