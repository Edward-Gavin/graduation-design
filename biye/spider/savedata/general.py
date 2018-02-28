# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from biye.spider.method import index
from biye.spider.operate import database


def save_post_author():
    """
    # # # 获取所有的帖子的作者信息----->users
    :return:
    """
    homepages = database.select_all('postn''nickname')
    au_ids = database.select_sql('postn', 'au_id')
    for au_id, homepage in zip(au_ids, homepages):
        try:
            print(au_id, homepage)
            span_text = []
            print('http://tieba.baidu.com/home/main?un='+homepage[0])
            res = index.get_response('http://tieba.baidu.com/home/main?un='+homepage[0])
            soup = index.get_bs(res)

            abc = index.author_post_info(soup)
            abc.insert(0, au_id[0])
            database.insert_sql_users('users', abc)
        except AttributeError as why:
            continue
        except TypeError as why:
            continue
