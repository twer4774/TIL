# ChoiceFormat

- 특정 범위에 속하는 값을 문자열로 변환
- 순서를 맞춰서 정의할 것

```java
import java.text.*;

class ChoiceFormatEx{
  public static void main(String[] args){
    double[] limits = {60, 70, 80, 90} //낮은 값부터 순서대로
    
    String[] grades = {"D", "C", "B", "A"};
    
    int[] scores = { 100, 95, 88, 70, 52, 60, 70 };
    
    ChoiceFormat form = new ChoiceFormat(limits, grades);
    
    for(int i=0; i < scores.length; i++){
      system.out.println(scores[i]+":"+form.format(scores[i]));
    }
  }
}

	/*
	100:A
	95:A
	88:B
	70:C
	52:D
	60:D
	70:C
	*/
```

