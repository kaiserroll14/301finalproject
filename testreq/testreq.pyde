import requests

def setup():
    size(500, 500)
    get_url()
    return

def draw():
    rect(25, 25, 25, 25)
    return

def get_url():
    r = requests.get('http://52.38.78.108/data.php')
    print(r.text)
    return