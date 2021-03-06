# 디버깅

- 컴퓨터 프로그램의 정확성이나 논리적인 오류(버그)를 검출하여 제거하는 과정
- 테스트 상의 체크, 기계를 사용하는 테스트, 실제 데이터를 사용해 테스트하는 법
- Xcode에서는 코드 중에 중단점을 설정함으로써 변수의 내용과 처리 흐름을 확인하면서 디버깅 할 수 있음

## 스텝 실행해서 동작 확인

- 애플리케이션을 1줄씩 실행해서 동작 확인
- 디버깅에서 주로 이용하는 기능은 실행 계속, 스텝 오버
- 실행 중인 코드에 있는 메소드나 함수의 안팎으로 이동해서 동작을 확인하고 싶을 때는 스텝 인과 스텝 아웃을 이용한다.

| 종류                   | 설명                                                         |
| ---------------------- | ------------------------------------------------------------ |
| 실행 계속(continue, c) | 실행을 다시 시작해서 다음의 유효한 중단점까지 실행           |
| 스텝 오버(next, n)     | 현재 표시되고 있는 코드에 따라 1줄씩 실행                    |
| 스텝 인(step, s)       | 현재 표시되고 있는 코드에 메소드나 함수가 나타나면 그 내부로 들어가 1줄씩 실행 |
| 스텝 아웃(finish)      | 현재 표시되고 있는 코드의 메소드나 함수의 호출 장소로 돌아와서 1줄씩 실행 |

## LLDB를 이용한 디버깅 방법

- LLDB: Xcode에 기본으로 내장되어있는 디버거
- 기존에 사용되던 gdb보다 많은 유용한 기능을 가짐

### 기본명령

#### 값 확인하기

- 가장 기본적으로 많이 사용하는 명령어는 변수값을 확인할 때 사용하는 p와 po 명령어(gdb 명령어)
- LLDB에서는 expr

#### 흐름 제어하기

- c 명령어를 통해 브레이크 포인트를 떠나 계속 진행 가능
- 다음 브레이크 포인트를 만날때 까지 실행 됨

### 

### 조건에 따른 액션 지정

- 특정 브레이크포인트에 진입했을 때 멈추지 않고 특정 명령을 수행 후 바로 진행하는 액션들을 지정 함
- br co a  => breakpoint command add

```
//현재 멈춰있는 브레이크포인트에 다음번에 진입시 등록한 명령어가 자동으로 수행됨
br co a
> p self.authToken //self.authToken 값 확인
> bt			   //backtrace 출력 
> c				   //브레이크 없이 넘어가기
> DONE
```

### 특정 변수 값 변화 모니터링하기

- Watchpoint 명령어를 이용하면 특정 변수값이 바뀔 때 break를 걸리게 할 수 있다.
- 모니터링을 하는데 많은 CPU 자원을 소모하기 때문에 성능상의 문제로 모니터링 할 수 있는 변수의 갯수는 Intel 4개, ARM 2개로 제한되어 있다.

```
w s v self->myVariable
watchpoint set variable self->myVariable
```



### 실행중에 값 바꾸기/함수 호출하기

- 프로그램이 실행중에 특정 상황을 만들어내지 못해서 디버깅이 어려운 경우, 실행중에 메모리상의 값을 바꾸거나, 수동으로 직접 호출하는 것이 필요한 경우들이 많이 있음
- LLDB에서는 실행중에 브레이크가 걸린 상태에서 특정코드를 on-the-fly로 실행하거나 메모리상의 값을 변경하는것이 가능
- 객체내부의 어디낙에서 브레이크가 걸려 있을 때 다음 명령어를 이용하면 해당 코드를 실행하는 것이 가능함

```
e -i false - [self thisIsCalledByHand]
```

