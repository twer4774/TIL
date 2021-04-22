# Mock과 Mocktio - @InjectMocks

Mock과 Spy의 주입을 허용합니다.

Mockito에서 가짜 객체를 주입하는 방식은 생성자 주입방식, Setter 주입방식, Field 주입방식이 있습니다.(DI와 동일)

### 생성자 주입방식(Constructor Injection)

생성자를 이용하여 가짜 객체를 주입하면 Mockito에서는 다른 주입방식을 시도하지 않습니다.

=> 매개변수가 있는 생성자가 있는 경우, 개체를 손상시키지 않기로 Mockito에서 결정

생성자 ConstructService를 만들어서 객체를 주입합니다.

```java
public class ConstructService {

    private RegionService regionService;

    public ConstructService(RegionService regionService) {
        this.regionService = regionService;
    }
  
  //메소드 정의
    public List<Region> getRegions(){
        return regionService.getRegions();
    }
}
```

### Setter 주입방식

Setter를 만들어서 객체를 주입합니다.

```java
public class SetterService {

    private RegionService regionService;

    public void setRegionService(RegionService regionService) {
        this.regionService = regionService;
    }
  
  //메소드 정의
    public List<Region> getRegions(){
        return regionService.getRegions();
    }
}
```

### Field 주입방식

객체를 사용할 때 필드에서 주입합니다.

```java
public class FieldService{
  private RegionService regionService;
  
  //메소드 정의
    public List<Region> getRegions(){
        return regionService.getRegions();
    }
}
```

### 세가지 주입 방식의 사용

```java
class BaseTestCase{
    private AutoCloseable autoCloseable;

    @BeforeEach
    void setUp(){
        MockitoAnnotations.openMocks(this);
    }

    @AfterEach
    void closeMock() throws Exception {
        MockitoAnnotations.openMocks(this).close();
    }
}
public class MockTest extends BaseTestCase{

		
    @Mock
    private RegionService regionService;

    @InjectMocks
    private ConstructorService constructorServiceInjectionMock;

    @InjectMocks
    private SetterService setterServiceInjectionMocks;

    @InjectMocks
    private FieldService fieldServiceInjectionMocks;

    @Test
    void constructorInjectionTest(){

        when(constructorServiceInjectionMock.getRegions()).thenReturn(regions);

        assertEquals(constructorServiceInjectionMock.getRegions().get(0).getName(), "Seoul");

    }

    @Test
    void setterInjectionTest(){
        when(setterServiceInjectionMocks.getRegions()).thenReturn(regions);

        assertEquals(setterServiceInjectionMocks.getRegions().get(0).getName(), "Seoul");
    }

    @Test
    void fieldInjectionTest(){
        when(fieldServiceInjectionMocks.getRegions()).thenReturn(regions);

        assertEquals(fieldServiceInjectionMocks.getRegions().get(0).getName(), "Seoul");
    }
}
```

