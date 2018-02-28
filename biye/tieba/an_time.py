# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def count_post_month(result):
    """
    Get the number of posts of every month in 2015, 2016, 2017
    :param result: 数据库查询结果，查取str_date and str_time
    :return: three dictionary of month of 2015, 2016, 2017
    """
    year_2017_month_count = {}
    year_2016_month_count = {}
    year_2015_month_count = {}

    month_count_2015_01 = 0
    month_count_2015_02 = 0
    month_count_2015_03 = 0
    month_count_2015_04 = 0
    month_count_2015_05 = 0
    month_count_2015_06 = 0
    month_count_2015_07 = 0
    month_count_2015_08 = 0
    month_count_2015_09 = 0
    month_count_2015_10 = 0
    month_count_2015_11 = 0
    month_count_2015_12 = 0
    month_count_2016_01 = 0
    month_count_2016_02 = 0
    month_count_2016_03 = 0
    month_count_2016_04 = 0
    month_count_2016_05 = 0
    month_count_2016_06 = 0
    month_count_2016_07 = 0
    month_count_2016_08 = 0
    month_count_2016_09 = 0
    month_count_2016_10 = 0
    month_count_2016_11 = 0
    month_count_2016_12 = 0
    month_count_2017_01 = 0
    month_count_2017_02 = 0
    month_count_2017_03 = 0
    month_count_2017_04 = 0
    month_count_2017_05 = 0
    month_count_2017_06 = 0
    month_count_2017_07 = 0
    month_count_2017_08 = 0
    month_count_2017_09 = 0
    month_count_2017_10 = 0
    month_count_2017_11 = 0
    month_count_2017_12 = 0

    # # # 分析三年中所有月份中的发帖数
    for datetime in result:
        date = datetime[0]
        year = date[0:4]
        month = date[5:7]

        if year == '2017':
            if month == '01':
                month_count_2017_01 += 1
                year_2017_month_count['2017_01'] = month_count_2017_01
            if month == '02':
                month_count_2017_02 += 1
                year_2017_month_count['2017_02'] = month_count_2017_02
            if month == '03':
                month_count_2017_03 += 1
                year_2017_month_count['2017_03'] = month_count_2017_03
            if month == '04':
                month_count_2017_04 += 1
                year_2017_month_count['2017_04'] = month_count_2017_04
            if month == '05':
                month_count_2017_05 += 1
                year_2017_month_count['2017_05'] = month_count_2017_05
            if month == '06':
                month_count_2017_06 += 1
                year_2017_month_count['2017_06'] = month_count_2017_06
            if month == '07':
                month_count_2017_07 += 1
                year_2017_month_count['2017_07'] = month_count_2017_07
            if month == '08':
                month_count_2017_08 += 1
                year_2017_month_count['2017_08'] = month_count_2017_08
            if month == '09':
                month_count_2017_09 += 1
                year_2017_month_count['2017_09'] = month_count_2017_09
            if month == '10':
                month_count_2017_10 += 1
                year_2017_month_count['2017_10'] = month_count_2017_10
            if month == '11':
                month_count_2017_11 += 1
                year_2017_month_count['2017_11'] = month_count_2017_11
            if month == '12':
                month_count_2017_12 += 1
                year_2017_month_count['2017_12'] = month_count_2017_12
        elif year == '2016':
            if month == '01':
                month_count_2016_01 += 1
                year_2016_month_count['2016_01'] = month_count_2016_01
            if month == '02':
                month_count_2016_02 += 1
                year_2016_month_count['2016_02'] = month_count_2016_02
            if month == '03':
                month_count_2016_03 += 1
                year_2016_month_count['2016_03'] = month_count_2016_03
            if month == '04':
                month_count_2016_04 += 1
                year_2016_month_count['2016_04'] = month_count_2016_04
            if month == '05':
                month_count_2016_05 += 1
                year_2016_month_count['2016_05'] = month_count_2016_05
            if month == '06':
                month_count_2016_06 += 1
                year_2016_month_count['2016_06'] = month_count_2016_06
            if month == '07':
                month_count_2016_07 += 1
                year_2016_month_count['2016_07'] = month_count_2016_07
            if month == '08':
                month_count_2016_08 += 1
                year_2016_month_count['2016_08'] = month_count_2016_08
            if month == '09':
                month_count_2016_09 += 1
                year_2016_month_count['2016_09'] = month_count_2016_09
            if month == '10':
                month_count_2016_10 += 1
                year_2016_month_count['2016_10'] = month_count_2016_10
            if month == '11':
                month_count_2016_11 += 1
                year_2016_month_count['2016_11'] = month_count_2016_11
            if month == '12':
                month_count_2016_12 += 1
                year_2016_month_count['2016_12'] = month_count_2016_12
        elif year == '2015':
            if month == '01':
                month_count_2015_01 += 1
                year_2015_month_count['2015_01'] = month_count_2015_01
            if month == '02':
                month_count_2015_02 += 1
                year_2015_month_count['2015_02'] = month_count_2015_02
            if month == '03':
                month_count_2015_03 += 1
                year_2015_month_count['2015_03'] = month_count_2015_03
            if month == '04':
                month_count_2015_04 += 1
                year_2015_month_count['2015_04'] = month_count_2015_04
            if month == '05':
                month_count_2015_05 += 1
                year_2015_month_count['2015_05'] = month_count_2015_05
            if month == '06':
                month_count_2015_06 += 1
                year_2015_month_count['2015_06'] = month_count_2015_06
            if month == '07':
                month_count_2015_07 += 1
                year_2015_month_count['2015_07'] = month_count_2015_07
            if month == '08':
                month_count_2015_08 += 1
                year_2015_month_count['2015_08'] = month_count_2015_08
            if month == '09':
                month_count_2015_09 += 1
                year_2015_month_count['2015_09'] = month_count_2015_09
            if month == '10':
                month_count_2015_10 += 1
                year_2015_month_count['2015_10'] = month_count_2015_10
            if month == '11':
                month_count_2015_11 += 1
                year_2015_month_count['2015_11'] = month_count_2015_11
            if month == '12':
                month_count_2015_12 += 1
                year_2015_month_count['2015_12'] = month_count_2015_12
    return year_2017_month_count, year_2016_month_count, year_2015_month_count


