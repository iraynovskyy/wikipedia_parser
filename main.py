import wikipedia


def wikipedia_search(word, limit):
    print(f'The word is: {word}, and limit: {limit}')
    list = wikipedia.search(word, results=limit)
    print('list:', list)
    dict = {}
    for i in list:
        try:
            result = wikipedia.page(i).url
        except wikipedia.exceptions.DisambiguationError as e:
            result = e.options
        except wikipedia.exceptions.PageError as e:
            result = f'Page id "{i}" does not match any pages. Try another id!'

        dict.update(
            {
                str(i): result
            }
        )
    return dict


data = wikipedia_search("Bob", 25)
print('data:', data)
