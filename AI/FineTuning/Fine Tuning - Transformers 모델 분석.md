# Transformers
- 다양한 NLP 작업을 해결하는데 사용
- Transformers Library :  공유된 모델을 만들고 사용할 수 잇는 다양한 기능들을 제공
- Model Hub : 누구나 다운로드하여 사용할 수 있는 수천 개의 사전 학습된 모델(pretrained models)들이 포함

## Transforemers Library
- pipeline 함수
	- Transformer library 기본 객체. 모델에 필요한 전/후처리 단계와 연결하여 텍스트를 직접 입력하고 이해하기 쉬운 답변을 만듦
```
from transforemrs import pipeline

classifier = pipeline("sentiment-analysis")
classifier(
["I've been wating for a HuggingFace course my whole life.", "I hate this so much"]
)
```
## 활용 가능한 파이프라인
| 파이프라인                         | 설명                                                                  |
| ----------------------------- | ------------------------------------------------------------------- |
| feature-extraction            | 기계 학습 및 데이터 분석 과정을 원시 데이터에서 관련 특징을 식별하고 추출하는 과정                     |
| fill-mask                     | 문장의 일부 단어를 가리고 해당 마스크를 대체해야 하는 단어를 예측하는 작업                          |
| ner(named entity recognition) | 엔티티를 식별하고 분류하는데 중점을 둔 NLP 기술                                        |
| question-answering            | 자연어로 인간이 제기하는 질문에 자동으로 답변하는 시스템                                     |
| sentiment-analysis            | 디지털 텍스트를 분석하여 메시지의 감정 톤이 긍정인지, 부정인지, 중립적인지를 결정하는 과정                 |
| summarization                 | 요약은 텍스트에서 참조되는 대부분 중요한 측면을 유지                                       |
| text-generation               | 텍스트를 생성하는것은 프롬프트를 제공하면 나머지 텍스트를 생성하여 자동으로 완성                        |
| translation                   | 텍스트 번역                                                              |
| zero-shot-classification      | 모델이 레이블이 지정된 예제 세트에 대해 학습된 다음 이전에 볼 수 없었던 클래스에서 새로운 예제를 분류할 수 있는 작업 |
### Mask filling
```
from transformers import pipeline

unmasker = pipeline("fill-mask")
# top_k=2 표시 개수
unmasker("This course will teach you all about <mask> models.", top_k=2)

# 응답 값은 <mask>에 적절한 답변을 넣어서 반환
```

### NER (Named entity recognition)
- 입력 텍스트의 어느 부분이 사람, 위치, 조직과 같이 엔티티에 해당하는지 찾는 작업
```
from transformers import pipeline

ner = pipeline("ner", grouped_entities=True)
ner("My name is Sylvain and I work at Hugging Face in Brooklyn.")
```
### Question Answering
질의 응답 파이프라인
```
from transformers import pipeline

question_answer = pipeline("question-answering")
question_answer(
question="Where do I work?",
context="My name is Sylvain and I work at Hugging Face in Brooklyn",
)
```

### Text generation
```
from transformers import pipeline

generator = pipeline("text-generation")
generator("In this course, we will teach you how to")

```

# Translation
- 번역
```
from transformers import pipeline

generator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
translator("Ce cours est produit par Hugging Face.")
```

### Zero-shot-classification
- 학습과정에서 본 적 없는 새로운 클래스를 인식하는 방식
```
from transformers import pipeline

classifier = pipeline("zero-shot-classification")
classifier(
"This is a course about the Transformers library",
candidate_labels=["education", "politics", "business"], # 3 개중 어느 카테고리로 분류할것인가
)
```

# Transformer Library로 파인튜닝
## Behind the pipeline에서 할 일
- Preprocessing with a tokenizer
	- 텍스트는 모델이 이해할 수 있는 형식으로 전처리
```
"""
1. 단어와 서브 단어, 심볼 등을 토큰으로 자름
2. integer와 토큰 매핑
3. 모델에 추가
"""
from transformers import AutoTokenizer

checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

raw_inputs = [
	"I've been waiting for a HuggingFace course my whole life.",
	"I hate this so much!",
]
inputs = tokenizer(raw_inputs, padding=True, truncation=True, return_tensors="pt")
print(inputs)
```
- Going through the model
	- 전처리 완료된 입력 테스트는 모델에 전달
```
# 1번 방법
from transformers import AutoModel
checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModel.from_pretrained(checkpoint)

# 2번 방법 - 원하는 모델 연결
"""
모델 리스트
- ForCausalLM 인과관련 모델
- ForMaskedLM
- ForMultipleChoice
- ForQuestionAnswering
- ForSequenceClassification 문장 분류 모델
- ForTokenClassification
"""
from transformers import AutoModelForSequenceClassification

checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
outputs = model(**inputs)

```
- Postprocessing the output
	- 모델이 예측한 결과는 후처리되어 사람이 이해할 수 있는 형태로 변환
```
model.config.id2label
```

## Models에서 할 일
- Creating a Transformer
```
# Bert Model 사용
from transformers import BertConfig, BertModel

# Config
config = BertConfig()

# Config를 모델에 연결
model = BertModel(config)
```
- Different loading methods
	- 위의 모델은 학습되지 않은 모델이므로 아래처럼 한번 학습된 모델을 사용하는 것을 권장한다.
```
from transformers import BertModel

model = Bertmodel.from_pretrained("bert-base-cased")
```
- Saving methods
```
model.save_pretrained("directory_on_my_computer")

ls directory_on_my_computer

```

## Tokenizers에서 할 일
- tokenizer 방식
	- Word-based : 일반적으로 몇 가지 규칙만 가지고도 설정 및 사용이 매우 쉬움. 단어로 나눔
	- Character-based : 단어가 아닌 문자로 나눔. -> 토큰이 작아짐.
	- Subword tokenization : 가장 많이 사용. 빈번하게 사용하는 단어는 더 작은 하위 단어로 분할하지 않고, 희귀 단어를 의미하는 하위 단어로 분할
- Loading and saving
```
from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-cased")
tokenizer.save_pretrained("directory_on_my_computer")
```
- Encoding
	- 텍스트를 숫자로 변환하는 과정
	- 토큰화, 입력 식별자 변환 2단계 프로세스 수행
		- 토큰이라 부르는 단어로 분리
		- 토큰화 결과인 토큰들을 숫자로 변환하여 텐서로 만들고, 이를 모델에 입력할 수 있도록 하는 것
```
from transformers import AutoTokenizer

tokenizer = Autotokenizer.from_pretrained("bert-base-cased")

sequence = "Using a Transformer network is simple"
tokens = tokenizer.tokenize(sequence)
print(tokens)

ids = tokenizer.convert_tokens_to_ids(tokens)
print(ids)
```
- Decoding
	- 변환된 입력 식별자(input IDs)를 이용하여 어휘집(vocabulary)에서 해당 문자열을 검색
```
decoded_string = tokenizer.decode([7993, 170, 11303, 1200, 2443, 1110, 3014])
print(decoded_string)
```