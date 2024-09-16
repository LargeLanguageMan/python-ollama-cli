import requests
import json

def get_response(model, prompt):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model,
        "prompt": prompt
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)
    all_chunks = []
    for chunk in response.iter_lines():
            if chunk:
                    decoded_data = json.loads(chunk.decode('utf-8'))
                    all_chunks.append(decoded_data)
    return all_chunks

if __name__ == "__main__":
    model = input("Enter model name (e.g., llama3.1): ")
    prompt = input("Enter your prompt: ")
    result = get_response(model, prompt)
    box = ""
    for response in result:
        box = box + response["response"]
    print(box)
