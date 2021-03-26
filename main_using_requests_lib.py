import json
import requests
import argparse
from requests.exceptions import HTTPError
import logging

# logging level set to INFO
logging.basicConfig(format='%(message)s',
                    level=logging.INFO)

LOG = logging.getLogger(__name__)


def wikipedia_search(word, limit):
    LOG.info(f'--- entered word is: {word}')
    LOG.info(f'--- entered limit is: {limit}')
    try:
        response = requests.get(
            f'https://en.wikipedia.org/w/api.php?action=opensearch&search={word}&limit={limit}&namespace=0&format=json')
        assert response.status_code == 200, f'Status_code should be 200 but it is {response.status_code}!'

        resp = response.json()
        topic_list = resp[1]
        url_list = resp[3]

        dict = {str(topic_list[i]): url_list[i] for i in range(len(topic_list))}
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

    LOG.info(f'--- data: {data}')
