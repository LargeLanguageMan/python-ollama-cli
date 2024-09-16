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
    for chunk in response.iter_lines():
        decoded_chunk = chunk.decode('utf-8')  # Decode the byte string
        json_chunk = json.loads(decoded_chunk)  # Parse the JSON data
        print(json_chunk["response"], end="", flush=True) 
if __name__ == "__main__":
    model = input("Enter model name (e.g., llama3.1): ")
    prompt = input("Enter your prompt: ")
    result = get_response(model, prompt)
    print("Waiting for model response...")
