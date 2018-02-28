# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from biye.spider.operate import database
from datetime import *


def barage_wrong():
    abc = database.select_all("pure_users", 'id', 'barage')
    datetime.now()
    d = date(2003, 11, 25)
    t = time(0, 0, 0)
    publishing = datetime.combine(d, t)
    maxage = datetime.now() - publishing
    maxyear = int(str(maxage)[0:4])/365
    print(maxyear)
    wrongage = []
    for age in abc:
        try:
            if float(age[1]) > maxyear:
                wrongage.append(age[0])
        except ValueError as why:
            wrongage.append(age[0])
    return wrongage


if __name__ == '__main__':
    wrong = barage_wrong()
    print(wrong)