import requests

url = 'http://localhost:80/predict'  # Replace with the actual URL of your FastAPI endpoint

# Define the request body data
body_data = {
  "user_input": {
    "text": "hello"
  },
  "chat_history": {
    "list": [
 
    ]
  }
}

response = requests.post(url, json=body_data)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")