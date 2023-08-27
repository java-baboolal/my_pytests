
import requests

def add(a,b):
    return a+b

def len_joke():
    print('len_joke invoked.')
    joke = get_joke()
    print(joke)
    return len(joke)

def get_joke():
    #url = 'https://pokeapi.co/api/v2/pokemon'
    url = 'https://official-joke-api.appspot.com/random_joke'

    response = requests.get(url)

    if response.status_code == 200:
        setup = response.json()['setup']
        punchline = response.json()['punchline']
        joke = 'question : ' +setup +'\nand\nanswer : '+punchline
    else:
        joke = 'No jokes'

    print('get_joke invoked.')
    return joke


if __name__ == '__main__':
    print(get_joke())

