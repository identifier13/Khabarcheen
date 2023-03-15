import requests
from bs4 import BeautifulSoup

# 9to5linux.com


def nineto5linux():
    url = 'https://9to5linux.com/'
    res = requests.get(url)
    data = BeautifulSoup(res.content, 'html.parser')

    news = data.find('div', {'class': 'content-area'}
                     ).find('article').find('div', {'class': 'post-thumbnail'})

    url_post = news.find('a')['href']
    text = news.find('img')['alt']
    image = news.find('img')['src']

    return url_post, text, image


# OMGLinux.com


def omg_linux():
    url = 'https://www.omglinux.com/news/'
    res = requests.get(url)
    data = BeautifulSoup(res.content, 'html.parser')

    news = data.find('div', {'class': 'content-area'}).find('article')

    url_post = news.find(
        'div', {'class': 'post-thumbnail'}).find('a')['href']
    text = news.find(
        'header', {'class': 'entry-header'}).find('h3').text
    image = news.find(
        'div', {'class': 'post-thumbnail'}).find('img')['src']

    return url_post, text, image


# ITSFOSS.com


def itsfoss():
    url = 'https://itsfoss.com/blog/'
    res = requests.get(url)
    data = BeautifulSoup(res.content, 'html.parser')

    news = data.find('main', {'class': 'main'}).find(
        'div', {'class': 'container'}).find('article', {'class': 'post-card'})

    url_post = news.find('a')['href']
    text = news.find('h2', {'class': 'post-card__title'}).find('a').text
    image = 'https://itsfoss.com' + \
        news.find('picture').find('img')['src'].replace('/size/w30', '')

    return url_post, text, image


# OMGUbuntu.com


def omg_ubuntu():
    url = 'https://www.omgubuntu.co.uk/'
    res = requests.get(url)
    data = BeautifulSoup(res.content, 'html.parser')

    news = data.find('div', {"class": "tile-layout__item"}
                     ).find('div', {'class': 'tile-layout__image'}).find('a')

    url_post = news['href']
    text = news['aria-label']
    image = news.find('img')['src']

    return url_post, text, image