def count_post_hour(result):
    """

    :param result: 数据库查询结果，查取str_date and str_time
    :return: a dictionary of every hour.
    """
    count_hour = {}

    count_hour_0 = 0
    count_hour_1 = 0
    count_hour_2 = 0
    count_hour_3 = 0
    count_hour_4 = 0
    count_hour_5 = 0
    count_hour_6 = 0
    count_hour_7 = 0
    count_hour_8 = 0
    count_hour_9 = 0
    count_hour_10 = 0
    count_hour_11 = 0
    count_hour_12 = 0
    count_hour_13 = 0
    count_hour_14 = 0
    count_hour_15 = 0
    count_hour_16 = 0
    count_hour_17 = 0
    count_hour_18 = 0
    count_hour_19 = 0
    count_hour_20 = 0
    count_hour_21 = 0
    count_hour_22 = 0
    count_hour_23 = 0

    # # # count the number of every hours.
    for datetime in result:
        time = datetime[1]
        hour = time[0:2]

        if hour == '00':
            count_hour_0 += 1
            count_hour['00'] = count_hour_0
        if hour == '01':
            count_hour_1 += 1
            count_hour['01'] = count_hour_1
        if hour == '02':
            count_hour_2 += 1
            count_hour['02'] = count_hour_2
        if hour == '03':
            count_hour_3 += 1
            count_hour['03'] = count_hour_3
        if hour == '04':
            count_hour_4 += 1
            count_hour['04'] = count_hour_4
        if hour == '05':
            count_hour_5 += 1
            count_hour['05'] = count_hour_5
        if hour == '06':
            count_hour_6 += 1
            count_hour['06'] = count_hour_6
        if hour == '07':
            count_hour_7 += 1
            count_hour['07'] = count_hour_7
        if hour == '08':
            count_hour_8 += 1
            count_hour['08'] = count_hour_8
        if hour == '09':
            count_hour_9 += 1
            count_hour['09'] = count_hour_9
        if hour == '10':
            count_hour_10 += 1
            count_hour['10'] = count_hour_10
        if hour == '11':
            count_hour_11 += 1
            count_hour['11'] = count_hour_11
        if hour == '12':
            count_hour_12 += 1
            count_hour['12'] = count_hour_12
        if hour == '13':
            count_hour_13 += 1
            count_hour['13'] = count_hour_13
        if hour == '14':
            count_hour_14 += 1
            count_hour['14'] = count_hour_14
        if hour == '15':
            count_hour_15 += 1
            count_hour['15'] = count_hour_15
        if hour == '16':
            count_hour_16 += 1
            count_hour['16'] = count_hour_16
        if hour == '17':
            count_hour_17 += 1
            count_hour['17'] = count_hour_17
        if hour == '18':
            count_hour_18 += 1
            count_hour['18'] = count_hour_18
        if hour == '19':
            count_hour_19 += 1
            count_hour['19'] = count_hour_19
        if hour == '20':
            count_hour_20 += 1
            count_hour['20'] = count_hour_20
        if hour == '21':
            count_hour_21 += 1
            count_hour['21'] = count_hour_21
        if hour == '22':
            count_hour_22 += 1
            count_hour['22'] = count_hour_22
        if hour == '23':
            count_hour_23 += 1
            count_hour['23'] = count_hour_23
    return count_hour
