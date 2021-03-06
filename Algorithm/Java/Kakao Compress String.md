# Kakao Compress String - 문자열 압축

> ###### 문제 설명
>
> 데이터 처리 전문가가 되고 싶은 **어피치**는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다. 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.
> 간단한 예로 aabbaccc의 경우 2a2ba3c(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데, 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 예를 들면, abcabcdede와 같은 문자열은 전혀 압축되지 않습니다. 어피치는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.
>
> 예를 들어, ababcdcdababcdcd의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 2ab2cd2ab2cd로 표현할 수 있습니다. 다른 방법으로 8개 단위로 잘라서 압축한다면 2ababcdcd로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.
>
> 다른 예로, abcabcdede와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 abcabc2de가 되지만, 3개 단위로 자른다면 2abcdede가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다. 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.
>
> 압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.
>
> ### 제한사항
>
> - s의 길이는 1 이상 1,000 이하입니다.
> - s는 알파벳 소문자로만 이루어져 있습니다.
>
> ##### 입출력 예
>
> | s                            | result |
> | ---------------------------- | ------ |
> | `"aabbaccc"`                 | 7      |
> | `"ababcdcdababcdcd"`         | 9      |
> | `"abcabcdede"`               | 8      |
> | `"abcabcabcabcdededededede"` | 14     |
> | `"xababcdcdababcdcd"`        | 17     |
>
> ### 입출력 예에 대한 설명
>
> **입출력 예 #1**
>
> 문자열을 1개 단위로 잘라 압축했을 때 가장 짧습니다.
>
> **입출력 예 #2**
>
> 문자열을 8개 단위로 잘라 압축했을 때 가장 짧습니다.
>
> **입출력 예 #3**
>
> 문자열을 3개 단위로 잘라 압축했을 때 가장 짧습니다.
>
> **입출력 예 #4**
>
> 문자열을 2개 단위로 자르면 abcabcabcabc6de 가 됩니다.
> 문자열을 3개 단위로 자르면 4abcdededededede 가 됩니다.
> 문자열을 4개 단위로 자르면 abcabcabcabc3dede 가 됩니다.
> 문자열을 6개 단위로 자를 경우 2abcabc2dedede가 되며, 이때의 길이가 14로 가장 짧습니다.
>
> **입출력 예 #5**
>
> 문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.
> 따라서 주어진 문자열을 x / ababcdcd / ababcdcd 로 자르는 것은 불가능 합니다.
> 이 경우 어떻게 문자열을 잘라도 압축되지 않으므로 가장 짧은 길이는 17이 됩니다.

## 풀이

- 처음에는 거꾸로 가장 긴 문자열(s.length()/2)부터 줄여가며 찾는 방법을 시도했으나, 실패
  - aaaaaaa  같은 문자열이라면 제일 긴 3으로 문자열을 나누면 2aaa가 정답으로 나올 확률이 있음. 답은 6a 로 나와야함
  - 거꾸로 0번째까지 가면서 최소 숫자 구하는 방식을 이용하면 되지만, 0부터 시작하는 방법이 더 구현하기 편함
- 비교 기준문자열(std)과 비교할 문자열(compare)을 s.length()를 넘느냐에 따라 선언을 달리해주어야 함
- 압축 길이를 저장하는 pre와 임시로 문자열을 저장하는 temp의 초기화를 잊지 말아야 함
- 의외로 마지막 xababcdcdababcdcd의 처리는 신경 쓸 필요가 없었음(i=0부터 비교하니까)
- 마지막으로 주의할 점
  - 테스트케이스 5번에서 에러 - 만약 s가 a라면? 문자의 길이가 1이라면 바로 문자열의 길이를 리턴해주면 됨

```java
class Solution {
    public int solution(String s) {
        int answer = 0;
        int min = 1000; //s의 최대 길이
        if(s.length() == 1){
            return 1;
        }
        
        String std = ""; //비교 기준 문자열
        String compare = ""; //비교할 문자열
        int pre = 1; //압축횟수
        String temp = ""; //비교 후 임시저장할 문자열
        
        //1부터 최대로 자를 수 있는 길이는 s.length()/2
        for(int n=1; n <= s.length()/2; n++){
            
            //비교 기준 문자열 반복문
            for(int i=0; i < s.length(); i+=n){
                
                if(i+n >= s.length()){
                    std = s.substring(i, s.length());
                } else {
                    std = s.substring(i, i+n);
                }
                
                
                //비교할 문자열 반복문
                //시작지점 = i + n(i: 기준문자열의 위치, n: 자르는 길이)
                for(int j=i+n; j < s.length(); j+=n){
                    
                    if(j+n >= s.length()){
                        compare = s.substring(j, s.length());
                    } else {
                        compare = s.substring(j, j+n);
                    }
                    
                    //두 문자가 같다면
                    if(std.equals(compare)){
                        pre++; //압축횟수를 1 증가시키고
                        i = j; //기준 문자열(i)의 위치를 j로 변환
                    } else{
                        break;
                    }
                    
                }
                
                //temp 만들기
                if(pre != 1){
                    temp += pre + std;
                    pre = 1; //pre 초기화
                } else {
                    temp += std;
                }
            }    
        
            //최소 문자의 길이 저장
            min = Math.min(min, temp.length());
            temp = ""; //temp 초기화
        }
        
        //최종적으로 가장 작은 문자열의 길이(min)의 값을 대입하여 출력
        answer = min;
        return answer;
    }
}
```

