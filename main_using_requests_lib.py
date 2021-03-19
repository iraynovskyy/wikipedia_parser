import json
import requests
from requests.exceptions import HTTPError


def wikipedia_search(word, limit):
    print(f'The word is: {word}, and limit: {limit}')
    dict = {}
    try:
        response = requests.get(
            f'https://en.wikipedia.org/w/api.php?action=opensearch&search={word}&limit={limit}&namespace=0&format=json')
        topic_list = json.loads(response.content)[1]
        url_list = json.loads(response.content)[3]

        for i in range(len(topic_list)):
            dict.update(
                {
                    str(topic_list[i]): url_list[i]
                }
            )
        return dict

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

    dict = {"result": "Nothing was added!"}
    return dict


data = wikipedia_search("car", 5)
print('data:', data)
