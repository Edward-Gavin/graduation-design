# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from biye.spider.method import index
from biye.spider.operate import database


def get_all_members(start, end):
    """
    # # 以下代码提取本贴吧中所有的会员信息 昵称，主页，本吧中的等级 ----->sortmember
    :param start:
    :param end:
    :return:
    """
    for page in range(start, end):
        url = index.build_url(index.MEMBER_URL, page=page)
        print(url)
        response = index.get_response(url)
        soup = index.get_bs(response)
        member_list = index.member_info(soup)
        print(member_list)
        for member in member_list:
            database.insert_sql_member('sortmember', member)


def get_detail_member():
    """
    # 获取member详细信息----->member_detail
    :return:
    """
    urls = database.select_all('sortmember', 'homepage')
    for url in urls:
        print(url)
        res = index.get_response(url[0])
        soup = index.get_bs(res)
        data = index.author_post_info(soup)
        if data != 0:
            database.insert_sql_member_detail('member_detail', data)


if __name__ == '__main__':
    get_detail_member()