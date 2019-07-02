# -*- coding: utf-8 -*-
"""
@file    : chandao.py.py
@date    : 2019-06-19
@author  : carey
"""

import requests
from lxml import etree
from pyquery import PyQuery as pq

unresolved_url = 'http://192.168.2.194/zentao/bug-browse-1-0-unresolved-0--38-20-1.html'
headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
        'Cookie': 'lang=zh-cn; device=desktop; theme=default; keepLogin=on; za=wuyeran; lastProduct=1; preBranch=0; preProductID=1; ajax_quickJump=on; zp=84904f1e55399c4041bdc5dfbc64f56fbfa40232; checkedItem=; ajax_lastNext=on; bugModule=0; qaBugOrder=openedDate_asc; selfClose=1; windowHeight=968; windowWidth=1905; zentaosid=sg8s2baqrhug460ngl33snimv7; OUTFOX_SEARCH_USER_ID_NCOO=1542708121.633844'
    }

def get_list():
    text = requests.get(unresolved_url, headers=headers).text
    html = etree.HTML(text)
    # bug_list = html.xpath("//tbody/tr[@class='text-center']/td[@class=' text-left']")
    # for bug in bug_list:
    #     print(bug.xpath("@title")[0])
    bug_list = html.xpath("//tbody/tr[@class='text-center']")
    for bug in bug_list:
        name = bug.xpath("td")
        print(name)


def get_list_by_pyquery(name=None, priority=None, id=None,):
    doc = pq(unresolved_url, headers=headers)
    trs = doc('tbody tr')
    bug_list = []
    for item in trs.items():
        id = item.children().eq(0).find('input').val()
        priority = item.children().eq(1).find('span').text()
        desc = item.children('.text-left').text()
        creator = item.children().eq(5).text()
        dealer = item.children().eq(7).text()
        bug = [id, priority, desc, creator, dealer]
        bug_list.append(bug)
    for bug in bug_list:
        print(bug)


if __name__ == '__main__':
    # get_list()
    get_list_by_pyquery()