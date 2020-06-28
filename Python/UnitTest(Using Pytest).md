# Unit Test

- 테스트 자동화
  - 매뉴얼 테스트 - 사람이 직접 하는것
    - 직관적이고 큰 계획이 없어도 가능
    - 시간이 오래걸리며 부정확함
  - 테스트 자동화
    - 반복, 자주 실행될 수 있도록 해야 함
    - 항상 정확해야 하며, 빠지는 부분이 없도록 해야 함
- 시스템 테스트 방법
  - performacne test
  - load test
  - 기능 테스트
    - UI Test (End-To-End Test)
      - User Interface를 통해 테스트
      - 서비스의 실제 구동방식과 동일하게 테스트 할 수 있음
      - 시간이 가장 많이 소요되는 테스트
        - 프론트에서부터 백엔드까지 모든 시스템을 실행시킴
        - 자동화하기 가장 까다로움 
      - 셀레니엄(Selenium) 같은 UI test 프레임워크 사용하여 자동화 가능
      - 디자인 렌더링부분에서 자동화가 힘듦
      - => 많은 단점들 때문에 꼭 필요한 테스트지만 비중을 가장 적게한다.
    - intergration Test
    - **unit test**

## Unit test

- 100% 자동화 가능. 메소드 단위로 테스트 코드 작성
- 장점
  - 실행하기 쉬움
  - 실행 속도 빠름
  - 100% 자동화
  - 디버깅이 쉬움
- 단점
  - 전체적인 테스트에 제한적
    - 단점을 보완하기 위해 intergration test와 UI test 병행
    - UI test(10%), Intergration Test(20%), Unit test(70%)
- 코드를 테스트하는 코드 작성

```python
def multiply_by_two(x):
  return x * 2
```

multiply_by_two 함수를 호출한 후 결과값이 예상하는 값과 동일한지 확인하는 코드 구현

```python
assert multiply_by_two(2) == 4
```

- assert는 False일 경우 AssertionError Exception을 던진다.

### Pytest

- unittest라는 내부 모듈이 있지만, 더 직관적인 pytest 외부라이브러리를 이용함

- ```
  pip install pytest
  ```

  - pytest는 파일 이름 앞부분에 test_명시 필요

  ```python
  #test_mulitply_by_two.py
  
  def mulitply_by_two(x):
    return x * 2
  
  def test_multiply_by_two():
    assert multiply_by_two(4) == 7
  ```

  ```
  pytest
  
  
  ============================= FAILURES ==============================
  _______________________ test_mulitply_by_two ________________________
  
      def test_mulitply_by_two():
  >       assert multiply_by_two(4) == 7
  E       assert 8 == 7
  E        +  where 8 = multiply_by_two(4)
  
  test_multiply_by_two.py:5: AssertionError
  ```