# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from biye.spider.operate import database
import pymysql

au_ids = database.select_all('users', 'au_id')
ids = database.select_all('users', 'id')

allin = database.select_all('pure_users', 'au_id')
for au_id, data_id in zip(au_ids, ids):
    print(data_id[0])
    conn = pymysql.connect(host='localhost',
                          user='root',
                          db='tieba',
                          charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute('select au_id, nickname, sex, barage, post_number, member from users where id=%d' % data_id[0])
    data = cursor.fetchone()
    conn.close()
    if au_id in allin:
        print('exist')
    else:
        print('not exist!')
        database.insert_sql_users('pure_users', data)
