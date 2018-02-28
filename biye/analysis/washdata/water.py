# !/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
通过对贴吧中会员用户的调查发现，确实有很大一批水军在其中，它们的具体表现形式为
相似账号说明：
    类型一：随机数用户。（可能是生成的随机数加密后取的前几位）
    类型二：昵称中，某些字段是一样的，但是其他一个字或编号不同。
    类型三：发帖和评论为零的用户，所谓的僵尸用户

在数据库中，可以很明显的看到它们的相似性。

本模块主要是分析贴吧中水军的模块，包含判断水军的函数，如果另外添加函数，包含在此。

主要是用正则表达式进行匹配，数量超过阈值，则认为水军军队。

"""
import re
from biye.spider.operate import database
from biye.spider.method import index


def analyze_member_random(name):
    """

    :param name: 会员nickname
    :return: 匹配返回1， 否则返回0
    """
    pattern = re.compile(r'^[A-Z]\S{3}\d\S\d\S{5}\d$')
    if pattern.match(name):
        return 1
    else:
        return 0


def analyze_member_str(name):
    """

    :param name: 会员nickname
    :return: 匹配返回1， 否则返回0
    """
    pattern = re.compile(r'^[\u4e00-\u9fa5]{5}[A-Z][a-z]$')
    if pattern.match(name):
        return 1
    else:
        return 0


def zero_post(soup):
    div = soup.find('div', class_='userinfo_userdata')
    span = div.find_all('span')
    if span[3].get_text() == '发贴:0':
        return 1
    else:
        return 0


# 水贴
def standard_water():
    """
    获取所有的水贴信息，判定条件为评论数小于等于5
    :return: a list contain water post.
    """
    reviews = database.select_all('postn', 'review_num')
    titles = database.select_all('postn', 'post_home')
    water_post = []
    for review, title in zip(reviews, titles):
        if int(review[0]) <= 5:
            water_post.append(title[0])
    return water_post


def zombie_member():
    """
    # 获取僵尸会员用户
    :return: 僵尸用户数
    """
    zombie_user = 0
    urls = database.select_all('sortmember', 'homepage')
    for url in urls:
        print(url)
        res = index.get_response(url[0])
        soup = index.get_bs(res)
        data = index.author_post_info(soup)
        if data == 0:
            zombie_user += 1
    return zombie_user


if __name__ == '__main__':
    standard_water()