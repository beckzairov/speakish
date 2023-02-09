import json
import requests

app_id  = "3aa393a4"
app_key  = "afb8f5eed873e5411f00fb9b57e3f5fa"

endpoint = "entries"
language_code = "en-us"
word_id = "example"


def getDefinitions(word_id):
    url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()
    r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
    res = r.json()

    if 'error' in res.keys():
        return False

    output = {}
    senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for sense in senses:
        definitions.append(f"👉 {sense['definitions'][0]}")
    output['definitions'] = "\n".join(definitions)

    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][1].get('audioFile'):
        output['audio'] = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][1]['audioFile']

    return output

if __name__ == '__main__':
    from pprint import pprint as print
    print(getDefinitions('america'))