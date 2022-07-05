# Query DSL - CASE
- 조건에 따른 값을 지정해주는 문법
- select, where, orer by 절에서 사용 가능

## Simple case
``` java
@Repository
public class MemberRepositorySupport extends QuerydslRepositorySupport {

    private final JPAQueryFactory queryFactory;

    public MemberRepositorySupport(JPAQueryFactory queryFactory) {
        super(Member.class);
        this.queryFactory = queryFactory;
    }

public List<String> findMemberCase(){

    return queryFactory
            .select(member.age
                    .when(10).then("10살")
                    .when(20).then("20살")
                    .otherwise("0")
            )
            .from(member)
            .fetch();
}


}

/* ================= */

@SpringBootTest
class MemberRepositorySupportTest {

    @Autowired
    private MemberRepositorySupport memberRepositorySupport;


@Test
void simpleCase(){
    List<String> memberCase = memberRepositorySupport.findMemberCase();

    memberCase.forEach(System.out::println);
}
}

/* ================= */
/*
결과
10살
20살
0
*/
```

## Complex case
``` java
@Repository
public class MemberRepositorySupport extends QuerydslRepositorySupport {

    private final JPAQueryFactory queryFactory;

    public MemberRepositorySupport(JPAQueryFactory queryFactory) {
        super(Member.class);
        this.queryFactory = queryFactory;
    }


}
/* ================= */

@SpringBootTest
class MemberRepositorySupportTest {

    @Autowired
    private MemberRepositorySupport memberRepositorySupport;


@Test
void complexCase(){
    List<Tuple> memberComplexCase = memberRepositorySupport.findMemberComplexCase();

    for(Tuple tuple : memberComplexCase){
        System.out.println(tuple);
    }
}

}
/* ================= */
/*
결과
[test1, 10, 미성년자]
[test2, 20, 20살 성인]
[test3, 12, 미성년자]
*/
```