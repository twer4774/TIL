# Mock과 Mocktio - @Mock @MockBean 

Mockito Document : https://javadoc.io/doc/org.mockito/mockito-core/latest/org/mockito/Mockito.html

참고 코드 : https://github.com/journaldev/journaldev/tree/master/Mockito-Examples

## Mock이란?

가짜 객체라고 불리며, 행위를 검증하기 위해 사용되는 객체입니다.

### 가짜 객체를 만드는 이유

실제 객체를 만드는데 드는 시간을 절약하기 위해서

의존성의 연결고리가 많이 연결된 경우, 구현의 복잡함을 피하기 위해서

## Spring Boot Test에서 Mock 사용(테스트 더블)

### 테스트 더블이란?

테스트를 진행하기 어려운 경우 테스트를 대신 진행할 수 있게 만드는 객체를 말합니다.

Mock 객체의 상위호환으로 생각하시면 됩니다.



### Spring Boot Test에서의 테스트 더블 => Mockito

Mock 객체를 만드는 방법을 통일하여 사용방법이 단순합니다. 

Mockito는 다음과 같은 동작들을 할 수 있습니다.

- Mock만들기(CreateMock)

- Mock의 동작 지정(Stub)
- Mock의 사용(Excercise)
- 검증(Verify)

```java
import static org.mockito.Mockito.*;

public class MockTest {

    @Test
    public void mockTest(){
        // Mock 만들기
        List mockedList = mock(List.class);

        //Mock의 사용
        mockedList.add("first");

        // Mock의 동작 지정
        when(mockedList.get(0)).thenReturn("first");

        //검증
        verify(mockedList).add("first");
    }

}
```



## @Mock과 @MockBean

Mock 객체를 선언할때 쓰이는 어노테이션

Spring의 ApplicationContext에 Mock 객체들을 넣어줍니다.

- @Mock 
  - import org.mockito.Mock

- @MockBean
  - import org.springframework.boot.test.mock.mockito.MockBean => 스프링 테스트에서 지원

=> Spring Boot Container가 테스트 시에 필요하고, Bean이 Container에 존재한다면 @MockBean을 사용하고 아닌 경우에는 @Mock을 사용합니다.

### @Mock

필드명에 @Mock을 선언해주어 에러검증을 더 쉽게하고, 해당 필드가 Mock객체임을 더 명확하게 표시합니다.

Serivce 레이어를 테스트할 때, Repository를 가짜 객체로 만드는 용도로 사용될 수 있습니다.(3 번째 예제)

일단, 아래의 예제들에서 공통으로 사용되는 부분을 클래스로 정의하여 상속받아 사용하겠습니다.

```java
public class BaseTestCase{
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
```

```java
public class MockTest {

    //Mock 만들기
    @Mock
    List mockedList;
    
    @BeforeEach
    void setUp(){
        //중요! : base class 또는 test runner가 필요합니다. 여기서는 MockTest를 넣어줍니다.
        //initMocks()에서 openMocks()로 변경되었습니다.
      	//역할 : @Mock 어노테이션 필드의 초기화
        MockitoAnnotations.openMocks(this);
    }

    @Test
    public void mockTest(){
        // Mock 만들기
//        List mockedList = mock(List.class);


        //Mock의 사용
        mockedList.add("first");

        // Mock의 동작 지정
        when(mockedList.get(0)).thenReturn("first");


        //검증
        verify(mockedList).add("first");
    }

}
// ========= Mock객체에 대한 간단한 예제 ==========
// 클래스를 사용하기 위해서는 new 객체명 등으로 인스턴스 객체를 만들어야 합니다.
// @Mock은 가짜 객체를 만들어 주기 때문에 초기화를 해주지 않아도 에러를 발생하지 않습니다.
public class MockTest extends BaseTestCase{
  
  	@Mock  //@Mock이 없는 경우 NullPointerException 에러 발생
    private Region region;

    @Test
    void regionTest(){
        region.setName("Busan");
        System.out.println(region.getName());
    }
}

// ==================== 다른 예제 =========================

public class MockTest extends BaseTestCase{
  	//1. RegionRepository를 Mock 객체로 만듭니다.
    @Mock
    private RegionRepository regionRepository;

    private RegionService regionService;

    @Test
    void regionServiceTest(){
      	//2. RegionRepository를 RegionService를 생성할 때 넣습니다.
      	//RegionRepository는 인스턴스 객체를 생성하지 않았는데, @Mock으로 인해 객체가 생성되어 다음과 같이 넣을 수 있게 됩니다.
        regionService = new RegionService(regionRepository);
        regionService.getRegions();
    }
}
```

### @MockBean

@WebMvcTest를 이용한 테스트에서 사용할 수 있습니다.

@WebMvcTest는 Controller를 테스트할 때 주로 이용되며, 단일 클래스의 테스트를 진행하므로 @MockBean을 통해 가짜 객체를 만들어 줍니다. => Controller객체까지만 생성되고 Serivce 객체는 생성하지 않습니다.

**@MockBean은 위와 같이 Bean 컨테이너에 객체(Service)가 있어야 다른 객체(Controller)와 협력할 수 있는데, 객체를 만들 수 없는 경우(@WebMvcTest)에 사용할 수 있습니다.**

```java
@WebMvcTest(RegionController.class)
public class MockTest extends BaseTestCase{
   @Autowired
   private MockMvc mvc;
  
   @MockBean
    private RegionService regionService;

    @Test
    void getRegions() throws Exception {
        List<Region> regions = new ArrayList<>();
        regions.add(Region.builder()
                .name("Seoul")
                .build());

        given(regionService.getRegions()).willReturn(regions);

        mvc.perform(get("/regions")).andExpect(status().isOk());
    }
}
```



