# Query DSL - Subquery
- com.querydsl.jpa.JPAExpressions 사용
- subquery는 가능한 한 join으로 변경하는 것이 좋다.
- 비즈니스 로직은 Service 계층에서 해결하는 것이 좋다.
- 데이터 포맷은 View 계층에서 해결하는 것이 좋다.

## select 절의 subquery
```
@Repository
public class MemberRepositorySupport extends QuerydslRepositorySupport {

private final JPAQueryFactory queryFactory;

public MemberRepositorySupport(JPAQueryFactory queryFactory) {
    super(Member.class);
    this.queryFactory = queryFactory;
}


public List<Tuple> findMemberSelectSubquery(){

    return queryFactory
            .select(member.name,
                    JPAExpressions.select(member.age.avg()).from(member)
            )
            .from(member)
            .fetch();
}

}


/* ======================= */

@SpringBootTest
class MemberRepositorySupportTest {

    @Autowired
    private MemberRepositorySupport memberRepositorySupport;


@Test
void select_subquery(){
    List<Tuple> memberSelectSubquery = memberRepositorySupport.findMemberSelectSubquery();

    for(Tuple tuple : memberSelectSubquery){
        System.out.println(tuple);
    }
}


}

/* ======================= */
/*
결과
[test1, 14.0]
[test2, 14.0]
[test3, 14.0]
*/
```


## from 절의 subquery
- JPA, JPQL 에서는 from 절의 서브쿼리를 지원하지 않는다.
- querydsl은 JPQL의 빌더 역할이기 때문에 JPQL이 지원하지 않는 문법은 사용할 수 없다.

## where 절의 subquery
- eq() 사용
- goe() 사용 (>= 함수)
- in() 사용
```
@Repository
public class MemberRepositorySupport extends QuerydslRepositorySupport {

private final JPAQueryFactory queryFactory;

public MemberRepositorySupport(JPAQueryFactory queryFactory) {
    super(Member.class);
    this.queryFactory = queryFactory;
}

// eq() 사용
public Member findMemberWhereSubqueryEq(){

    return queryFactory
            .selectFrom(member)
            .where(member.age.eq(
                    JPAExpressions
                            .select(member.age.max())
                            .from(member))
            )
            .fetchOne();
}

// goe() 사용 (>=함수)
public List<Member> findMemberWhereSubqueryGoe(){

    return queryFactory
            .selectFrom(member)
            .where(member.age.goe(
                    JPAExpressions
                            .select(member.age.avg())
                            .from(member)
            ))
            .fetch();
}

// in() 사용
public List<Member> findMemberWhereSubqueryIn(){

    return queryFactory
            .selectFrom(member)
            .where(member.age.in(
                    JPAExpressions
                            .select(member.age)
                            .from(member)
                            .where(member.age.gt(10))
            ))
            .fetch();
}


}

/* ======================= */

@SpringBootTest
class MemberRepositorySupportTest {

    @Autowired
    private MemberRepositorySupport memberRepositorySupport;

@Test
void where_subquery(){
    // 가장 나이가 많은 회원 - eq()
    Member memberWhereQueryEq = memberRepositorySupport.findMemberWhereSubqueryEq();

    System.out.println("eq : " + memberWhereQueryEq.getName());

    // 평균 나이 이상의 회원리스트 - goe()
    List<Member> memberWhereSubqueryGoe = memberRepositorySupport.findMemberWhereSubqueryGoe();

    for (Member member : memberWhereSubqueryGoe){
        System.out.println("goe : " + member.getName());
    }


    // 10살 이상 - in()
    List<Member> memberWhereSubqueryIn = memberRepositorySupport.findMemberWhereSubqueryIn();
    for(Member member : memberWhereSubqueryIn){
        System.out.println("in : " + member.getName());
    }
}

}


/* ======================= */
/* 
결과
eq : test2
goe : test2
in : test2
in : test3
*/
```

## 참고
[Querydsl 기본문법 학습하기](https://velog.io/@shlee327/Querydsl-%EA%B8%B0%EB%B3%B8%EB%AC%B8%EB%B2%95-%ED%95%99%EC%8A%B5%ED%95%98%EA%B8%B0)
[querydsl 서브쿼리 - 개발자로 성장하기](https://hjhng125.github.io/querydsl/querydsl-subquery/)
