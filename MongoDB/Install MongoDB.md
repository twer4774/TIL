# MongoDB 설치 (Mac)

- https://blog.naver.com/xxxismin/222260628040

## 사용

- db : 현재사용하고 있는 데이터베이스  이름 출력
- db.stats() : 현재 사용하고 있는 데이터베이스 정보 출력
- use test : 데이터베이스 사용(존재하지 않으면 생성됨)
- db.dropDatabase()
- db.createCollection(“book”,{capped:true, size:6142800, max:10000})
  - capped: true로 설정시 활성화
    - 고정된 크기를 가진 컬렉션, 사이즈를 초과하면 가장 오래된 데이터를 덮어씀
  - size: capped가 true일 경우 필수로 설정해야 하는 값
  - max: 해당 컬렉션에 추가할 수 있는 최대 document 개수
- show collections;
- db.testCollection.drop();
- db.book.insert([{"name":"abc"}, {"name":"hello"}])
- db.book.drop() : test데이터베이스의 book이라는 collection을 제거
- db.books.find() : document리스트 확인
- db.book.remove({"name":"hello"}): document리스트 삭제

## homebrew 설치 - 카탈리나 이상부터 하기 힘듦

- mac용 패키지 관리자인 homebrew 설치
- https://brew.sh/index_ko
- 터미널에서 실행

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## mongodb 설치

- https://github.com/mongodb/homebrew-brew

```
brew tap mongodb/brew
brew install mongodb-community
mongo -version
```
