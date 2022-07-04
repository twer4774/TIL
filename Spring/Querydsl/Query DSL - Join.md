# Query DSL - Join
- 첫 번째 파라미터에 조인 대상을 지정하고, 두 번째 파라미터에 별칭으로 사용할 Q 타입 지정

## DB
- Team Table
```
+----+-------+---------+
| id | name  | type    |
+----+-------+---------+
|  1 | team1 | amature |
|  2 | team2 | semipro |
+----+-------+---------+
```
- Member Table
```
+----+-------+------+---------+---------+
| id | name  | age  | address | team_id |
+----+-------+------+---------+---------+
|  1 | test1 | 10   | NULL    |       1 |
|  2 | test2 | 20   | NULL    |       1 |
|  3 | test3 | 12   | 집1     |       2 |
+----+-------+------+---------+---------+
```


## 기본 조인
join(조인 대상, 별칭으로 사용할 Q타입)
- join(), innerJoin() : 내부 조인 (inner join)
- leftJoin() : left 외부 조인
- rightJoin() : right 외부 조인
- JPQL의 on과 성능 최적화를 위한 fecth 조인 제공
``` java
@Repository
public class MemberRepositorySupport extends QuerydslRepositorySupport {


// team 아이디가 1번인 회원 리스트 출력
public List<Member> findMemberJoin(){
    return queryFactory
            .select(member)
            .from(member)
            .where(member.team.id.eq(1L))
            .fetch();
}

/* ============================ */
@SpringBootTest
class MemberRepositorySupportTest {

    @Autowired
    private MemberRepositorySupport memberRepositorySupport;

@Test
void 조인(){
    List<Member> memberJoin = memberRepositorySupport.findMemberJoin();

    for(Member member : memberJoin){
        System.out.println(member.getName());
    }
}

}

/* ============================ */
/* 결과
test1
test2
*/
```

## 세타 조인
- **비교 연산자를 사용**해 두 릴레이션의 속성 값에 맞는 모든 튜플을 연결한 새로운 튜플로 결과 릴레이션을 반환한다.
=> 연관 관계가 없는 필드로 조인한다.
=> 조인하는 테이블의 모든 행의 갯수만큼 반환된다.
- from 절에 테이블을 나열한다.
``` java 
@Repository
public class MemberRepositorySupport extends QuerydslRepositorySupport {


// team 아이디가 1번인 회원 리스트 출력
public List<Member> findMemberJoin(){
    return queryFactory
            .select(member)
            .from(member)
            .where(member.team.id.eq(1L))
            .fetch();
}
// thetajoin
public List<Member> findMemberThetaJoin(){
    return queryFactory
            .select(member)
            .from(member,team)
            .fetch();
}
}
/* ============================ */
@SpringBootTest
class MemberRepositorySupportTest {

    @Autowired
    private MemberRepositorySupport memberRepositorySupport;
@Test
void 세타조인(){
    List<Member> memberThetaJoin = memberRepositorySupport.findMemberThetaJoin();

    for(Member thetaMember : memberThetaJoin){
        System.out.println("MemberName : " + thetaMember.getName() + " / TeamName : " + thetaMember.getTeam().getName());
    }
}
}

/* ============================ */
/*
// 결과
MemberName : test1 / TeamName : team1
MemberName : test1 / TeamName : team1
MemberName : test2 / TeamName : team1
MemberName : test2 / TeamName : team1
MemberName : test3 / TeamName : team2
MemberName : test3 / TeamName : team2
*/
```

## 조인 on 절
- 조인대상 필터링
``` java
@Repository
public class MemberRepositorySupport extends QuerydslRepositorySupport {
public List<Member> findMemberJoinWithOn(){
    return queryFactory
            .select(member)
            .from(member)
            .leftJoin(team).on(member.team.id.eq(team.id))
            .where(team.id.eq(1L))
            .fetch();
}
}

/* ============================ */
@SpringBootTest
class MemberRepositorySupportTest {

    @Autowired
    private MemberRepositorySupport memberRepositorySupport;

@Test
void on_사용(){
    List<Member> memberJoinWithOn = memberRepositorySupport.findMemberJoinWithOn();

    for(Member onMember : memberJoinWithOn){
        System.out.println(onMember.getName());
    }
}
}

/* ============================ */
/*
// 결과
test1
test2
*/
```


## 조인 페치 조인
- SQL 조인을 활용해서 연관된 엔티티를 SQL을 한번에 조회하는 기능  (SQL에서 지원하는 기능은 아니다.)
- 주로 성능 최적화에 사용된다.
- 연관된 엔티티를 쿼리 한번으로 모두 가져오는 방법 (FetchType.EAGER와 같은 동작)
	- FetchType.EAGER와 차이
		- EAGER 사용시 해당 연관관계에서 발생하는 모든 쿼리에서 연관관계 데이터도 모두 가져온다.
		- 특정 상황에서만 한 번에 데이터를 가져오고 싶을 때는 fetchJoin()을 사용하는 것이 좋다.
		- N+1문제를 fetchJoin으로 해결할 수 있다.
``` java
@Repository
public class MemberRepositorySupport extends QuerydslRepositorySupport {
// fetch join 사용
public List<Member> findMemberFetchJoin(){
    return queryFactory
            .selectFrom(member)
            .join(member.team, team).fetchJoin()
            .where(member.team.id.eq(2L))
            .fetch();
}

}

/* ============================ */
@SpringBootTest
class MemberRepositorySupportTest {

    @Autowired
    private MemberRepositorySupport memberRepositorySupport;

@Test
void fetchJoin(){
    List<Member> memberFetchJoin = memberRepositorySupport.findMemberFetchJoin();


    for(Member member : memberFetchJoin){
        System.out.println(member.getName());
    }
}

}

/* ============================ */
/*
// 결과
test3
*/

```



## 참고
- [querydsl join - 개발자로 성장하기](https://hjhng125.github.io/querydsl/querydsl-join/)
- https://velog.io/@shlee327/Querydsl-%EA%B8%B0%EB%B3%B8%EB%AC%B8%EB%B2%95-%ED%95%99%EC%8A%B5%ED%95%98%EA%B8%B0
