# Query DSL - Dynamic Query
- QueryDSL은 원하는 필드만 DTO로 뽑을 수 있다.
- 동적 쿼리를 처리하는 두 가지 방법
	- BooleanBuilder를 이용하는 방법
	- Where 절에서 파라미터를 이용하는 방법

### BooleanBuilder
- null인지 아닌지 판별하여 builder를 조립해서 where 문에 넣는다.
- .and(), .or()등을 이용해 조건을 추가할 수 있다.
``` java
@Repository
public class MemberRepositorySupport extends QuerydslRepositorySupport {

    private final JPAQueryFactory queryFactory;

    public MemberRepositorySupport(JPAQueryFactory queryFactory) {
        super(Member.class);
        this.queryFactory = queryFactory;
    }

	public List<Member> findMemberBooleanBuilder(String name, String address){

    BooleanBuilder builder = new BooleanBuilder();

    if(name != null){
        builder.and(member.name.eq(name));
    }

    if(address != null){
        builder.and(member.address.eq(address));
    }

    return queryFactory
            .selectFrom(member)
            .where(builder)
            .fetch();
	}

}

/* =================== */
@SpringBootTest
class MemberRepositorySupportTest {

    @Autowired
    private MemberRepositorySupport memberRepositorySupport;

// BooleanBuilder
@Test
void booleanBuilderTest(){
    List<Member> memberBooleanBuilder = memberRepositorySupport.
            findMemberBooleanBuilder("test1", null);

    for(Member member : memberBooleanBuilder){
        System.out.println(member.getName());
    }
}

}

/* =================== */
/*
결과
test1
*/
```

### Where절에서 파라미터를 이용하는 방법
- BooleanExpression 타입을 리턴하는 메서드를 만들어 조건을 추가하는 방식이다.
``` java
@Repository
public class MemberRepositorySupport extends QuerydslRepositorySupport {

    private final JPAQueryFactory queryFactory;

    public MemberRepositorySupport(JPAQueryFactory queryFactory) {
        super(Member.class);
        this.queryFactory = queryFactory;
    }

// BooleanExpression
public List<Member> findMemberBooleanExpression(String name, String address){

    return queryFactory
            .selectFrom(member)
            .where(nameEq(name), addressEq(address))
            .fetch();
}
// 결과가 null이면 where()에서 무시된다.
private BooleanExpression nameEq(String name){
    return name != null ? member.name.eq(name) : null;

}

private BooleanExpression addressEq(String address){
    return address != null ? member.address.eq(address) : null;
}


}

/* =================== */
@SpringBootTest
class MemberRepositorySupportTest {

    @Autowired
    private MemberRepositorySupport memberRepositorySupport;

@Test
void booleanExpressionTest(){
    List<Member> memberBooleanExpression = memberRepositorySupport.findMemberBooleanExpression("test1", null);

    for(Member member : memberBooleanExpression){
        System.out.println(member.getName());
    }
}

}

/* =================== */
/*
결과
test1
*/
```

## 참고
[Querydsl 동적 쿼리](https://velog.io/@aidenshin/Querydsl-%EB%8F%99%EC%A0%81-%EC%BF%BC%EB%A6%AC)
[querydsl 동적 쿼리 - 개발자로 성장하기](https://hjhng125.github.io/querydsl/querydsl-dynamic-query/)
