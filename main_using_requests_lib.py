import json
import requests
import argparse
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
    except KeyError as e:
        print(f'KeyError occurred: {e}. Check if you entered all input data correctly (str, int).')
    except Exception as err:
        print(f'Other error occurred: {err}')

    dict = {"result": "Something went wrong! Exception occurred! Try [-h] or [--help] for help."}
    return dict


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process two parameters (str, int)')
    parser.add_argument('--word', type=str,
                        help='Input word (type=str) which topic of wikipedia page should contain')
    parser.add_argument('--limit', type=int,
                        help='Input items limit (type=int) in output dictionary')

    args = parser.parse_args()
    data = wikipedia_search(args.word, args.limit)

    print('data:', data)
