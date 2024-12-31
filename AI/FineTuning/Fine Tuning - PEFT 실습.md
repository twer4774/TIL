## PEFT란
- Parameter Efficient Fine-Tuning 
- LLM의 대부분의 파라미터를 프리징 한 후 일부의 파라미터만을 파인튜닝

## 1. requirements 설치
```
!pip install -q bitsandbytes datasets accelerate loralib
!pip install -q git+https://github.com/huggingface/transformers.git@main git+https://github.com/huggingface/peft.git
```
## 2. 모델 불러오기
``` python
#!pip install torch --upgrade

import torch
print("PyTorch version:", torch.__version__)
print("CUDA 사용 가능:", torch.cuda.is_available())
print("현재 GPU:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "None")
```

```python
import os 

os.environ["CUDA_VISIBLE_DEVICES"]="0"
import torch
import torch.nn as nn
import bitsandbytes as bnb
from transformers import AutoTokenizer, AutoConfig, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(
	"facebook/opt-6.7b",
	load_in_8bit=True,
	device_map='auto',
)

tokenizer = AutoTokenizer.from_pretrained("facebook/opt-6.7b")
```
## 3. 모델에서 후처리
	- 특정 레이어만 튜닝하기 위해 전체 잠금
``` python
for param in model.parameters():
	param.requires_grad = False # freeze the model - train adapters later
	if param.ndim == 1:
		# cast the small parameters (e.g. layernorm) to fp32 for stability
		param.data = param.data.to(torch.float32)
model.gradient_checkpointing_enable() # reduce number of stored activations
model.enable_input_require_grads()
  

class CastOutputToFloat(nn.Sequential):
	def forward(self, x): return super().forward(x).to(torch.float32)
model.lm_head = CastOutputToFloat(model.lm_head)
```

## 4. LoRA 적용
``` python
def print_trainable_parameters(model):

	"""
	Prints the number of trainable parameters in the model.
	"""

	trainable_params = 0
	all_param = 0
	for _, param in model.named_parameters():
		all_param += param.numel()
	
		if param.requires_grad:
			trainable_params += param.numel()

	print(
	f"trainable params: {trainable_params} || all params: {all_param} || trainable%: {100 * trainable_params / all_param}"
	)
```

``` python
from peft import LoraConfig, get_peft_model

config = LoraConfig(
	r=16,
	lora_alpha=32,
	target_modules=["q_proj", "v_proj"],
	lora_dropout=0.05,
	bias="none",
	task_type="CAUSAL_LM"
)

model = get_peft_model(model, config)
print_trainable_parameters(model)
```
## 5. 학습
``` python
import transformers

from datasets import load_dataset

data = load_dataset("Abirate/english_quotes")
data = data.map(lambda samples: tokenizer(samples['quote']), batched=True)

trainer = transformers.Trainer(
	model=model,
	train_dataset=data['train'],
	args=transformers.TrainingArguments(
	per_device_train_batch_size=4,
	gradient_accumulation_steps=4,
	warmup_steps=100,
	max_steps=200,
	learning_rate=2e-4,
	fp16=True,
	logging_steps=1,
	output_dir='outputs'
),
	data_collator=transformers.DataCollatorForLanguageModeling(tokenizer, mlm=False)
)

model.config.use_cache = False # silence the warnings. Please re-enable for inference!
trainer.train()
```

## 6. 허깅페이스 허브와 공유
``` python
from huggingface_hub import notebook_login

notebook_login()
```

``` python
model.push_to_hub("wonik-hi/opt-6.7b-lora", use_auth_token=True)
```
## 7. 허깅페이스 허브에서 로드
``` python
import torch
from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM, AutoTokenizer

peft_model_id = "wonik-hi/opt-6.7b-lora"
config = PeftConfig.from_pretrained(peft_model_id)
model = AutoModelForCausalLM.from_pretrained(
	config.base_model_name_or_path, return_dict=True, load_in_8bit=True, device_map='auto',
	llm_int8_enable_fp32_cpu_offload=True
)
tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)
  
# Load the Lora model
model = PeftModel.from_pretrained(model, peft_model_id)
```

``` python
# 질의
batch = tokenizer("Two things are infinite: ", return_tensors='pt')
with torch.cuda.amp.autocast():
	output_tokens = model.generate(**batch, max_new_tokens=50)

print('\n\n', tokenizer.decode(output_tokens[0], skip_special_tokens=True))
```

