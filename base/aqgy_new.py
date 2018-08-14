import requests
from lxml import etree
import json as js


def get_one_page(start):
    start = i * 20
    print("----------------------第%s页--------------------" % (i+1))
    url = 'https://movie.douban.com/subject/24852545/comments?start='+str(start)+'&limit=20&sort=new_score&status=P'
    response = requests.get(url)
    return response.text


def parse_page(page):
    html = etree.HTML(page)
    comments = html.xpath("//div[@class='comment']")
    # score = html.xpath("//div[@class='comment']//h3//span[@class='comment-info']//span[contains(@class,'rating')]/@title")
    for comment in comments:
        text = comment.find(path="p").find(path="span[@class='short']").text
        score = comment.find(path="h3").find(path="span[@class='comment-info']").findall(path="span")[1].get('title')
        print('%s %s' % (text,score))


if __name__ == '__main__':
    for i in range(0, 11):
        page = get_one_page(i)
        parse_page(page)



