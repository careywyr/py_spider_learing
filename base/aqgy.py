import requests
from lxml import etree


def get_one_page(start):
    start = i * 20
    print("----------------------第%s页--------------------" % (i+1))
    url = 'https://movie.douban.com/subject/24852545/comments?start='+str(start)+'&limit=20&sort=new_score&status=P'
    response = requests.get(url)
    return response.text


def parse_page(page):
    html = etree.HTML(page)
    comments = html.xpath("//div[@class='comment']//p//span//text()")
    score = html.xpath("//div[@class='comment']//h3//span[@class='comment-info']//span[contains(@class,'rating')]/@title")
    print(len(comments),len(score))
    for i in range(0,  len(comments)):
        try:
            print('%s  %s' % (comments[i], score[i]))
        except:
            pass


if __name__ == '__main__':
    for i in range(0, 11):
        page = get_one_page(i)
        parse_page(page)



