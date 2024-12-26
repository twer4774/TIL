- RAG(Retrieval-Augmented Generation)은 맞춤형 데이터를 활용하여 LLM의 효율성 개선
- 질문이나 작업에 과련된 데이터/문서를 검색하고 이를 LLM의 컨텍스트로 제공

## RAG 기술 단계
- 검색 부분 (Retrieval Component) : 정보 찾기
	- 사용자의 질문 입력
	- 관련된 정보나 데이터를 대규모 데이터베이스나 문서 집합에서 검색
- 생성 부분 (Generation Component) : 이야기 만들기
	- 검색된 정보를 기반으로 자연스러운 언어의 답변 생성
	- GPT와 같은 전이 학습(Transformer-based) 모델 활용
	- 생성된 모델은 검색된 정보를 통합/이해하며, 질문에 가장 적합한 답변을 생성하는데 사용

## OpenAI에 최적화된 프롬프트
- https://smith.langchain.com/hub/rlm/rag-prompt
```
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
Question: {question} 
Context: {context} 
Answer:
```