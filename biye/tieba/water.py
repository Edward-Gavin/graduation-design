# !/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
通过对贴吧中会员用户的调查发现，确实有很大一批水军在其中，它们的具体表现形式为
相似账号说明：
    类型一：随机数用户。（可能是生成的随机数加密后取的前几位）
    类型二：昵称中，某些字段是一样的，但是其他一个字或编号不同。

在数据库中，可以很明显的看到它们的相似性。

本模块主要是分析贴吧中水军的模块，包含判断水军的函数，如果另外添加函数，包含在此。

主要是用正则表达式进行匹配，数量超过阈值，则认为水军军队。

"""
import re


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


#
# import requests
# from bs4 import BeautifulSoup
#
# if __name__ == '__main__':
#     reponse = requests.get('http://tieba.baidu.com/home/main?un=%B1%A6%B1%A6%B5%C4%D0%A1%B0%D7%CA%F37')
#     print(reponse)
#     bs = BeautifulSoup(reponse.text, 'lxml')
#     post = zero_post(bs)
#     print(post)
