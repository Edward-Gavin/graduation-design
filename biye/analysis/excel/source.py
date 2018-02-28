# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       db='tieba',
                       charset='utf8mb4')

sql = 'select * from source1'
cursor = conn.cursor()
cursor.execute(sql)
result = cursor.fetchmany(10)
cursor.close()
conn.close()
for i in result:
    with open('hah.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel')
        spamwriter.writerow(list(i))