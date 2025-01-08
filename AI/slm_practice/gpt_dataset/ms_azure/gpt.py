import openai

class GPT():
    def __init__(self) -> None:

        self.engin = 'gpt-4o'
        self.temperature =0.7
        self.few_shot_examples = None

    def _generate(
            self,
            query: str = None,
            img_url: str = None
    ) -> str:
        
        messages = [{"role":"system","content":f"{self.system_message}"}]
        if self.few_shot_examples is not None:
            for example in self.few_shot_examples:
                messages.append({"role":"user","content": f"{example['user_message']}"})
                messages.append({"role":"assistant","content": f"{example['assistant_message']}"})
        
        if img_url is None:
            messages.append({"role":"user","content": f"{query}"})
        else :
            messages.append(
            {
            "role":"user", 
            "content": [
                            {
                                "type": "text",
                                "text" : query
                            }, 
                            {
                                "type": "image_url",
                                "image_url":{
                                    "url": img_url
                                }
                            }
                        ]
            }
            )


        try:
            response = openai.ChatCompletion.create(
                engine=self.engine,
                messages=messages,
                temperature=self.temperature,
            )['choices'][0]['message']['content']
            return response
        except (openai.error.RateLimitError, openai.error.Timeout) as e:
            print('OpenAI API RateLimitError Occured!!')
            return '[Error]'