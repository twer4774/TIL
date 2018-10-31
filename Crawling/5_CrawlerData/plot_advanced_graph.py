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