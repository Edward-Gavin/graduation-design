# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from biye.spider.operate import database
from biye.spider.operate import formatfile


def statistic_sex():
    """
    Return the number of boys, girls and unknow.

    :return:
    """
    sexes = database.select_all('pure_users', 'sex')
    boys = 0
    girls = 0
    for sex in sexes:
        for one in sex:
            if str(one) == 'female':
                girls += 1
            else:
                boys += 1
    return boys, girls

boy, girl = statistic_sex()
static = {"boys": boy, "girls": girl}
formatfile.dict_to_json(static, name='../../show/data/sex.json')
