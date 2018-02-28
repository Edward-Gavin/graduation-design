# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from biye.spider.operate import database
from biye.spider.operate import formatfile


def statistic_post():
    """
    判断用户的活跃度，活跃等级为七级, 以用户的发帖数为判断标准
    :return:
    """
    posts = database.select_all('pure_users', 'post_number')
    active = {
        "0-20": 0,
        "20-100": 0,
        "100-500": 0,
        "0.5K-1K": 0,
        "1K-5K": 0,
        "5K-10K": 0,
        "10K+": 0
    }

    for post in posts:
        try:
            if post[0][-1] == '万':
                post_int = float(post[0][:-1]) * 10000
            else:
                post_int = int(post[0])
            if 0 <= post_int < 20:
                active["0-20"] += 1
            elif 20 <= post_int < 100:
                active["20-100"] += 1
            elif 100 <= post_int < 500:
                active["100-500"] += 1
            elif 500 <= post_int < 1000:
                active["0.5K-1K"] += 1
            elif 1000 <= post_int < 5000:
                active["1K-5K"] += 1
            elif 5000 <= post_int < 10000:
                active["5K-10K"] += 1
            else:
                active["10K+"] += 1
        except ValueError as why:
            pass
    return active
revi = statistic_post()
formatfile.dict_to_json(revi, '../../show/data/post.json')
