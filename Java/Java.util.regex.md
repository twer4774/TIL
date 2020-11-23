# Java.util.regex

- 정규식 : 원하는 패턴의 문자열을 찾아내기 위해 미리 정의된 기호와 문자를 이용해 작성한 문자열

```java
import ajva.util.regex.*; //Pattern과 Matcher가 속한 패키지

class RegularEx{
  public static void main(String[] args) {
    String[] data = {"bat", "baby", "bonus", "cA", "ca", "co", "c.", "c0", "car,", "combat", "count", "date", "disc"};
    
    //정규식을 매개변수로 Pattern 클래스의 static메서드인 Pattern compile(String regex)을 호출하여 Pattern 인스턴스를 얻음
    Pattern p = Pattern.compile("c[a-z]*"); //c로 시작하는 소문자 영단어
    
    for(int i=0; i<data.length; i++){
      //정규식으로 비교할 대상을 매개변수로 Pattern클래스의 Matcher macher(CharSequence input)를 호출하여 Matcher인스턴스를 얻음
      Matcher m = p.matcher(data[i]);
      //Matcher인스턴스에 boolean matches()를 호출해 정규식에 부합하는지 확인
      if(m.matches(){
        System.out.println(data[i] + ", ");
    }
  }
}
         
// ca, co, car, combat, count,
```

## 자주쓰이는 패턴들 정리

| 정규식 패턴                          | 설명                                                         | 결과          |
| ------------------------------------ | ------------------------------------------------------------ | ------------- |
| c[a-z]*                              | c로 시작하는 영단어                                          | c, ca, co ... |
| c[a-z]                               | c로 시작하는 두자리 영단어                                   | ca, co,       |
| c[a-zA-Z]                            | c로 시작하는 두자리 영단어(대소문자 구분 안함)               | cA,ca,co      |
| c[a-zA-Z9-9]<br />c\w                | c로 시작하고 숫자와 영어와로 조합된 두 글자                  | cA,ca,co,c0   |
| .*                                   | 모든 문자열                                                  |               |
| c.                                   | c로 시작하는 두자리 문자열                                   |               |
| c.*                                  | c로 시작하는 모든 문자열(기호포함)                           | cA,ca,c#...   |
| c\\.                                 | c와 일치하는 문자열'.'은 패턴작성에 사용되는 문자열이므로 escape문자인 '\\'를 사용해야 함 |               |
| [b\|c].\*<br />[bc].\*<br />[b-c].\* | b또는 c로 시작하는 문자열                                    |               |
| [^b\|c]                              | b또는 c로 시작하지 않는 문자열                               |               |
| .\*a.\*                              | a를 포함하는 모든 문자열                                     |               |
| [b\|c].{2}                           | b 또는 c로 시작하는 세 자리 문자열                           | bat, car,     |

## 그룹화

- 정규식의 일부를 괄호로 나누어 묶어서 그룹화 할 수 있음
  - +, * 가뒤에 오면서 그롭화된 부분이 반복할 수 있음
  - group()을 이용해 나누어 얻음

```java
import java.util.regex.*;

class RegularEx{
  public static void main(String[] args){
    String source= "HP:011-1111-1111, HOME:02-999-9999 ";
    String pattern = "(0\\d{1,2})-(\\d{3,4})-(\\d{4})";
    
    Pattern p = Pattern.compile(pattern);
    Matcher m = p.matcher(source);
    
    int i = 0;
    while(m.find()){ //find(): 일치하는 패터이 없으면 false반환
      System.out.println(++i + ": " + m.group() + " -> " + m.group(1) 
                        + ", " + m.group(2)
                        + ", " + m.group(3));
    }
  }
}

//1: 011-1111-1111 -> 011, 1111, 1111
//2: 02-999-9999 -> 02, 999, 9999
```

- 주요패턴
  - 0\\\d{1,2} : 0으로 시작하는 최소 2자리 최대 3자리 숫자
  - \\\d{3,4}: 최소 3자리 최대 4자리 숫자
  - \\\d{4}: 4자리의 숫자

- find를 이용해 특정 위치 문자 치환

```java
class RegularEx{
  public static void main(String[] args){
    String source = "A broken hand works, but not a broken heart.";
		String pattern = "bronken";
    StringBuffer sb = new StringBuffer();
    
    Pattern p = pattern.compile(pattern);
    Matcher m = p.matcher(source);
    
    int i = 0;
    while(m.find()){
      System.out.println(++i + "번째 매칭:" + m.start() + "~" + m.end());
      //broken을 drunken으로 치환하여 sb에 저장
      m.appendReplacement(sb, "drunken");
    }
    
    m.appendTail(sb); //마지막으로 치환된 이후의 부분을 sb에 덧붙임
    System.out.println("Replacement count : " + i);
    System.out.println("result: " + sb.toString());
  }
}
  
  while()
  ...
```

