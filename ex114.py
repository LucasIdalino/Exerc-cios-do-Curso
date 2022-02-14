import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except urllib.error.URLError:
    print(f'O site não está acessível.')
else:
    print(f'O site está acessível.')
