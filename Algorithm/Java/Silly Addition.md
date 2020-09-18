# Silly Addtion

> For this Kata you will have to forget how to add two numbers together.
>
> The best explanation on what to do for this kata is this meme:
>
> In simple terms, our method does not like the principle of carrying over numbers and just writes down every number it calculates :-)
>
> You may assume both integers are positive integers
>
> You may assume both integers are positive integers and the result will not be bigger than `Integer.MAX_VALUE`
>
> 
>
> 이 Kata의 경우 두 개의 숫자를 더하는 방법을 잊어야합니다.
>
> 이 카타를 위해 무엇을해야하는지에 대한 가장 좋은 설명은이 mem입니다.
>
> 간단히 말해서, 우리의 방법은 숫자를 이월하는 원칙을 좋아하지 않고 계산하는 모든 숫자를 기록합니다. :-)
>
> 두 정수 모두 양의 정수라고 가정 할 수 있습니다.
>
> 두 정수 모두 양의 정수라고 가정 할 수 있으며 결과는 다음보다 크지 않을 것입니다. Integer.MAX_VALUE

## 풀이

- 1의 자리부터 계산하기 위해 stack을 이용하여 임시 저장소를 만듦
- 

```java
package com.company;

import java.util.Stack;

/*

16 + 18 = 214
=> 16
   18
   ---
   2 14
 */
public class SillyAdd {

    public static int sillyAdd(int num1, int num2){
        int answer = 0;
        String result = "";
        Stack<Integer> stack = new Stack<Integer>();

        int num1len = String.valueOf(num1).length();
        int num2len = String.valueOf(num2).length();
        int len = Math.max(num1len, num2len);
        for (int i = 0; i < len; i++) {
            //10으로 나눈 나머지 의 덧셈
            int temp = num1 % 10;
            int temp2 = num2 % 10;

            stack.push(temp + temp2);
						
						//계산한 수들을 빼고, 10으로 나눠 자릿수를 낮춤
            num1 = (num1 - temp) / 10;
            num2 = (num2 - temp2) / 10;

        }

        while(!stack.isEmpty()){
            result += stack.pop();
        }

        answer = Integer.parseInt(result);
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(sillyAdd(16, 18)); //214
        System.out.println(sillyAdd(2, 11)); //13
    }
}
```

- 다른 사람의 풀이
  - for문의 인수값을 저렇게 Q, S 따로 설정하면서 쓸 수 있는지 배움

```java
class SillyAdditon
{
  static int add(int Q,int S)
  {
    var R = "";
   
    for (;0 < Q + S; Q /= 10, S /= 10) R = Q % 10 + S % 10 + R;
    return R.length() < 1 ? 0 : Integer.parseInt(R);
  }
}
```

