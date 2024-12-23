# 공통코드
import requests
import os
from dotenv import load_dotenv

load_dotenv()
def query(MODEL_URL, payload):
    headers = {"Authorization": f"Bearer {os.environ.get('HUGGING_FACE_KEY')}"}
    response = requests.post(f"https://api-inference.huggingface.co/models/{MODEL_URL}", headers=headers, json=payload)
    return response.json()
    