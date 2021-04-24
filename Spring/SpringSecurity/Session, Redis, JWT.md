# Session, Redis, JWT

### Session을 사용하는 이유

- HTTP 프로토콜의 약점을 보완하기 위해 필요합니다.
  - connectionless(비연결지향) : Request / Response 완료 후 연결을 끊습니다.
  - stateless(비상태저장) : 이전에 보냈던 정보를 새로운 Request에서 사용하지 않습니다.
- 쿠키와 세션은 위와 같은 약점을 보완하고자 사용합니다.
  - 쿠키와 세션은 모두 사용자의 정보를 저장하고 필요에 따라 사용합니다.
    - 쿠키는 웹에, 세션은 서버에 정보 저장

### Session의 특징

- 웹 서버에 사용자 정보 저장
- 보안적으로 쿠키보다 우수
- 각 클라이언트의 고유 ID 부여

- 동작 순서
  1. 사용자 접근 요청
  2. Request-Header에서 Cookie를 이용해 session-id 확인
  3. session-id가 없다면, session-id를 생성하여 클라이언트에 반환
  4. 서버에 Request를 요청 시 쿠키는 session-id를 Request-Header에 넣어 요청 
- 세션 데이터는 session-id와 value 형태로 구성
  - NoSQL 구조는 Key-Value 형태이므로 세션정보를 저장하기에 적합합니다. => Redis, Memcached를 사용하는 이유

## Redis란

### Redis

- In-Memory 기반의 NoSQL
- Replication을 지원(장애 극복 기능)
  - Master / Slave로 구성하여 서비스 중단 없이 운영 가능합니다.

### Redis를 세션 서버로 이용하는 이유

- 세션 데이터는 session-id와 value 형태로 구성
  - NoSQL 구조는 Key-Value 형태이므로 세션정보를 저장하기에 적합합니다. 
- Replication을 지원(장애 극복 기능)
  - Master / Slave로 구성하여 서비스 중단 없이 운영 가능합니다.
- In-Memory 방식으로 속도가 빠릅니다.

## 스프링부트와 Redis

https://sup2is.github.io/2020/07/15/session-clustering-with-redis.html

## 스프링부트와 JWT

https://velog.io/@ayoung0073/springboot-JWT

https://jwt.io

JWT: JSON Web Token

속성 정보를 JSON 데이터 구조로 표현한 토큰으로, 인증된 사용자의 정보를 암호화 합니다.

서버와 클라이언트 간 정보교환 시 HTTP request Header에 JSON 토큰을 넣어서 요청합니다.

### 사용

jjwt인것 주의(j두번)

```
implementation 'io.jsonwebtoken:jjwt-api:0.10.7'
```

- JwtUtil

```java
public class JwtUtil {

    private Key key;

    public JwtUtil(String secret) {
        //Java security에서 제공하는 Key 인터페이스로 반환하며, Keys는 jwt라이브러리에서 제공하는 것을 이용한다.
        this.key = Keys.hmacShaKeyFor(secret.getBytes());
    }


    public String createToken(long userId, String name, Long restaruantId) {
        //JJWT 라이브러리 사용

        JwtBuilder builder = Jwts.builder()
                .claim("userId", userId)
                .claim("name", name);

        if(restaruantId != null){
            builder = builder.claim("restaurantId", restaruantId);
        }

        String token = builder
                .signWith(key, SignatureAlgorithm.HS256)
                .compact();

        return token;
    }

    public Claims getClaims(String token) {

        //Jws : Sign이 포함된 jwt를 의미
        Claims claims = Jwts.parser()
                .setSigningKey(key)
                .parseClaimsJws(token)
                .getBody();

        return claims;
    }
}
```

- Jwt를 인증을 위해 커스텀 필터 생성
  - 스프링 시큐리티에서 인증은 필터를 통해 이루어 진다. 제공하는 외에 커스텀 필터를 생성한다.

```java
public class JwtAuthenticationFilter extends BasicAuthenticationFilter {

    private JwtUtil jwtUtil;

    public JwtAuthenticationFilter(AuthenticationManager authenticationManager, JwtUtil jwtUtil) {
        super(authenticationManager);
        this.jwtUtil = jwtUtil;
    }

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain chain) throws IOException, ServletException {

        Authentication authentication = getAuthentication(request);

        if (authentication != null) {
            SecurityContext context = SecurityContextHolder.getContext();
            context.setAuthentication(authentication);
        }


        chain.doFilter(request, response);
    }

    //내부에서 사용되는 Authentication
    private Authentication getAuthentication(HttpServletRequest request){
        String token = request.getHeader("Authorization");

        if(token == null){
            return null;
        }

        //JwtUtil에서 cliams 얻기
        //token에 "Bearer "이 임의로 삽입되므로 제거한다.
        Claims claims = jwtUtil.getClaims(token.substring("Bearer ".length()));
        Authentication authentication = new UsernamePasswordAuthenticationToken(claims, null);
        return authentication;
    }
}
```

- SecurityConfig에 추가

```java
@Configuration
@EnableWebSecurity
public class SecurityJavaConfig extends WebSecurityConfigurerAdapter {

    @Value("${jwt.secret}")
    private String secret;

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        Filter filter = new JwtAuthenticationFilter(authenticationManager(), jwtUtil());

        http
                .cors().disable()
                .csrf().disable()
                .formLogin().disable()
                .headers().frameOptions().disable()
                .and()
                .addFilter(filter)
                .sessionManagement()
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS) //세션은 상태를 가지지 않는다.
        ;
    }

    //IoC 컨테이너가 직접 관리하도록 함
    @Bean
    public PasswordEncoder passwordEncoder(){
        return new BCryptPasswordEncoder();
    }

    @Bean
    public JwtUtil jwtUtil(){
        return new JwtUtil(secret);
    }

}

```

- 사용

```java
@RequiredArgsConstructor
@RestController
public class ReviewController {

    private final ReviewService reviewService;


    @ResponseBody
    @PostMapping("/restaurants/{restaurantId}/reviews")
    public ResponseEntity<?> create(
            Authentication authentication,
            @PathVariable("restaurantId") Long restaurantId,
            @Valid @RequestBody Review resource
    ) throws URISyntaxException {
        Claims claims = (Claims) authentication.getPrincipal();

        String name = claims.get("name", String.class);
        Integer score = resource.getScore();
        String description = resource.getDescription();
        Review review = reviewService.addReview(restaurantId, name, score, description);

        String url = "/restaurants/"+restaurantId+"/reviews/" + review.getId();
        return ResponseEntity.created(new URI(url)).body("{}");
    }

}
```

### 구조

- Header : 3가지 요소를 암호화할 알고리즘 등의 옵션
- Payload : 유저의 고유 ID 등 인증에 필요한 정보
- Verify Signature: Header, Payload와 Secret Key가 더해져 암호화

### 장점

- 별도의 서버가 필요 없습니다.
- REST 서비스로 제공 가능합니다.
- URL 파라미터와 헤더로 사용합니다.
- 수평 스케일, 디버깅 및 관리에 용이합니다.
- 트래픽에 대한 부담이 적습니다.
- 독립적으로 사용가능합니다.

### 단점

- 한 번 발급된 토큰은 삭제할 수 없습니다.
- 토큰 탈취 시 악의적인 용도로 사용가능합니다. => Refresh Token을 이용하여 보완합니다.