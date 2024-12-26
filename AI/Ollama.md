- 오픈소스 LLM을 로컬에서 쉽게 실행할 수 있게하는 도구
- Mistral, Llama3 등다양한 오픈 소스 LLM 지원
- 모델 가중치, 설정, 데이터 셋을  하나의 패키지로 묶어 Modefile로 관리

## 소스
https://github.com/twer4774/TIL/blob/master/AI/slm_practice/ollama_exam/ollama_exam.ipynb

## Ollama 정의
- Ollama에 모델 추가
- Modefile로 관리
	- Ollama에 올리기 위해 페르소나, 템플릿 등을 정의
### 실행 방법
- gguf 파일 다운로드
- Modefile 작성
```
FROM ggml-model-Q4_K_M.gguf

TEMPLATE """{{- if .System }}
<s>{{ .System }}</s>
{{- end }}
<s>Human:
{{ .Prompt }}</s>
<s>Assistant:
"""

SYSTEM """A chat between a curious user and an atificial intelligence assistant."""

PARAMETER temperature 0.1

PARAMETER stop "<s>"
PARAMETER stop "</s>"
```
- Ollama 실행
```
ollama create ggml-model-Q4_K-M.gguf -f Modefile

ollama list

ollama run ggml-model-Q4_K_M.gguf
```