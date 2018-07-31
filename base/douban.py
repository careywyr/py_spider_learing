import requests
from lxml import etree

URL = 'https://movie.douban.com/chart'


def get_one_page():
    response = requests.get(URL)
    return response.text


def parse_html(text):
    html = etree.HTML(text)
    result = html.xpath("//div[@class='pl2']//a//text()")
    formatResult = []
    for index, a in enumerate(result):
        movie = a.strip()
        try:
            if '/' in movie and (movie.index('/') == len(movie)-1):
                movie = movie[0:movie.index('/')-1].strip()
        except:
            continue
        formatResult.append(movie)
    moviechart = "/".join(formatResult).split("//")
    moviechart[len(moviechart)-1] = moviechart[len(moviechart)-1][:-1]
    for value in moviechart:
        print(value)


if __name__ == '__main__':
    text = get_one_page()
    parse_html(text)
