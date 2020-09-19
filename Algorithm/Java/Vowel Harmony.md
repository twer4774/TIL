# Vowel Harmony(모음 하모니)

> [Vowel harmony](https://en.wikipedia.org/wiki/Vowel_harmony) is a phenomenon in some languages. It means that "A vowel or vowels in a word are changed to sound the same (thus "in harmony.")" ([wikipedia](https://en.wikipedia.org/wiki/Vowel_harmony#Hungarian)). This kata is based on [vowel harmony in Hungarian](https://en.wikipedia.org/wiki/Vowel_harmony#Hungarian).
>
> ### Task:
>
> Your goal is to create a function `dative()` (`Dative()` in C#) which returns the valid form of a valid Hungarian word `w` in [dative case](http://www.hungarianreference.com/Nouns/nak-nek-dative.aspx) i. e. append the correct suffix `nek` or `nak` to the word `w` based on vowel harmony rules.
>
> ### Vowel Harmony Rules (simplified)
>
> When the last vowel in the word is
>
> 1. a *front vowel* (`e, é, i, í, ö, ő, ü, ű`) the suffix is `-nek`
> 2. a *back vowel* (`a, á, o, ó, u, ú`) the suffix is `-nak`
>
> ### Examples:
>
> ```java
> Kata.dative("ablak") == "ablaknak"
> Kata.dative("szék") == "széknek"
> Kata.dative("otthon") == "otthonnak"
> ```
>
> ### Preconditions:
>
> 1. To keep it simple: All words end with a consonant :)
> 2. All strings are unicode strings.
> 3. There are no grammatical exceptions in the tests.



> 모음 조화 는 일부 언어의 현상입니다. 이것은 "단어의 모음 또는 모음이 같은 소리로 변경됨 (따라서"조화 ")"( wikipedia )을 의미합니다.
> 이 카타는 헝가리어 모음 조화를 기반으로 합니다.
>
> 직무:
> 목표는 dative case 에서 유효한 헝가리어 단어의 유효한 형식을 반환 하는 함수 dative()( Dative()C #에서) 를 만드는 것입니다.
> 즉, 올바른 접미사를 추가 하거나 모음 조화 규칙에 따라 단어에 추가합니다 .wneknakw
>
> 모음 조화 규칙 (간체)
> 단어의 마지막 모음이
>
> 앞의 모음 ( e, é, i, í, ö, ő, ü, ű) 접미사 인-nek
> 이면 모음 ( a, á, o, ó, u, ú) 접미사 인-nak
>
> 예 :
> Kata.dative("ablak") == "ablaknak"
> Kata.dative("szék") == "széknek"
> Kata.dative("otthon") == "otthonnak"
>
> 전제 조건 :
> 간단하게하기 위해 : 모든 단어는 자음으로 끝납니다. :)
> 모든 문자열은 유니 코드 문자열입니다.
> 테스트에는 문법적 예외가 없습니다.

## 풀이

- 내풀이

```java
package com.company;

public class VowelHarmony {

    private static char[] nek = { 'e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű'};
    private static char[] nak = {'a', 'á', 'o', 'ó', 'u', 'ú'};

    public static String dative(String word) {

        char[] temp = word.toCharArray();
        //nek과 nak에 있는 문자의 위치 저장, 반복문을 돌다가 더 빠른것으로 갱신
        int max = 0;
        String suffix = "";
        //word의 끝 문자부터 첫번째 문자로 이동
        for (int i = temp.length-1; i > 0; i--) {


            //nek, nak의 문자가 들어있는지 확인 -> 어떻게??
            for (int j = 0; j < nek.length; j++) {
                if(nek[j] == temp[i]){
                    max = Math.max(i, max);
                }
            }

            for (int j = 0; j < nak.length; j++) {
                if(nak[j] == temp[i]){
                    max = Math.max(i, max);
                }
            }

        }

        System.out.println("max : " + temp[max]);
        //nek과 nak 중 맞는 접미사를 붙여서 출력
        for (char c : nek){
            if(c == temp[max]){
                return word + "nek";
            }
        }

        return word + "nak";
    }

    public static void main(String[] args) {

        System.out.println(dative("ablak"));
        System.out.println(dative("szék"));
        System.out.println(dative("otthon"));
        System.out.println(dative("virágn"));
    }
}
```

- 다른 사람의 풀이

```java
public class Kata {
    public static String dative(String word) {
        String w1 = word.replaceAll("[eéiíöőüű]","1");
        String w2 = word.replaceAll("[aáoóuú]","2");
        return w1.lastIndexOf("1")>w2.lastIndexOf("2")? word+"nek":word+"nak";
    }
}
```

```java
public class Kata {
    static final String w1 = "eéiíöőüű";
    static final String w2 = "aáoóuú";
    
    public static String dative(String word) {
      for (int i = word.length() - 1; i >= 0; i--)
      {
        if (w1.indexOf(word.charAt(i)) >= 0) return word + "nek";
        if (w2.indexOf(word.charAt(i)) >= 0) return word + "nak";
      }
      return word;
    }
}
```

- 내가 풀고 싶었던 풀이방법

```java
public class Kata {
  
  private static String NEK = "eéiíöőüű";
  private static String NAK = "aáoóuú";
  
  public static String dative(String word) {
    for (char c : new StringBuilder(word).reverse().toString().toCharArray()) {
      if (NEK.contains(""+c)) return word + "nek";
      if (NAK.contains(""+c)) return word + "nak";
    }
    return word;
  }

}
```

