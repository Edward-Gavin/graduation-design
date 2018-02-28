# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from biye.tieba import index
from biye.tieba import operate


def statistic_sex():
    """
    Return the number of boys, girls and unknow.

    :return:
    """
    sexes = operate.select_sql('pure_users', 178368, 1, 178368, 'sex')
    boys = 0
    girls = 0
    for sex in sexes:
        for one in sex:
            if str(one) == 'female':
                girls += 1
            else:
                boys += 1

    return boys, girls


result = operate.select_all('source1', 'title')
for res in result:
    with open('title.txt', 'a', encoding='utf-8', errors='ignore') as file:
        file.write(res[0], )
        file.write('\n')
if __name__ == 'main':
    # abc = post_info(10)
    # select_sql('usual', 'au_id', 'nickname', 'post_title')
    # for data in abc:
    #     insert_sql('tieba', abc)

    # result = operate.select_sql('tieba', 'au_id', 'nickname', 'detail')
    # for tuple_r in result:
    #     url = tuple_r[2]
    #     res = get_response(url)
    #     # 规定response的编码格式，这里默认的是ISO-8859-1
    #     res.encoding = 'utf-8'
    #     print(res.request.url)
    #     bsobj = get_bs(res)
    #     user = author_detail_info(bsobj)
    #     user.insert(0, tuple_r[1])
    #     user.insert(0, tuple_r[0])
    #     while len(user) != 7:
    #         user.append(' ')
    #     print(user)
    #     operate.insert_user_sql('user', user)

    # homepages = operate.select_sql('postn', 200000, 186752, 208886, 'nickname')
    # au_ids = operate.select_sql('postn', 200000, 186752, 208886, 'au_id')
    # for au_id, homepage in zip(au_ids, homepages):
    #     try:
    #         print(au_id, homepage)
    #         span_text = []
    #         print('http://tieba.baidu.com/home/main?un='+homepage[0])
    #         res = get_response('http://tieba.baidu.com/home/main?un='+homepage[0])
    #         soup = get_bs(res)
    #
    #         abc = author_post_info(soup)
    #         abc.insert(0, au_id[0])
    #         operate.insert_sql_users('users', abc)
    #     except AttributeError as why:
    #         continue
    #     except TypeError as why:
    #         continue

    # # 以下代码将所有的大学吧中的帖子的标题和主页插入到数据库
    # pages = get_page(50, 5000)
    # for page in pages:
    #     print(page)
    # for i in range(1, 3000):
    #     print(i * 50 + 233750)
    #     response = get_response_with_headers(URL_F, kw='大学', ie='utf-8', pn=i * 50 + 233750)
    #     print(response.request.url)
    #     res_soup = get_bs(response=response)
    #     # print(res_soup)
    #     titleList = get_post_homepage(res_soup)
    #     # print(titleList)
    #     for title in titleList:
    #         operate.insert_sql_source1('source1', title)

    # 获取所有的标题，存入文件
    print('ab')
    result = operate.select_all('source1', 'title')
    print(result)
    for res in result:
        with open('title.txt', 'a', encoding='utf-8', errors='ignore') as file:
            file.write(res[0], )
            file.write('\n')

    # 以下代码分析帖子主页，提取需要的数据
    # selectResult = operate.select_sql('source1', 99900, 208408, 212155, 'homepage')
    # for home in selectResult:
    #     homeUrl = ''.join(home)
    #     print(homeUrl)
    #     response = get_response(homeUrl)
    #
    #     try:
    #         post = post_info(get_bs(response))
    #         post.insert(0, homeUrl)
    #         print(post)
    #         operate.insert_sql_post('postn', post)
    #     except AttributeError as why:
    #         continue
    #     except KeyError as why:
    #         continue

    # # # 查找post表中，使用的client类型
    # select_result = operate.select_sql('post1', 9800, 'client_type')
    # print(len(select_result))
    # android = 0
    # apple = 0
    # unknown = 0
    # for result in select_result:
    #     if result[0] == 'android':
    #         android += 1
    #     elif result[0] == 'apple':
    #         apple += 1
    #     else:
    #         unknown += 1
    # print(android)
    # print(apple)
    # print(unknown)

    # 多线程抓取会员用户信息
    # for x in range(20):
    #     start = 1 + x * 23
    #     end = 23 + 23 * x + 1
    #     th = threading.Thread(target=get_all_members, args=(start, end))
    #     th.start()

    # get_all_members(1, 458)

    # # # 获取水军信息
    # ab = operate.select_sql('sortmember', 9500, 'nickname')
    # ran = 0
    # st = 0
    # for tu in ab:
    #     ran += water.analyze_member_random(tu[0])
    #     st += water.analyze_member_str(tu[0])
    # if ran > 200 and st > 200:
    #     print(ran + st)

    # # # 获取每个小时中的发帖数
    # abc = operate.select_sql('post2', 17800, 'str_date', 'str_time')
    # hour = an_time.count_post_hour(abc)
    # dict_to_json(hour, name='hour.json')

    # # 获取每月的发帖数
    # month_2017, month_2016, month_2015 = an_time.count_post_month(abc)
    # dict_to_json(month_2017, name='month_2017.json')
    # dict_to_json(month_2016, name='month_2016.json')
    # dict_to_json(month_2015, name='month_2015.json')

    # # # # 会员详细信息表的的创建，以及数据插入
    # homes = operate.select_sql('members', 11021, 'homepage')
    # for home in homes:
    #     print(home[0])
    #     try:
    #         response = get_response(home[0])
    #         response.encoding = 'utf-8'
    #         soup = get_bs(response=response)
    #         abc = author_post_info(soup)
    #         operate.insert_sql_member_detail('member_detail', abc)
    #     except TypeError as why:
    #         continue
    #     except AttributeError as why:
    #         continue

    # a, b = statistic_sex()
    # print(a, b)
