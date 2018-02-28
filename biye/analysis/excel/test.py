# !/usr/bin/env python3
# -*- coding: utf-8 -*-


from pyexcel_xls import save_data
from pyexcel_xls import get_data
from collections import OrderedDict
import pymysql


if __name__ == '__main__':
    conn = pymysql.connect(host='localhost',
                           user='root',
                           db='tieba',
                           charset='utf8mb4')

    # sql = 'select id, post_title, post_home, review_num, nickname, au_id, str_date, str_time, client_type'
    sql = 'select id, title, homepage, post_author, author_home from source1'
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    xls_header = get_data('./abc.xlsx')
    xh = xls_header.pop("sheet1")
    xd = OrderedDict()
    xd.update({"sheet 1": xh+result})
    save_data('./abc.xlsx', xd)
