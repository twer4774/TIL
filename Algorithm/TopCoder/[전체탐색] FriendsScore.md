# [전체탐색] FriendsScore

>  * 친구 여부를 나타내는 배열이 주어짐
>  * 일단, 서로 친구라면 친구
>  * C가 A와 B와는 친구인데, A,B는 서로 친구가 아니여도 A,B는 친구로 간주
>  * 가장 인기가 많은 사람의 친구수를 리턴

## 내 풀이

- 직접 친구와 간접 친구를 나눈다.
  - 직접 친구 : A, B가 서로 Y 값을 가짐
  - 간접 친구 : A와 C가 Y / B와 C가 Y  => A와 B는 친구
- **주의 사항 : 자기 자신은 친구로 세지 않는다.**

```java
public class FriendScore {

    static String[] friends1 = {"NNN", "NNN", "NNN"}; //0
    static String[] friends2 = {"NYY", "YNY", "YYN"}; //2 모든 사람이 2명의 전체 친구가 있음
    static String[] friends3 = {"NYNNN", "YNYNN", "NYNYN", "NNYNY", "NNNYN"}; //4


    public static int heighestScore(String[] friends){
        int ans = 0;
        int n = friends[0].length();

        for (int i = 0; i < n; i++) {
            int cnt = 0;

            for (int j = 0; j < n; j++) {
                //자기 자신은 친구로 세지 않음
                if(i == j) continue;

                //i와 j가 둘다 Y이면 친구(직접친구)
                if(friends[i].charAt(j) == 'Y'){
                    cnt++;
                } else {
                    for (int k = 0; k < n; k++) {
                        //j와 k가 친구이고, k가 i와 친구이면 => i,j는 친구(간접친구)
                        if(friends[j].charAt(k) == 'Y' && friends[k].charAt(i) == 'Y'){
                            cnt++;
                            break;
                        }
                    }
                }
            }

            ans = Math.max(ans, cnt);
        }

        return ans;
    }

    public static void main(String[] args) {
        System.out.println(heighestScore(friends1));
        System.out.println(heighestScore(friends2));
        System.out.println(heighestScore(friends3));
    }
}

/*
0
2
4
*/
```

