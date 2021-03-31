# 스프링 부트에서 비밀번호 암호화하기

- 스프링부트에서 비밀번호를 암호화해 MySQL에 저장

### 비밀번호 저장방법

- 단순 텍스트
- **단방향 해시 함수의 다이제스트**
  - 복호화 할 수 없는 암호화 방법
  - 운영자들도 사용자의 비밀번호를 모른다(복호화를 할 수 없으므로, 또 복호화해서 사용자의 비밀번호를 알 필요가 없으므로)
  - SHA-256으로 인코딩 

## PasswordEncoder

- 단방향 암호화를 지원하는 인터페이스 - security에서 기본으로 제공

```java
@Configuration
@EnableWebSecurity
@AllArgsConstructor
public class SecurityConfig {

    @Bean
    public PasswordEncoder passwordEncoder(){
        return new BCryptPasswordEncoder();
    }
}
```

## 사용

- Test에서 사용

```java
@Test
  public void createAdmin(){
			BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();
			String defaultPw = passwordEncoder.encode("password1234");
    
    	AdminUser adminUser = AdminUser.builder()
                .adminId("myadmin")
                .password(defaultPw)//비밀번호를 암호화 시켜서 저장한다.
                .adminName("ADMIN")
                .role(Role.SUPERADMIN.getValue())
                .createdAt(LocalDateTime.now())
                .updatedAt(LocalDateTime.now())
                .build();

        log.info("{}", adminUser);
        adminUserRepository.save(adminUser);
  }
```

- Serivce에서 비밀번호 확인하기
  - passwordEncoder.matches() 메소드를 이용하여 입력되는 패스워드와 데이터베이스에서 가져온 패스워드를 비교한다.

```java
@Transactional
public Optional<AdminUser> login(String adminId, String password){
  
  BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();
  ...
  
  //matches(입력되는 패스워드, 데이터베이스에서 가져온 패스워드)
    boolean check = passwordEncoder.matches(password, admin.getPassword());
  if(check){
    log.info("로그인 성공");
  } else {
    log.info("비밀번호가 맞지않습니다.");
    return Optional.empty();
  }
  ...
}
```

