# -*- coding: utf-8 -*-
"""
@file    : spider_man.py
@date    : 2019-07-01
@author  : carey
"""

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import requests
from lxml import etree
import jieba


def go():
    comment_list = []
    for x in range(0, 50):
        url = 'https://movie.douban.com/subject/26931786/comments?start={}&limit=20&sort=new_score&status=P'.format(x*20)
        text = requests.get(url).text
        html = etree.HTML(text)
        result = html.xpath("//div[@class='comment']//p//span/text()")
        if len(result) > 0:
            for comment in result:
                comment_list.append(comment)
    join = "".join(comment_list)
    jieba.suggest_freq(('钢铁侠'), True)
    cut_text = " ".join(jieba.cut(join))
    stopwords = set(STOPWORDS)
    stopwords.add('一部')
    stopwords.add('就是')
    stopwords.add('还是')
    stopwords.add('一个')
    stopwords.add('不过')
    stopwords.add('电影')
    wordcloud = WordCloud(stopwords=stopwords, background_color="white", width=1000, font_path='simsun.ttc', height=860, margin=2).generate(cut_text)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    go()

