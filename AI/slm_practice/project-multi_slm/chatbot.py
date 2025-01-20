import time
import gradio as gr
import json
from threading import Thread
import yaml
import os
import re
from azure.gpt.orch import Orch
from azure.bing_search.news import News
from azure.bing_search.web import Web
# from azure.cognitive_search.ai_search import AISearch
# from huggingface.inference_Llama3 import Inference


def run(message, history):

    print(f"message : {message}")
    print(f"history : {history}")
    print("\n=============================================\n")
    
    agent, keyword = Module._orch_generate(message, history)

    if "Document" in agent:
        file_name = agent.split('Document:')[1].strip()
        print(f"file name : {file_name}")
        search_results = Retrieval._aisearch(
            keyword=keyword,
            file_name=file_name,
            count=max_search_document.value
        )

    elif agent == "Web agent":
        search_results, urls, titles = Retrieval._websearch(
            keyword=keyword,
            count=max_search_document.value
        )
    
    elif agent == "News agent":
        search_results, urls, titles = Retrieval._newssearch(
            keyword=keyword,
            count=max_search_document.value
        )

    print(f"search_results : {search_results}")
    print("\n=============================================\n")
    
    args = {
        "temperature" : temperature.value,
        "top_p" : top_p.value,
        "top_k" : top_k.value,
        "max_new_tokens" : max_new_tokens.value
    }
    
    response = ''
    for token in Module._response_generate(
        message=message,
        search_results=search_results,
        agent=agent,
        keyword=keyword,
        args=args
    ):
        response += token
        yield response
    
    if (agent == "Web agent") or (agent == "News agent"):
        for url, title in zip(urls, titles):
            response += "\n"
            response += HTMLGenerator.href_link(
                name=title[:20],
                url=url
            )
            yield response

def update_value(val, component_name):  
    component = globals()[component_name]  
    component.value = val  
    return f'Value is set to {val}'  

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=3): 
            gr.Markdown("<h1>🛸 나만의 업무 AI 비서</h1>") 
            chat1 = gr.ChatInterface(  
                fn=run,  # 채팅 봇 함수  
                multimodal=True,  # 멀티모달 지원  
                fill_height=True,  # 높이 자동 조정  
                theme="soft",  # 테마 설정  
                # clear_btn="Clear 🗑",  # 클리어 버튼 텍스트  
                examples=[
                    {"text": "삼성전자 뉴스 찾아줄래?"}, 
                    {"text": "이 문서 요약해줘"}
                ] # 예제 입력  
            )

        with gr.Column(scale=1):
            with gr.Row():
                # 파라미터 설정 섹션의 제목 추가
                gr.Markdown("<h3 style='margin-top: 10px'>Model Parameters</h3>")  

            # 모델 선택을 ㅜ이한 드롭다운 메뉴 추가
            model = gr.Dropdown(
                value="Llama3(Ours)",   
                choices=["Llama3(Ours)", "GPT-3.5", "GPT-4"],   
                label="Model",   
                info="Choose a model",   
                interactive=False  
            )

            # Temperature 슬라이더 추가
            temperature = gr.Slider(
                value=0.7,
                maximum=1.0,
                label="Temperature",
                interactive=True,
                info="""The value used to modulate the newx token probabilities."""
            )

            temperature.change(
                fn=update_value,
                inputs=[temperature, gr.State('temperature')]
            )

              # Top-p 슬라이더를 추가 
            top_p = gr.Slider(  
                value=0.7,  
                maximum=1.0,  
                label="Top-p",  
                interactive=True,  
                info="""If set to float < 1, only the smallest set of most probable tokens   
                with probabilities that add up to top_p or higher are kept for generation."""  
            )

            top_p.change(  
                fn=update_value,  
                inputs=[top_p, gr.State('top_p')]
            ) 
              
            # Top-k 슬라이더를 추가
            top_k = gr.Slider(  
                minimum=1,  
                value=50,  
                maximum=100,  
                step=1,  
                label="Top-k",  
                interactive=True,  
                info="""The number of highest probability vocabulary tokens to keep for top-k-filtering."""  
            )

            top_k.change(  
                fn=update_value,  
                inputs=[top_k, gr.State('top_k')]
            ) 
            
            # Max new tokens 슬라이더를 추가 
            max_new_tokens = gr.Slider(  
                minimum=50,  
                value=512,  
                maximum=2000,  
                step=1,  
                label="max_new_tokens",  
                interactive=True,  
                info="""This parameter controls the maximum number of new tokens   
                to be generated in each step of the model's output.  
                A lower value will result in shorter responses from the model."""  
            )

            max_new_tokens.change(  
                fn=update_value,  
                inputs=[max_new_tokens, gr.State('max_new_tokens')]
            ) 
              
            # Max search document 슬라이더를 추가 
            max_search_document = gr.Slider(  
                minimum=1,  
                value=3,  
                maximum=5,  
                step=1,  
                label="max_search_document",  
                interactive=True,  
                info="""This parameter determines the max number of documents to be 
                considered during the search process when the model is looking 
                for information to generate the output. Higher values may result 
                in more diverse but possibly less focused responses."""
            )

            max_search_document.change(  
                fn=update_value,  
                inputs=[max_search_document, gr.State('max_search_document')]
            ) 
    
if __name__ == "__main__":
    demo.queue()
    demo.launch(share=True,allowed_paths=["."])




