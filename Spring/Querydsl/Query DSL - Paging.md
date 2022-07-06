# Query DSL - Paging
- fetchResults() : 페이징 정보를 포함한 total count 쿼리 실행한다.
- count 쿼리를 select 쿼리와 분리하여 사용하는 것이 좋다.
- offset() : 0부터 시작. 앞에 스킵할 row의 수 지정
- limit() : 최대로 가져올 row의 수

``` java
@Repository
public class MemberRepositorySupport extends QuerydslRepositorySupport {

    private final JPAQueryFactory queryFactory;

    public MemberRepositorySupport(JPAQueryFactory queryFactory) {
        super(Member.class);
        this.queryFactory = queryFactory;
    }

/* Paging */
public List<Member> findMemberWithPaging(){

    return queryFactory
            .selectFrom(member)
            .limit(2) // 노출 row 수
            .offset(0) // skip row 수
            .fetch();
	}
}	

/* =================== */
@SpringBootTest
class MemberRepositorySupportTest {

    @Autowired
    private MemberRepositorySupport memberRepositorySupport;

/* Paging */
@Test
void paging(){
    List<Member> memberWithPaging = memberRepositorySupport.findMemberWithPaging();

    for (Member member : memberWithPaging) {
        System.out.println(member.getName());
    }
}

}

/* =================== */
/*
결과
test1
test2
*/
```


## 참고
[querydsl paging - 개발자로 성장하기](https://hjhng125.github.io/querydsl/querydsl-paging/)
[Querydsl 기본문법 학습하기](https://velog.io/@shlee327/Querydsl-%EA%B8%B0%EB%B3%B8%EB%AC%B8%EB%B2%95-%ED%95%99%EC%8A%B5%ED%95%98%EA%B8%B0)
[JPA Spring Data JPA와 QueryDSL 이해, 실무 경험 공유](https://ict-nroo.tistory.com/117)
