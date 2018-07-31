import requests
from lxml import etree


def get_one_page(offset):
    url = 'http://maoyan.com/board/4'
    if offset != 0:
        url = url+'?offset='+offset
    headers = {
        'User-Agent':'Mozilla/5.0(Macintosh;IntelMacOSX10_11_4)AppleWebKit/537.36(KHTML,likeGecko)Chrome/52.0.2743.116Safari/537.36'
    }
    return requests.get(url, headers=headers).text


def parse_page(page, count):
    html = etree.HTML(page)
    divs = html.xpath("//div[@class='board-item-content']")
    for div in divs:
        summary = "".join(div.xpath('string(.)').strip()).replace('\n', '')
        name = summary[0: summary.index(' ')]
        actors = summary[summary.index('主演'):summary.index('上映时间')]
        show_time = summary[summary.index('上映时间'):summary.rindex(' ')]
        score = summary[summary.rindex(' '):]
        print('%d: %s  %s %s %s' % (count, name, actors, show_time, score))
        count += 1
        # print(str(i) + ' ----> ' + "".join(div.xpath('string(.)').strip()).replace('\n', ''))

if __name__ == '__main__':
    for i in range(0, 10):
        page = get_one_page(str(i*10))
        parse_page(page, 10*i+1)
