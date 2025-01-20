import torch
import os
from threading import Thread
from transformers import (
    AutoTokenizer, 
    AutoModelForCausalLM,
    BitsAndBytesConfig,
    TextIteratorStreamer
)

class Inference:
    def __init__(self) -> None:

        config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
        )

        self.tokenizer = AutoTokenizer.from_pretrained(
            "beomi/Llama-3-Open-Ko-8B-Instruct-preview", 
            load_in_4bit=True
        )
        fp = os.path.join(os.path.dirname(__file__), 'outputs/checkpoint-1600')
        self.model = AutoModelForCausalLM.from_pretrained(
            fp, 
            torch_dtype="auto",
            device_map="cuda:0",
            quantization_config=config
        )
        
        self.terminators = [
            self.tokenizer.eos_token_id,
            self.tokenizer.convert_tokens_to_ids("<|eot_id|>")
        ]
        
        self.streamer = TextIteratorStreamer(
            self.tokenizer, 
            skip_prompt=True, 
            skip_special_tokens=True
        )

    def _generate(
        self,
        system_prompt: str,
        fewshot_prompt: list,
        context_prompt: str,
        question_prompt: str,
        keyword: str,
        args: dict
    ) -> str:

        messages = [
            {"role": "system", "content": f"{system_prompt}"}
        ]
        for example in fewshot_prompt:
            messages.append(
                {"role": "user", "content": f"{example['user_message']}"}
            )
            messages.append(
                {"role": "assistant", "content": f"{example['assistant_message']}"}
            )
        messages.append(
            {"role": "user", "content": f"###Context:{context_prompt}\n###Keyword:{keyword}\n###Question:Context에 따르면, {question_prompt}"}
        )

        print(f"final prompt : {messages}")

        input_ids = self.tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            return_tensors="pt"
        ).to(self.model.device)

        generate_kwargs = dict(
            input_ids=input_ids,
            streamer=self.streamer,
            do_sample=True,
            no_repeat_ngram_size=3
        )
        generate_kwargs.update(args)

        print(f"generate_kwargs : {generate_kwargs}")

        t = Thread(target=self.model.generate, kwargs=generate_kwargs)
        t.start()

        for new_token in self.streamer:
            yield new_token
