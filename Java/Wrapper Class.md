# Wrapper Class

- 자바의 8개의 기본형은 객체로 다루지 않음
  - 자바가 완전히 객체지향이 아니라는 소리를 듣는 이유
- 기본형 변수도 객체로 다뤄야하는 경우 wrapper 클래스로 기본형을 객체로 변환함

| 기본형  | 래퍼클래스 | 생성자                                                       | 활용                                                         |
| ------- | ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| boolean | Boolean    | Boolean (boolean value)<br />Boolean (String s)              | Boolean b = new Boolean(true);<br />Boolean b2 = new Boolean("true"); |
| char    | Character  | Character (char value)                                       | Character c = new Character('a');                            |
| byte    | Byte       | Byte (byte value)<br />Byte (String s)                       | Bytre b = new Byte(10);<br />Byte b2 = new Byte("10");       |
| short   | Short      | Short (short value)                                          | Short s = new Short(10);                                     |
| int     | Integer    | Integer (int value)<br />Integer (String s)                  | Integer i = new Integer(100);<br />Integer i2 = new Integer("100"); |
| long    | Long       | Long (long value)<br />Long (String s)                       | Long l = new Long(100);<br />Long l2 = new Long("100");      |
| float   | Float      | Float (double value)<br />Float (float value)<br />Float (String s) | Float f = new Float(1.0);<br />Float f2 = new Float(1.0f);<br />Float f3 = new Float("1.0f"); |
| double  | Double     | Double (double value)<br />Double (String s)                 | Double d = new Double(1.0);<br />Double d2 = new Double("1.0"); |

## 문자열을 숫자로 변환하기

```java
int i = new Integer("100").intValue(); 
int i2 = Integer.parseInt("100"); //주로 사용. 반환값이 기본형
Integer i3 = Integer.valueOf("100"); //반환값이 래퍼클래스 타입
```

