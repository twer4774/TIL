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
    stacked = df_jobs.stack()[7]

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