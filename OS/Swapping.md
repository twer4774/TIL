# Swapping

- 프로세스는 실행되기 위해 메모리 공간에 적재 되어야 함
- 프로세스는 메모리에 따라 저장공간(하드웨어, SSD)로 이동했다가 다시 메모리로 돌아올 수 있음
  - 저장공간에 프로세스를 내리는 행위 : Swap out
  - 메모리에 프로세스를 로딩하는 행위 : Swap in
- 하드디스크에 있던 것을 메모리에 다시 로딩하고 실행시켜야하므로 느릴 수 있는 단점
  - 하지만, 부족한 메모리 공간에서 더 많은 프로세스를 실행 시킬 수 있어서 이용함
