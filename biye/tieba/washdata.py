# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from biye.tieba import operate
import pymysql

au_ids = operate.select_sql('users', 2180806, 65771, 2180806, 'au_id')
ids = operate.select_sql('users', 2180806, 65771, 2180806, 'id')

allin = operate.select_all('pure_users', 'au_id')
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
    print(data)
    if au_id in allin:
        print('exist')
    else:
        print('not exist!')
        operate.insert_sql_users('pure_users', data)
