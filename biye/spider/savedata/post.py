# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from biye.spider.method import index
from biye.spider.operate import database


def save_source_post():
    """
    # 以下代码将所有的大学吧中的帖子的标题和主页插入到数据库----->source1
    :return:
    """
    pages = index.get_page(50, 5000)
    for page in pages:
        print(page)
    for i in range(1, 3000):
        print(i * 50 + 233750)
        response = index.get_response_with_headers(index.URL_F, kw='大学', ie='utf-8', pn=i * 50 + 233750)
        print(response.request.url)
        res_soup = index.get_bs(response=response)
        # print(res_soup)
        titleList = index.get_post_homepage(res_soup)
        # print(titleList)
        for title in titleList:
            database.insert_sql_source1('source1', title)


def save_detail_post():
    """
    # # #以下代码分析帖子主页，提取需要的数据----->postn
    :return:
    """
    selectResult = database.select_all('source1', 'homepage')
    for home in selectResult:
        homeUrl = ''.join(home)
        print(homeUrl)
        response = index.get_response(homeUrl)

        try:
            post = index.post_info(index.get_bs(response))
            post.insert(0, homeUrl)
            print(post)
            database.insert_sql_post('postn', post)
        except AttributeError as why:
            continue
        except KeyError as why:
            continue

