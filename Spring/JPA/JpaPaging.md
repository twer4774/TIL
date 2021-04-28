# JPA Paging

참고 

https://www.popit.kr/spring-boot-jpa-%ED%8E%98%EC%9D%B4%EC%A7%95-api-%EB%A7%8C%EB%93%A4%EA%B8%B0/

http://devstory.ibksplatform.com/2020/03/spring-boot-jpa-pageable.html

- 복잡하고 어려지는 않지만 실제 쿼리로 작성할 때는 상당히 번거로운 작업이됨
  - SQL마다 다른 쿼리문 등
  - JPA에서는 이러한 문제를 아주 쉽게 해결할 수 있어 핵심 비지니스에 집중할 수 있음

### 간단한 페이징처리

```java
@GetMapping("/base")
public ResponseEntity baseRead(Pageable pageable){
  Page<Hospital> hospitalList = hospitalRepository.findAll(pageable);

  return new ResponseEntity(hospitalList, HttpStatus.OK);
}

//http://localshot:8080/api/hospital/base?page=2
```

### 커스텀 페이징 처리

```java
//Repository
//시 입력으로 병원 조회
@Query(value="SELECT * FROM ByeCorona.hospital hs where hs.sido_cd_nm=:si", nativeQuery = true)
Page<Hospital> findBySidoNm(@Param("si") String si, Pageable pageable);

//Controller
@GetMapping("")
public ResponseEntity read(@RequestParam String sido, @PageableDefault(size = 5) Pageable pageable) {

  return hospitalService.hospitalReadBySido(sido, pageable);
}

//Service
@Transactional
public ResponseEntity hospitalReadBySido(String sido, Pageable pageable){
  Page<Hospital> hosptialList = hospitalRepository.findBySidoNm(sido, pageable);

  return new ResponseEntity(hosptialList, HttpStatus.OK);
}
```

