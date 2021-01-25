# [Greedy] BigNumber

> - 큰 수 만들기
>
> ###### 문제 설명
>
> 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
>
> 예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.
>
> 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.
>
> ##### 제한 조건
>
> - number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
> - k는 1 이상 `number의 자릿수` 미만인 자연수입니다.
>
> ##### 입출력 예
>
> | number     | k    | return |
> | ---------- | ---- | ------ |
> | 1924       | 2    | 94     |
> | 1231234    | 3    | 3234   |
> | 4177252841 | 4    | 775841 |

## 다른 사람의 풀이

- 못 풀어서 다른 사람의 풀이 이용
- 풀이
  - 입력된 숫자가 모두 0일 경우 예외처리를 한다. `if(number.charAt(0) == '0') return "0"`
  - 각 자리 숫자 하나 하나 뽑을 때마다 그때의 최대값을 선택해야 한다. 가령, 예제에서 10의 자리 숫자로 9를 선택하고 1의 자리 숫자로 그 다음으로 큰 수 4를 선택해야 정답이 나온다.
  - 인덱스가 0부터 시작할 때, k개의 숫자를 뺏을 때 최대 숫자는 적어도 0번째부터 k번째 숫자 중에 나와야 한다. (예제에 따르면, 1부터 2까지 중 숫자 하나를 골라야 마지막 숫자 4를 골랐을 때 답변의 총 길이가 2가 된다. 만약 첫번째 숫자로 4를 고르면 그 다음 숫자를 고를 수 없으므로 정답이 될 수 없다.따라서 범위는 `int i = 0; i < number.length() - k; i++`이다.
  - 지금 위치부터 그 다음 숫자를 뽑을 때까지 과정 역시 위와 같다. 범위는 `int j = idx; j <= k + i; j++`이다.

```java
class Solution {
    public String solution(String number, int k) {
        int idx = 0;
        char max;
	StringBuilder answer = new StringBuilder();

	if(number.charAt(0) == '0') return "0";
      
	for(int i = 0; i < number.length() - k; i++) {
		max = '0';
		for(int j = idx; j <= k + i; j++) {
      if(max < number.charAt(j)) {
        max = number.charAt(j); 
        idx = j + 1;
      }
		}//for			
		answer.append(max);
	}//for
      return answer.toString(); 
   }
}
```

## 또 다른 풀이

- Stack 이용

```java
import java.util.Stack;
class Solution {
    public String solution(String number, int k) {
        char[] result = new char[number.length() - k];
        Stack<Character> stack = new Stack<>();

        for (int i=0; i<number.length(); i++) {
            char c = number.charAt(i);
          //stack이 비었으면 실행이 안되고 넘어감
          //stack에 값이 있으면, 가장 위의 값과 c를 비교하여 큰 숫자를 찾음
            while (!stack.isEmpty() && stack.peek() < c && k-- > 0) {
                stack.pop();
            }
          //stack에 값을 넣음
            stack.push(c);
        }
        for (int i=0; i<result.length; i++) {
            result[i] = stack.get(i);
        }
        return new String(result);
    }
}
```

