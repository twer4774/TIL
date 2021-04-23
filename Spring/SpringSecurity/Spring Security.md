# Spring Security

## 스프링 시큐리티리란?

- 어플리케이션의 보안(인증 및 권한)을 담당하는 프레임워크
- Spring Security를 사용하지 않으면
  - 자체적으로 세션을 체크해야 한다.
  - redirect를 일일이 설정해주어야 한다.
    - 로그인 완료 시 다음 화면으로 넘어가기 등
- 특징
  - Filter를 기반으로 동작한다.
    - SpringMVC와 분리되어 관리하고 동작할 수 있다.
  - bean으로 설정할 수 있다.
    - Spring Security  3.2부터 XML 설정을 이용하지 않아도 된다.
- 용어
  - 접근 주체(Principal) : 보호된 대상에 접근하는 유저
  - 인증(Authenticate) : 현재 유저가 누구인지 확인(로그인)
    - 어플리케이션의 작업을 수행할 수 있는 주체임을 증명한다.
  - 인가(Authorize) : 현재 유저의 권한을 검사한다.
    - 어떤 페이지, 리소스 등에 접근할 수 있는지를 검사한다.
  - 권한 : 인증된 주체가 어플리케이션의 동작을 수행할 수 있도록 허락 되었는지 확인한다.
    - 권한 승인이 필요한 부분으로 접근하려면 인증 과정을 통해 주체가 증명 되어야 한다.
    - 권한 부여 영역
      - 웹 요청 권한
      - 메소드 호출 및 도메인 인스턴스에 대한 접근 권한

## Architecture 

- https://springbootdev.com/2017/08/23/spring-security-authentication-architecture/

