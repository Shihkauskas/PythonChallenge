import requests
from flask import Flask
from flask import render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def main():
    news = []
    all_news = []
    html = requests.get('http://habr.ru').text
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find_all('div', {'class': 'posts_list'})
    for zagolovok in div:
        post = zagolovok.find_all('h2', {'class': 'post__title'})
        for links in post:
            links = links.find_all('a')
            for link in links:
                link = link.get('href')
                news.append(link)
    for main_news in news:
        main_news = requests.get(main_news).text
        main_soup = BeautifulSoup(main_news, 'lxml')
        main_div = main_soup.find_all('article', {'class': 'post post_full'})
        for i in main_div:
            all_news.append(i)
    with open('templates/habr.html', 'w', encoding='utf8') as file:
        file.write(', '.join([str(i) for i in all_news]))

    return render_template('habr.html')
if __name__ == '__main__':
    app.run()
