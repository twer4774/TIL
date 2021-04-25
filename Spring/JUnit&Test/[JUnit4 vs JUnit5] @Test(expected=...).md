# [JUnit4 vs JUnit5] @Test(expected=...)

예외 처리에 관련된 테스트를 진행하다 보면 @Test(expected= NullPointerException.calss)와 같이 이 테스트는 NullPointerException로 예외처리를 진행하겠다는 표시를 하게됩니다.

**위의 코드는 JUnit4에서 작성가능한 코드이며, JUnit5에서는 assertThrows 메소드를 사용하여 동일한 기능을 구현할 수 있습니다.**

```java
//JUnit4
@Test(expected=NullPointerException.class)
public void DetailWithNotExisted(){
		String hi = null;
  	hi.length(); //NullPointerException 발생
}

//JUnit5
@Test
public void DetailWithNotExisted(){
		String hi = null;
  	assertThrows(NullPointerException.class, () -> {
    	hi.length(); //NullPointerException 발생  
    })
}
```

- JUnit5 구문의 장점
  - 람다식으로 더 다양한 경우의 수를 간단하게 처리할 수 있게 되었습니다.

## 활용 - 커스텀 예외 생성 및 서비스 레이어 테스트

1. 커스텀 예외를 작성합니다.
2. @ControllerAdvice를 이용하여 모든 컨트롤러의 예외를 잡아주는 클래스를 만들어줍니다.
3. 서비스 레이이어 테스트를 실행합니다.
4. 서비스 레이어 테스트의 assertThrow를 위해 서비스 레이어에서 throw 해주는 코드를 작성합니다.

```java
//1. 커스텀 예외를 작성합니다.
public class RestaurantNotFoundException extends RuntimeException {

    public RestaurantNotFoundException(long id) {
        super("Could not find restaurant " + id);
    }
}

//2. @ControllerAdvice 이용
@ControllerAdvice
public class RestaurantErrorAdvice {    
    @ResponseBody
    @ResponseStatus(HttpStatus.NOT_FOUND)
    @ExceptionHandler(RestaurantNotFoundException.class)
    public String handlerNotFound(){
        return "{}";
    }
}

//3. 서비스레이어에서 테스트를 진행합니다.
class RestaurantServiceTest {
  ...
    @Test
    public void getRestaurantWithNotExisted(){

    //service의 getRestaurant에서 throw 추가 필요
    assertThrows(RestaurantNotFoundException.class, ()-> {
      Restaurant restaurant = restaurantService.getRestaurant(404L); //404번의 아이디는 없다. => NotFoundException 발생
    });
  }
}

//4. 서비스레이어에서 에러를 던져주는 코드 작성
@Service
public RestaurantService{
  ...
   public Restaurant getRestaurant(Long id) {
        Restaurant restaurant = restaurantRepository.findById(id)
                .orElseThrow(() -> new RestaurantNotFoundException(id)); //커스텀 예외 던지기

        return restaurant;
    }
}
```

위의코드를 작성 후 3번에서 작성한 테스트 코드를 실행하여 결과를 확인 할 수 있습니다.