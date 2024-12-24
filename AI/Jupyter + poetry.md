- poetry로 jupyter notebook을 설치하고 ipynb를 vscode로 이용하는 방법

- [주피터 사용법 참고 - 원격접속설정 포함] https://greeksharifa.github.io/references/2019/01/26/Jupyter-usage/
# poetry + Jupyter  설정
```
# 접속
poetry shell

# 초기화 기본 설정 (모두 enter)
poetry init

poetry install


# 주피터 설치
poetry add jupyter
poetry run ipython kernel install --user --name="slm-jupyter"

# 주피터 실행
poetry run jupyter-notebook

```
