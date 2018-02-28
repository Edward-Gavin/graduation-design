# !/usr/bin/env python3
# -*- coding: utf-8 -*-


from biye.spider.operate import database
from biye.spider.operate import formatfile


def statistic_barage():
    barages = database.select_all('pure_users', 'barage')
    age = {
        "onedown": 0,
        "one": 0,
        "two": 0,
        "three": 0,
        "four": 0,
        "five": 0,
        "six": 0,
        "seven": 0,
        "eight": 0,
        "nine": 0,
        "ten": 0,
        "eleven": 0,
        "twelve": 0,
        "twelveup": 0
    }
    for barage in barages:
        try:
            if 0 <= float(barage[0]) < 1:
                age['onedown'] += 1
            elif 1 <= float(barage[0]) < 2:
                age['one'] += 1
            elif 2 <= float(barage[0]) < 3:
                age['two'] += 1
            elif 3 <= float(barage[0]) < 4:
                age['three'] += 1
            elif 4 <= float(barage[0]) < 5:
                age['four'] += 1
            elif 5 <= float(barage[0]) < 6:
                age['five'] += 1
            elif 6 <= float(barage[0]) < 7:
                age['six'] += 1
            elif 7 <= float(barage[0]) < 8:
                age['seven'] += 1
            elif 8 <= float(barage[0]) < 9:
                age['eight'] += 1
            elif 9 <= float(barage[0]) < 10:
                age['nine'] += 1
            elif 10 <= float(barage[0]) < 11:
                age['ten'] += 1
            elif 11 <= float(barage[0]) < 12:
                age['eleven'] += 1
            elif 12 <= float(barage[0]) <13:
                age['twelve'] += 1
            else:
                age['twelveup'] += 1
        except ValueError as why:
            pass

    return age


ages = statistic_barage()
formatfile.dict_to_json(ages, '../../show/data/barage.json')
