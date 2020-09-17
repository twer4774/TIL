# Spin Words - 5글자 뒤집기

> Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
>
> Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
>
> 하나 이상의 단어의 문자열을 받아 동일한 문자열을 반환하지만 5 개 이상의 문자 단어를 모두 뒤집는 함수를 작성하십시오 (이 Kata의 이름과 동일). 전달 된 문자열은 문자와 공백으로 만 구성됩니다.
> 공백은 두 개 이상의 단어가있는 경우에만 포함됩니다.
>
> 예 : spinWords ( "Hey fellow warriors") => returns "Hey wollef sroirraw"
>     spinWords ( "This is a test") => returns "This is a test"
>     spinWords ( "This is another test") => returns "This rehtona test"

## 풀이

```java
public class SpinWords {

  public String spinWords(String sentence) {
    //TODO: Code stuff here
    String answer = "";

    String[] st = sentence.split(" ");
    for (int i = 0; i < st.length; i++){
        if(st[i].length() > 4){
            String temp = new StringBuffer(st[i]).reverse().toString();
            st[i] = temp;
        }
       if(i == st.length-1){
                answer += st[i];
        } else {
            answer += st[i] + " ";
        }
    }
   
    return answer;
  }
}
```

- 다른사람의 풀이
  - 나는 if로 마지막 순회문자 i를 확인했는데 join으로 해결
  - 또 다른 방법으론 map과 collect를 이용

```java
 for (int i=0; i<words.length; i++) {
      if (words[i].length() >= 5) {
        words[i] = new StringBuilder(words[i]).reverse().toString();
      }
    }
    return String.join(" ",words);
  }
//--------------------------------------
public String spinWords(String sentence) {
    return Arrays.stream(sentence.split(" "))
                 .map(i -> i.length() > 4 ? new StringBuilder(i).reverse().toString() : i)
                 .collect(Collectors.joining(" "));
  }
```

