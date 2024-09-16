import requests
import json

def get_response(model, prompt):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

if __name__ == "__main__":
    model = input("Enter model name (e.g., llama3.1): ")
    prompt = input("Enter your prompt: ")
    result = get_response(model, prompt)
    print("Waiting for model response...")
    print(result['response'])
