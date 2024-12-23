import requests

headers = {"Authorization": "Bearer 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"}
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
data = query(
    {
        "inputs": "The tower is 324 meters (1,063 ft) tall, about the same height as an 81-strorey building, and the tallest structure in Paris. Its base is sqaure, measuring 125 meters (410 ft) on each side."
        , "parameters": {"do_sample": False},
    }
)
print(data)