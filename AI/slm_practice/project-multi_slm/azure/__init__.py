import os
import yaml
import openai

# Azure 사용 시
def get_auth():
    curr_dir = os.path.dirname(__file__)
    auth_path = os.path.join(curr_dir, 'auth.yml')
    auth = yaml.safe_load(open(auth_path, encoding='utf-8'))
    return auth

auth = get_auth()

# openai.api_type = "azure"
# openai.api_base = f"https://{auth['Azure_OpenAI']['name']}.openai.azure.com/"
# openai.api_version = "2024-02-15-preview"
# openai.api_key = auth['Azure_OpenAI']['key']


# OpenAI 바로 사용
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

