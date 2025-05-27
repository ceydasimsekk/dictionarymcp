import requests

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        meanings = data[0]["meanings"]
        definitions = [m["definitions"][0]["definition"] for m in meanings]
        return definitions
    else:
        return ["Definition not found."]
