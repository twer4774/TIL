# [Spring Security] defaultSuccessUrl, successForwardUrl, successHandler

- 참고 : https://www.codejava.net/frameworks/spring-boot/spring-boot-security-customize-login-and-logout

  

## defaultSuccessUrl

- Spring Security는 인증이 필요한 페이지에 사용자가 접근하면, 로그인 페이지로 이동시킨다.
  - 로그인이 성공하면 사용자가 처음에 접근했던 페이지로 리다이렉트 시켜준다.
- 사용자가 로그인하기 전에 방문했던 페이지가 아닌, 다른 페이지를 원한다면 defaultSuccessUrl을 사용한다.

```java
http.formLogin().defaultSuccessUrl("/login_success");
```

## successForwardUrl

- 로그인이 성공한 후 보내는 Url
- 특정 url을 호출하여 다른 로직을 한 번 더 실행한다.

```java
http.formLogin().successForwardUrl("/login_success_handler");
```

```java
@Controller
public class TestController(){
  
  @GetMapping("/login_success_handler")
  public String loginSuccessHandler(){
    return "index";
  }
}
```

## successHandler

- successFrowardUrl과 비슷한 것으로, controller로 분리된 로직을 config 단에서 한 번에 처리할 수 있다.

```java
http.formLogin().successHandler(
  
 	new AuthenticationSuccessHandler() {
        
   @Override
   public void onAuthenticationSuccess(HttpServletRequest request, HttpServletResponse response, Authentication authentication) throws IOException, ServletException {
				response.sendRedirect("/index");
   }
);
```

