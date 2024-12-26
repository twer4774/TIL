- Vector DB는 정보를 벡터로 저장하는 데이터 베이스
- 벡터 데이터 : 다차원 벡터 공간에 표현되는 데이터를 의미
- 일반적으로 기계 학습에 사용되는 임베딩 알고리즘에서 파생
## Vector Databases의 이점
- 효율적인 데이터 관리 (Efficient Data Management)
- 검색 기능 향상 (Enhanced Search Capabilities)
- 확장성 (Scalability)
- 머신러닝과 AI와의 호환성 (Compatibility with AI and Machine Learning)

## Vector Database OpenSource
1. Chroma : 탐색기능 좋음
2. Weaviate 
3. Qdrant : 효율적인 유사성 검색, 위치 정보에 좋음
4. Milvus : 고성능을 위한 벡터 데이터베이스
5. Faiss : 유사성 검색과 클러스터링

### ChromaDB VS Faiss
| ChromaDB | - 컴퓨터 비전 및 이미지 처리를 위해 특별히 설계<br>- 대규모 색상 데이터를 관리하고 검색                          |
| -------- | ------------------------------------------------------------------------------ |
| FAISS    | - 유사성 검색을 위해 설계된 범용적 라이브러리<br>- 특정 유형의 데이터에 국한되지 않음<br>- 문서가 많아져도 검색속도가 빠른편이다. |
