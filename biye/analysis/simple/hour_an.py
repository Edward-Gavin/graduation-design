# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from biye.analysis.simple import an_time
from biye.spider.operate import dict_to_json as tr
from biye.spider.operate import database


# # 获取每个小时中的发帖数
abc = database.select_all('postn', 'str_date', 'str_time')
hour = an_time.count_post_hour(abc)
tr.dict_to_json(hour, name='../../show/data/hour.json')

# 获取每月的发帖数
month_2017, month_2016, month_2015 = an_time.count_post_month(abc)
tr.dict_to_json(month_2017, name='../../show/data/month_2017.json')
tr.dict_to_json(month_2016, name='../../data/show/month_2016.json')
tr.dict_to_json(month_2015, name='../../show/data/month_2015.json')
