# SpringBoot Property로 Key관리

### Resources에 application-serviceKey.properties 생성

.gitignore에 추가해놓을 것

```properties
#application-serviceKey.properties
api.datago.serviceKey=HEwfww
```

### ServiceKey.java 생성

- Component로 빈 등록
- 주의사항
  - @Value는 import factory.annotation.Value (Lombok 아님)
  - PropertySource 설정

```java
import lombok.Getter;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.PropertySource;
import org.springframework.stereotype.Component;

@Component
@Getter
@PropertySource("classpath:application-serviceKey.properties")
public class ServiceKey {

    @Value("${api.datago.serviceKey}")
    private String dataoServiceKey;
}

```

### 간단한 RestController

```java
@RestController
@RequestMapping("/test")
public class TestController {

    @Autowired
    private ServiceKey serviceKey;

    @GetMapping("")
    public void read(){

        System.out.println(serviceKey.getDataoServiceKey());
    }
}
```

