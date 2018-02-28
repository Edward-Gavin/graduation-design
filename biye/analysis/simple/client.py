# !/usr/bin/env python3
# -*- coding: utf-8 -*-


from biye.spider.operate import database
from biye.spider.operate import formatfile


def statistic_client():
    select_result = database.select_all('postn', 'client_type')
    android = 0
    apple = 0
    unknown = 0
    for result in select_result:
        if result[0] == 'android':
            android += 1
        elif result[0] == 'apple':
            apple += 1
        else:
            unknown += 1
    return android, apple, unknown


androids, apples, unknows = statistic_client()
statistic = {'andiord': androids, 'apple': apples, 'unknown': unknows}
formatfile.dict_to_json(statistic, '../../show/data/client.json')