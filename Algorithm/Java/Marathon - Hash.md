# 완주하지 못한 선수(Marathon) - Hash

> ###### 문제 설명
>
> 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
>
> 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
>
> ##### 제한사항
>
> - 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
> - completion의 길이는 participant의 길이보다 1 작습니다.
> - 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
> - 참가자 중에는 동명이인이 있을 수 있습니다.
>
> ##### 입출력 예
>
> | participant                             | completion                       | return |
> | --------------------------------------- | -------------------------------- | ------ |
> | [leo, kiki, eden]                       | [eden, kiki]                     | leo    |
> | [marina, josipa, nikola, vinko, filipa] | [josipa, filipa, marina, nikola] | vinko  |
> | [mislav, stanko, mislav, ana]           | [stanko, ana, mislav]            | mislav |
>
> ##### 입출력 예 설명
>
> 예제 #1
> leo는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
>
> 예제 #2
> vinko는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
>
> 예제 #3
> mislav는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.

## 풀이

### Hash로 풀기

- <String, Integer> 해시맵을 이용한다. <이름, 인원수>
- 해시맵에 participant와 completion을 넣어준다.
  - participant를 넣을때는 인원수를 1씩 늘린다.
  - completion을 넣을때는 인원수를 1씩 뺀다.
  - 최종적으로 1의 value(인원수)값을 갖는 key(이름)가 완주하지 못한 선수가 된다.
- 배운점
  - hash
  - hash.getOrDefault(key, defaultValue) => 굳이 쓸필요는 없지만 if문을 안써도 되므로 가독성과 효율이 높아질듯 함 

```java
import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
       String answer = "";
        //<이름, 인원수>형식으로 저장
        HashMap<String, Integer> hash = new HashMap<>();

        //paticipant의 값 넣기
        //getOrDefault(key, defaultValue) => key값이 있으면 해당 value값, 아니면 defaultValue값
        for(String player: participant){
            //hash에 값을 넣을때 인원수를 하나씩 늘려주기 위해 +1을 해준다.
            hash.put(player, hash.getOrDefault(player, 0) + 1);
        }

        //completion의 값 넣기
        for(String player: completion){
            //hash에 값을 넣을때 인원수를 하나씩 빼주기 위해 -1을 해준다.
            hash.put(player, hash.getOrDefault(player, 0) - 1);
        }

        //hash의 value가 1인 key값이 완주하지 못한 선수가 된다.
        for(String player: hash.keySet()){
            if(hash.get(player) == 1){
                answer = player;
            }
        }
        
        return answer;
    }
}
```

### 정렬과 배열로 풀기

- 배열을 정렬하고 하나씩 순서대로 비교하며 일치하지 않는 값을 출력

```java
import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);
        Arrays.sort(completion);
        int i;
        for ( i=0; i<completion.length; i++){

            if (!participant[i].equals(completion[i])){
                return participant[i];
            }
        }
        return participant[i];
    }
}
```

