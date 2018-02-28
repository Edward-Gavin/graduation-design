# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from biye.spider.operate import database
from biye.spider.operate import formatfile


def statistic_review():
    """
    统计post回复数据
    :return:
    """
    quality = {
        "0-5": 0,
        "5-50": 0,
        "50-100": 0,
        "0.1K-0.5K": 0,
        "0.5K-1K": 0,
        "1K+": 0
    }
    reviews = database.select_all("postn", "review_num")
    for review in reviews:
        if 0 <= int(review[0]) < 5:
            quality["0-5"] += 1
        elif 5 <= int(review[0]) < 50:
            quality["5-50"] += 1
        elif 50 <= int(review[0]) < 100:
            quality["50-100"] += 1
        elif 100 <= int(review[0]) < 500:
            quality["0.1K-0.5K"] += 1
        elif 500 <= int(review[0]) < 1000:
            quality["0.5K-1K"] += 1
        else:
            quality["1K+"] += 1
    return quality


qu = statistic_review()
formatfile.dict_to_json(qu, "../../show/data/review.json")