![스프링시큐리티 아키텍처](https://github.com/twer4774/TIL/blob/master/Spring/SpringSecurity/%EC%8A%A4%ED%94%84%EB%A7%81%EC%8B%9C%ED%81%90%EB%A6%AC%ED%8B%B0%20%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98.png)

1. Http Request 수신

   - Spring Security는 필터로 동작을 한다.
   - 요청이 들어오면, 인증과 권한을 위한 필터들을 통하게 된다.
   - 유저가 인증을 요청할때 필터는 인증 메커니즘과 모델을 기반으로한 필터들을 통과한다.
   - 예
     - HTTP 기본 인증을 요청하면 BasicAuthenticationFilter를 통과한다.
     - HTTP Digest 인증을 요청하면 DigestAuthenticationFilter를 통과한다.
     - 로그인 폼에 의해 요청된 인증은 UseerPasswordAuthenticationFilter를 통과한다.
     - x509 인증을 요청하면 X509AuthenticationFilter를 통과한다.

2. 유저 자격을 기반으로 인증토큰(AuthenticationToken) 만들기

   - username과 password를 요청으로 추출하여 유저 저격을 기반으로 인증 객체를 생성한다.
     - 대부분의 인증메커니즘은 username과 password를 기반으로 한다.
   - username과 password는 UsernamePassworkdAutehnticationToekn을 만드는데 사용된다. 

3. Filter를 통해 AuthenticationToken을 AuthenticationManager에 위임한다.

   - UsernamePasswordAuthenticationToken오브젝트가 생성된 후, AuthenticationManager의 인증 메소드를 호출한다.  
   - AuthenticationManager는 인터페이스로 정의되어있다.
     - 실제 구현은 ProviderManager에서 한다.

   ```java
   //AuthenticationManager.java
   public interface AuthenticationManager{
     Authentication authenticate(Authentication authentication) throws AuthenticationException;
   }
   ```

   - 실제 프로그래밍 구현에서 AuthenticationManager를 사용하기 위해 설정에 AuthenticationManagerBuilder를 이용해 아래에 정의된 UserServiceDetails를 매핑시켜준다.
     - 여기서는 LoginService가 UserDetailsService를 구현하였으므로, LoginService가 UserDetailsService의 역할을 한다. 

   ```java
   @Override
   protected void configure(AuthenticationManagerBuilder auth) throws Exception{   auth.userDetailsService(loginService); }
   ```

   

   - ProviderManager는 AuthenticationProvider를 구성하는 목록을 갖는다.

   ```java
   public class ProviderManager implements AuthenticationManager, MessageSourceAware, InitializingBean { ... }
   ```

   - ProviderManager는 AuthenticationProvider에 각각의 목록들을 제공하고, password Authentication 객체를 기반으로 만들어진 인증을 시도한다.
     - password Authentication 객체 = UsernamePasswordAuthenticationToken

4. AuthenticationProvider의 목록으로 인증을 시도한다.

   - AuthenticationProvider의 위치(Core에 들어있다는것만 알아두자)

   ```
   Gradle:org.springframework.security/spring-security-core/spring-security-core-5.4.5-sources.jar library root/org/springframework/security/authentication/AuthenticationProvider.java
   ```

   - AuthenticationProvider 내용

   ```java
   public interface AuthenticationProvider {
       Authentication authenticate(Authentication authentication) throws AuthenticationException;
       boolean supports(Class<?> authentication);
   }
   ```

   - 인증을 위해 제공하는 것들
     - CasAuthenticationProvider
     - JaasAuthenticationProvider
     - DaoAuthenticationProvider
     - OpenIDAuthenticationProvider
     - RememberMeAuthenticationProvider
     - LdapAuthenticationProvider

5. UserDetailsService의 요구

   - UserDetailsService는 username 기반의 user details를 검색한다.
     - AuthenticationProvider에서 제공하고 있는 DaoAuthenticationProvider를 사용하는 것이다.

   ```java
   public interface UserDetailsService
   {
     UserDetails loadUserByUsername(String username) throws UsernameNotFoundException;
   }
   ```

6. UserDetails를 이용해서 User객체에 대한 정보를 검색한다.

   - UserDetailsService는 인터페이스이므로, 우리가 인증하고자하는 비즈니스로직을 정의한 serivce레이어에서 구현을 실행하는 방식을 이용한다.

   ```java
   public class LoginService implements UserDetailsService{}
   ```

   - UserDetailsService는 UserDetails를 username을 기반으로 검색을 실행한다.

     - UerDetails는 인터페이스로, 우리가 데이터베이스 생성하기 위한 객체(ex. AdminUser 또는 User 등)에서 정보를 가져올 때 이용된다.

     ```java
     public interface UserDetails extends Serializable {
       Collection<? extends GrantedAuthority> getAuthorities();
       String getPassword();
     	String getUsername();
       ...
     }
     ```

7. User객체의 정보들을 UserDetails가 UserDetailsService(LoginService)에 전달한다.

   - 데이터베이스에서 User 객체에 매핑된 정보를 가져와 UserDetailsService(LoginService)에 전달한다.
   - 전달된 User 객체의 정보와 사용자가 요청한 인증 정보(username, password)를 확인하는 로직을 LoginService에 구현한다.

   ```java
   @Transactional
   public Optional<AdminUser> login(String adminId, String password) throws UsernameNotFoundException { //인증 로직 구현(아이디, 비밀번호를 확인하는 로직을 거친다.)}
   ```

   - UserDetailsService에서 username을 기반으로 검색을 실행한다고 위에 정의했다.

     - loadUsername은 UserDetailsService가 구현을 필수로 하기를 원하는 메소드이다.
     - 반환 값으로 User에 id와 password, 권한 정보를 넣어서 반환한다.
       - User는 org.springframework.security.core.userdetails에서 기본적으로 제공해주는 User 객체이다. 
         - 개발자는 User를 그대로 사용해도 되고, User를 상속받아 확장하여 사용해도 되고, 아래와 같이 권한을 넘겨줄때만 이용할 수도 있다.
           - 또는 User대신 UserDetails(인터페이스)를 구현하여 사용할 수도 있다.
         - 중요한것은, UserDetailsService가 권한 정보를 알 수 있도록 결론적으로 User라는 객체를 통해  정보를 받을 수 있어야 한다는 것이다.

     ```java
     @Override
     public UserDetails loadUserByUsername(String adminName) throws UsernameNotFoundException { 
     AdminUser adminUser = adminUserRepository.findByAdminName(adminName);
             AdminUser admin = adminUser.get();
     
             List<GrantedAuthority> authorities = new ArrayList<>();
     
             if("ADMIN".equals(adminName)){
                 authorities.add(new SimpleGrantedAuthority(Role.ADMIN.getValue()));
             } else {
                 authorities.add(new SimpleGrantedAuthority(Role.MEMBER.getValue()));
             } 
       //User 객체에 아이디, 비밀번호, 권한정보를 넘겨준다.
      return new User(
                     admin.getAdminId()
                     , admin.getPassword()
                     , authorities
                     );
     }
     ```

     - User객체의 내용(UserDetils를 구현한 객체)

     ```java
     public class User implements UserDetails, CredentialsContainer {
     
     	private static final long serialVersionUID = SpringSecurityCoreVersion.SERIAL_VERSION_UID;
     
     	private static final Log logger = LogFactory.getLog(User.class);
     
     	private String password;
     
     	private final String username;
     
     	private final Set<GrantedAuthority> authorities;
     
     	private final boolean accountNonExpired;
     
     	private final boolean accountNonLocked;
     
     	private final boolean credentialsNonExpired;
     
     	private final boolean enabled;
       ...
     }
     ```

8. 인증 객체 또는 AuthenticationException

   - 유저의 인증이 성공하면, 전체 인증정보를 리턴한다.
     - 인증에 실패하면 AuthenticationException을 던진다.
   - 인증에 성공한 객체의 정보
     - authenticated - true
     - grant authorities list : 권한 정보
     - user credentials(username only) : username으로 인증된 사항

9. 인증 끝

   - AuthenticationManager는 완전한 인증(Fully Populated Authentication)객체를 Authentication Filter에 반환한다.

10. SecurityContext에 인증 객체를 설정한다.

    - AuthenticationFilter는 인증 객체를 SecurityContext에 저장한다.

    ```java
    SecurityContextHolder.getContext().setAuthentication(authentication);
    ```

    



