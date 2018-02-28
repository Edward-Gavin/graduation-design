# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql


def conn_sql():
    """
    Connect to db of local. Return a connection of the list.
    :return: connection
    """
    conn = pymysql.connect(host='localhost',
                           user='root',
                           db='tieba',
                           charset='utf8mb4')
    return conn


def insert_sql(table, data):
    """
    Insert data to database.

    :param table: 操作的表
    :param data: 插入的数据(此处的类型为list类型，其中的元素为tuple)
    :return:
    """
    conn = conn_sql()
    try:
        with conn.cursor() as curs:
            sql = 'insert into ' + table + ' (`post_title`,`post_home`,`review_num`,`nickname`,' \
                                           '`au_id`,`homepage`,`detail`) values (%s, %s, %s, %s, %s, %s, %s)'
            curs.execute(sql, data)
            conn.commit()
    finally:
        conn.close()


def insert_user_sql(table, data):
    """
    Insert data to database.

    :param table: 操作的表
    :param data: 插入的数据(此处的类型为tuple)
    :return:
    """
    conn = conn_sql()
    try:
        with conn.cursor() as curs:
            sql = 'insert into ' + table + ' (`au_id`,`nickname`,`sex`,`age`,' \
                                           '`city`,`married`,`education`) values (%s, %s, %s, %s, %s, %s, %s)'
            curs.execute(sql, data)
            conn.commit()
    finally:
        conn.close()


def insert_sql_source(table, data):
    """

    :param table:
    :param data:
    :return:
    """
    conn = conn_sql()
    try:
        with conn.cursor() as curs:
            sql = 'insert into ' + table + ' (`title`,`homepage`) values (%s, %s)'
            curs.execute(sql, data)
            conn.commit()
    finally:
        conn.close()


def insert_sql_source1(table, data):
    """

    :param table:
    :param data:
    :return:
    """
    conn = conn_sql()
    try:
        with conn.cursor() as curs:
            sql = 'insert into ' + table + ' (`title`,`homepage`, `post_author`, `author_home`) values (%s, %s, %s, %s)'
            curs.execute(sql, data)
            conn.commit()
    finally:
        conn.close()


def insert_sql_member(table, data):
    """

    :param table:
    :param data:
    :return:
    """
    conn = conn_sql()
    try:
        with conn.cursor() as curs:
            sql = 'insert into ' + table + ' (`homepage`,`nickname`, `level`) values (%s, %s, %s)'
            curs.execute(sql, data)
            conn.commit()
    finally:
        conn.close()


def insert_sql_member_detail(table, data):
    """

    :param table:
    :param data:
    :return:
    """
    conn = conn_sql()
    try:
        with conn.cursor() as curs:
            sql = 'insert into ' + table + '(`nickname`, `sex`, `postage`, `postnumber`, `member`) values (%s, %s, %s, %s, %s)'
            curs.execute(sql, data)
            conn.commit()
    finally:
        conn.close()


def insert_sql_post(table, data):
    """
    :param table:
    :param data:
    :return:
    """
    conn = conn_sql()
    try:
        with conn.cursor() as curs:
            sql = 'insert into ' + table + \
                  ' (`post_title`,`post_home`, `review_num`, `nickname`, `au_id`, `str_date`,' \
                  ' `str_time`, `client_type`) values (%s, %s, %s,%s, %s, %s, %s, %s)'
            curs.execute(sql, data)
            conn.commit()
    finally:
        conn.close()


def insert_sql_users(table, data):
    """
    :param table:
    :param data:
    :return:
    """
    conn = conn_sql()
    try:
        with conn.cursor() as curs:
            sql = 'insert into ' + table + \
                  ' (`au_id`, `nickname`, `sex`, `barage`, `post_number`, `member`) values (%s, %s, %s,%s, %s, %s)'
            curs.execute(sql, data)
            conn.commit()
    finally:
        conn.close()


def select_sql(table, amount=1, start=10, end=20, *args):
    """
    Return selected value.

    :param end:
    :param start:
    :param amount: 提取的数据量，默认为1条
    :param table: 操作的表
    :param args: 可变参数中包含的是想要查询的字段
    :return:
    """
    # 这里是对参数进行格式化处理
    temp = (str(args)[1:-1]).replace("'", '')
    if len(args) == 1:
        temp = (str(args)[1:-2]).replace("'", '')
    conn = conn_sql()
    try:
        cursor = conn.cursor()
        count = cursor.execute('select %s from %s limit %d, %d' % (temp, table, start, end))
        # print('total:{}'.format(count)
        return cursor.fetchmany(amount)
    finally:
        conn.close()


def select_sex_user(table, amount=1, start=10, end=20):
    conn = conn_sql()
    try:
        cursor = conn.cursor()
        count = cursor.execute('select sex from %s limit %d, %d' % (table, start, end))
        # print('total:{}'.format(count))
        return cursor.fetchmany(amount)
    finally:
        conn.close()


def select_all(table, *args):
    temp = (str(args)[1:-1]).replace("'", '')
    if len(args) == 1:
        temp = (str(args)[1:-2]).replace("'", '')
    conn = conn_sql()
    try:
        cursor = conn.cursor()
        cursor.execute('select '+temp+' from '+table)
        returnall = cursor.fetchall()
    finally:
        conn.close()
    return returnall
