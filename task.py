import wikipedia
import random

list = wikipedia.search("python", results=5)

# list = []
# for i in range(n):
#     list=list.append()
# list = wikipedia.search("python", results=3)
print('list=', list)
print('===========================')

dict = {}
for i in list:
    try:
        url = wikipedia.page(i).url
        # print(wikipedia.page(i).url)
    except wikipedia.exceptions.DisambiguationError as e:
        s = random.choice(e.options)
        # url = wikipedia.page(s).url
        url = e.options
    except wikipedia.exceptions.PageError as e:
        url = 'page_error_exception'

    dict.update(
        {
            str(i): url
        }
    )

print('result:', dict)

print('===========================')
# for i in list:
#     try:
#         print(wikipedia.page(i).url)
#     except wikipedia.exceptions.DisambiguationError as e:
#         print('TEST:', e.options)
