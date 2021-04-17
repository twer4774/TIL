# Mock과 Mocktio - @Spy @SpyBean

Mockito Document : https://javadoc.io/doc/org.mockito/mockito-core/latest/org/mockito/Mockito.html

참고 코드 

- https://github.com/journaldev/journaldev/tree/master/Mockito-Examples

- https://cobbybb.tistory.com/16

## Spy

#### Spy란?

실제 객체의 스파이를 생성하여 실제 객체의 메소드를 호출 할 수 있게 합니다.

#### Spy 사용

```java
public class SpyTest{
    @Test
    void spyTest(){
        List list = new LinkedList();
        List spy = spy(list);
	
      when(spy.size()).thenReturn(100);
      
      //실제 객체의 메소드를 사용
        spy.add("one");
        spy.add("two");

        System.out.println(spy.size());

        verify(spy).add("one");
        verify(spy).add("two");
    }
}
//100
```

when을 사용하다 보면 spy의 동작이 불가능할 경우가 있습니다. 때문에 항상 doReturn, Answer, Throw() 등을 같이 사용하는 것이 좋습니다.

```java
@Test
void spyTest(){
  List list = new LinkedList();
  List spy = spy(list);

  //실제 메소드 get(0) 호출 시 IndexOutOfBoundsException 발생 => 리스트가 비어있기 때문
  when(spy.get(0)).thenReturn("foo");

  //doReturn으로 예외를 발생하지 않도록 조작
  doReturn("foo").when(spy).get(0);
}
```



## @Spy @SpyBean

#### @Spy

필드인스턴에 어노테이션으로 정의하여 쉽고 간단하게 Spy를 만듭니다.

```java
public class SpyTest {

    @Spy
    List<String> spyOnList = new ArrayList<>();

    @BeforeEach
    public void setUp(){
        MockitoAnnotations.openMocks(this);
    }

    @Test
    void spyTest(){
        spyOnList.add("A");

        assertEquals("A", spyOnList.get(0));

        when(spyOnList.size()).thenReturn(10);
        assertEquals(10, spyOnList.size());

    }
}
```

#### @SpyBean

@MockBean과 마찬가지로 스프링 컨테이너에 Bean으로 등록된 객체에 대해 Spy를 생성해줍니다.

**주의 사항 : @SpyBean이 Interface일 경우 구현체가 반드시 Spring Context에 등록되어야 합니다. => 등록되지 않은 상태라면, @MockBean을 사용하는 것이 좋은 방법이 될 수 있습니다.**

```java
public interface SpyRepository {
    public String spyMethod();
}

//=========================================
@RequiredArgsConstructor
@Service
public class SpyService {

    private final SpyRepository spyRepository;

    public void spyServiceMethod(){
        spyRepository.spyMethod();
    }
}
//==========================================
@SpringBootTest
public class SpyTest {

  	//주의사항: @SpyBean가 인터페이스일 경우 구현체는 반드시 Spring Context에 등록되어야 한다.
  	//@SpyBean 사용시 에러
    @MockBean
    private SpyRepository spyRepository;

    @SpyBean
    private SpyService spyService;

    @BeforeEach
    void setUp(){
        MockitoAnnotations.openMocks(this);
    }

    @Test
    void spyTest(){
        spyRepository.spyMethod();
        spyService.spyServiceMethod();
    }
    
}
```

### 위의 예제를 변경하여 주의사항을 지키는 경우

주의사항: @SpyBean가 인터페이스일 경우 구현체는 반드시 Spring Context에 등록되어야 한다.

```java
//인터페이스 구현체 생성 후 Bean 등록
@Repository
public class SpyRepositoryImpl implements SpyRepository{

    @Override
    public String spyMethod() {
        return "hi";
    }
}
//==========================================
@SpringBootTest
public class SpyTest {


  	@SpyBean
    private SpyRepository spyRepository;

    @SpyBean
    private SpyService spyService;

    @BeforeEach
    void setUp(){
        MockitoAnnotations.openMocks(this);
    }

    @Test
    void spyTest(){
        spyRepository.spyMethod();
        spyService.spyServiceMethod();
    }
    
}
```

