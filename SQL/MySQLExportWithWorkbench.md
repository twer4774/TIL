# MySQL Export

데이터베이스를 외부로 내보내기 위함

1. Workbench 기준으로 Server 메뉴 - Data Export
2. 데이터베이스(Schema) 선택
3. 테이블(SchemaObject) 선택
4. Export Options - Export to Self-Contained File 선택(저장경로 설정도 필요)
   - Export to Dump Project Folder 옵션과의 차이
     - Export to Dump Project Folder의 경우 테이블의 갯수만큼 SQL 파일이 생성됨
     - Export to Self-Contained File은 모든 테이블이 하나의 SQL 파일로 합쳐서 생성
5. Start Export 실행

