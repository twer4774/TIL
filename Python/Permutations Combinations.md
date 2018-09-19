# 순열과 조합

- 1, 2, 3의 숫자에서 두장을 꺼내는 경우 => 12, 13, 21, 23, 31, 32

- 'A', 'B', 'C'로 만들수 있는 경우의 수 => 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'

  ```python
  '''
  숫자를 담은 일차원 리스트, mylist에 대해 mylist의 원소로 이루어진 모든 순열을 사전순으로 리턴하는 함수 solution을 완성해주세요.
  mylist	output
  [2, 1]	[[1, 2], [2, 1]]
  [1, 2, 3]	[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
  '''
  import itertools
  def solution(mylist):
      answer = [[]]
      answer = list(map(list, itertools.permutations(sorted(mylist))))
      return answer
  
  #for문을 이용해 순열만들기
  def permute(l):
      n = len(l)
      result = []
      c = n * [0]
  
      result.append(l)
  
      i = 0;
      while i < n:
          if c[i] < i:
              if i % 2 == 0:
                  tmp = l[0]
                  l[0] = l[i]
                  l[i] = tmp
  
              else:
  
                  tmp = l[c[i]]
                  l[c[i]] = l[i]
                  l[i] = tmp
  
              result.append(l)
              c[i] += 1
              i = 0
          else:
              c[i] = 0
              i += 1
  
      return result
  
  l = [1, 2, 3, 4, 5]
  print(permute(l))
  
  
  #itertools.permutation이용
  import itertools
  
  pool = ['A', 'B', 'C']
  #.join은 문자열을 원하는 기호를 이용해 붙일때 이용하는 함수
  print(list(map(''.join, itertools.permutations(pool)))) #3개의 원소로 순열 만들기
  print(list(map(''.join, itertools.permutations(pool, 2)))) #2개의 원소로 순열 만들기
  
  #조합은 itertools.combinations를 이용한다.
  ```

   