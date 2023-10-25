from bs4 import BeautifulSoup
from random import choice
import requests


desktop_agents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    'Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko)'
    ' Version/10.0.1 Safari/602.2.14',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']



def random_headers():
    return {'User-Agent': choice(desktop_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

URL = "https://dota2.ru/news/updates/" 
MAIN_URL = "https://dota2.ru/"

articles = []
additional_links = []

def ParsingNews():
    page = requests.get(URL, headers=random_headers())
    soup = BeautifulSoup(page.text, "html.parser")
    page_tree = soup.find("ul", class_="index__news-list js-news-list")
    if page_tree is not None:
        new_page_tree = page_tree.find_all(class_='index__news-link game-icon js-game-icon')
        for item in new_page_tree:
            link = MAIN_URL + item.get('href')
            update_neme = item.find('div', class_='index__news-name').text.replace('\r', '').replace('\n', '').replace('\t', '')
            additional_links.append([update_neme, link])
    else:
        additional_links.append('')
    
    global_news = additional_links
    pnews = ''
    for i in range(len(global_news)):
        pnews += f'{i + 1}. [{global_news[i][0].replace("[", "").replace("]", "")}]({global_news[i][1]})\n'
    
    return pnews


