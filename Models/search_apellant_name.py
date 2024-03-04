import requests

api_key = 'YOUR_API_KEY'

appellant_name = 'Miranda'

search_url = 'https://www.courtlistener.com/api/rest/v3/search/'

headers = {
    'Authorization': f'Token {api_key}'
}

# SEARCHING QUERY
params = {
    'type': 'o',  # 'o' stands for opinions
    'q': f'"appellant_name": "{appellant_name}"'
}

response = requests.get(search_url, headers=headers, params=params)

if response.status_code == 200:
    results = response.json()
    print("Got em")
    print("Search results:", results)
else:
    print("An error occurred:", response.status_code, response.text)
