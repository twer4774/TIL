# Query DSL - 기초
- 참고 
	- [Querydsl 기본문법 학습하기](https://velog.io/@shlee327/Querydsl-%EA%B8%B0%EB%B3%B8%EB%AC%B8%EB%B2%95-%ED%95%99%EC%8A%B5%ED%95%98%EA%B8%B0)
	- [Querydsl 다이나믹 쿼리 사용하기](https://jojoldu.tistory.com/394)
## JPA와 비교
- JPA 비교해 JPA의 장점
	- 가독성이 좋다.
		- JPA에서 기본적으로 제공하는 기능을 넘어서는 기능은 일반적으로 native query 옵션으로 수행한다. -> 문자열을 이어붙이는 형태이므로 오타로 인해 런타임 시 오류가 발생할 가능성이 높다.
	- 컴파일 시점에서 에러를 체크할 수 있다.
	-  IDE의 자동 완성 기능이 지원된다.
	- **동적쿼리를 지원한다.**
- 단점 
	- 추가적인 학습이 필요하다.
		- ex) member.age.gt(10)은 age > 10을 의미한다.	
	- native query문이 아니므로, RDBMS나 MySQL에서 쿼리문을 실행하기 위해서는 다시 쿼리문을 작성해야 한다.

## Depdency
```
buildscript {
	ext {
		queryDslVersion = "5.0.0"
	}
}

plugins {
	id 'org.springframework.boot' version '2.7.0'
	id 'io.spring.dependency-management' version '1.0.11.RELEASE'
	id 'java'

	// querydsl 추가
	id "com.ewerk.gradle.plugins.querydsl" version "1.0.10"
}

group = 'walter.unit'
version = '0.0.1-SNAPSHOT'
sourceCompatibility = '11'

configurations {
	compileOnly {
		extendsFrom annotationProcessor
	}
}

repositories {
	mavenCentral()
}

dependencies {
	implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
	implementation 'org.springframework.boot:spring-boot-starter-mustache'
	implementation 'org.springframework.boot:spring-boot-starter-web'
	runtimeOnly 'mysql:mysql-connector-java'

	// querydsl 추가
	implementation "com.querydsl:querydsl-jpa:${queryDslVersion}"
	implementation "com.querydsl:querydsl-apt:${queryDslVersion}"

	compileOnly 'org.projectlombok:lombok'
	annotationProcessor 'org.projectlombok:lombok'
	testImplementation 'org.springframework.boot:spring-boot-starter-test'
}

tasks.named('test') {
	useJUnitPlatform()
}

// querydsl 추가 시작
def querydslDir = "$buildDir/generated/querydsl"

querydsl {
	jpa = true
	querydslSourcesDir = querydslDir
}

sourceSets {
	main.java.srcDir querydslDir
}

configurations {
	querydsl.extendsFrom compileClasspath
}

compileQuerydsl{
	options.annotationProcessorPath = configurations.querydsl
}

compileQuerydsl.doFirst {    if(file(querydslDir).exists() )        delete(file(querydslDir))}

```
## yml
```
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/test?allowPublicKeyRetrieval=true&useSSL=false&useUnicode=true&serverTimezone=Asia/Seoul&zeroDateTimeBehavior=convertToNull
    username: username
    password: password
    driver-class-name: com.mysql.cj.jdbc.Driver

  jpa:
    database-platform: org.hibernate.dialect.MySQL8Dialect
    hibernate:
      ddl-auto: none #배포시 NONE으로 변경

```
## Entity 추가
```
@Entity
@Getter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Member {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name")
    private String name;

    @Column(name = "age")
    private int age;

    @Column(name = "address")
    private String address;


    @ManyToOne
    @JoinColumn(name = "team_id")
    private Team team;

}

==================

@Entity
@Getter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Team {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    private String type;

    @OneToMany(fetch = FetchType.LAZY, mappedBy = "team")
    private List<Member> memberList;
}

```
## QModel 생성
- gradle - tasks - build - clean
- gradle - tasks - other - compileQuerydsl
- build - generated 파일에서 QModel 확인
	- 자동 생성되는 QMember
```
/**
 * QMember is a Querydsl query type for Member
 */
@Generated("com.querydsl.codegen.DefaultEntitySerializer")
public class QMember extends EntityPathBase<Member> {

    private static final long serialVersionUID = 851117285L;

    public static final QMember member = new QMember("member1");

    public final NumberPath<Long> id = createNumber("id", Long.class);

    public final StringPath name = createString("name");

    public QMember(String variable) {
        super(Member.class, forVariable(variable));
    }

    public QMember(Path<? extends Member> path) {
        super(path.getType(), path.getMetadata());
    }

    public QMember(PathMetadata metadata) {
        super(Member.class, metadata);
    }

}
=================
/**
 * QTeam is a Querydsl query type for Team
 */
@Generated("com.querydsl.codegen.DefaultEntitySerializer")
public class QTeam extends EntityPathBase<Team> {

    private static final long serialVersionUID = -955329688L;

    public static final QTeam team = new QTeam("team");

    public final NumberPath<Long> id = createNumber("id", Long.class);

    public final ListPath<Member, QMember> memberList = this.<Member, QMember>createList("memberList", Member.class, QMember.class, PathInits.DIRECT2);

    public final StringPath name = createString("name");

    public final StringPath type = createString("type");

    public QTeam(String variable) {
        super(Team.class, forVariable(variable));
    }

    public QTeam(Path<? extends Team> path) {
        super(path.getType(), path.getMetadata());
    }

    public QTeam(PathMetadata metadata) {
        super(Team.class, metadata);
    }

}
```
## Config
```
@Configuration
public class QuerydslConfiguration {

    @PersistenceContext
    private EntityManager entityManager;

    @Bean
    public JPAQueryFactory jpaQueryFactory(){
        return new JPAQueryFactory(entityManager);
    }

}
```

## RepositorySupport
```
@Repository
public class MemberRepositorySupport extends QuerydslRepositorySupport {

    private final JPAQueryFactory queryFactory;

    public MemberRepositorySupport(JPAQueryFactory queryFactory) {
        super(Member.class);
        this.queryFactory = queryFactory;
    }

    public List<Member> findByName(String name){
        return queryFactory
                .selectFrom(member)
                .where(member.name.eq(name))
                .fetch();
    }
}

===============================
@Repository
public class TeamRepositorySupport extends QuerydslRepositorySupport {


    private final JPAQueryFactory queryFactory;

    public TeamRepositorySupport(JPAQueryFactory queryFactory) {
        super(Team.class);
        this.queryFactory = queryFactory;
    }

}

```
## Test
```
@SpringBootTest
class MemberRepositorySupportTest {

    @Autowired
    private MemberRepositorySupport memberRepositorySupport;

@Test
void getTest1(){
    Member test1 = memberRepositorySupport.findByNameOne("test1");

    StringBuilder sb = new StringBuilder();
    sb.append("id: ");
    sb.append(test1.getId());
    sb.append(" / ");
    sb.append("age: ");
    sb.append(test1.getAge());
    sb.append(" / ");
    sb.append("address: ");
    sb.append(test1.getAddress());
    sb.append(" / ");
    sb.append("teamType : ");
    sb.append(test1.getTeam().getType());
    sb.append(" / ");
    sb.append("teamName : ");
    sb.append(test1.getTeam().getName());

    System.out.println(sb.toString());

}

}

================ 결과
id: 1 / age: 10 / address: null / teamType : amature / teamName : team1

```