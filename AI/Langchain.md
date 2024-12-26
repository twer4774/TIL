- OpenAI, Cohere, Bloom, hugginface 등 여러 대형 LLM 공급업체와의 상호작용을 간소화하기 위해 설계된 강력한 라이브러리
- 한개 이상의 LLM사이의 논리적으로 연결된 Chains를 생성할 수 있는 기능 제공

## 구성요소
- LangSmith : 디버그, 테스트, 모니터링
- LangServe : RestAPI 배포
- LangChain : 체인, 검색 전략 아키텍처
- LangChain-Community : 써드파티 통합. langchain-openai, langchain-anthropic 등
- Langchain-core : 기본 추상화, Langchain 표현언어

## Langchain 정의
- 컴포넌트
	- Model IO
		- 프롬프트 관리, 프롬프트 최적화, 챗모델과 LLM 인터페이스
	- Retrieval
		- 다양한 소스에서 데이터 검색
	- Agents
		- LLM의 자율성 허용. 작업 수행 -> 관찰 -> 수행 반복 작업등