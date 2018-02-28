# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import imp
import json

import requests
from bs4 import BeautifulSoup
import urllib.parse
import threading
from fake_useragent import UserAgent

from biye.tieba import operate
from biye.tieba import water
from biye.tieba import an_time

imp.reload(operate)

URL = 'http://tieba.baidu.com'
INDEX_URL = 'https://www.baidu.com'
URL_F = 'http://tieba.baidu.com/f'
MEMBER_URL = 'http://tieba.baidu.com/bawu2/platform/listMemberInfo'
HOME_PAGE = 'http://tieba.baidu.com/home/main?un='


def get_page(average, total):
    """
    Return a list contain pages.

    :param average: 每页中的帖子个数
    :param total: 请求的页数
    :return: 一个包含页数的列表
    """
    page = []
    for i in range(total):
        page.append(i * average)
    return page


def build_url(url, page):
    """
    Build the URL that you want to request.
    :param url: main url
    :param page: 第几页
    :return:
    """
    payload = {
        'word': '%B4%F3%D1%A7',
        'pn': page
    }
    params = urllib.parse.urlencode(payload)
    total_url = '?'.join([url, params.replace('25', '')])
    return total_url


def get_response(address, **kwargs):
    """
    Return the response of the request with url and params.
    :param address: url
    :param kwargs:
    :return:
    """
    response = requests.get(address, params=kwargs)

    return response


def get_response_with_headers(address, **kwargs):
    """
    Return the response of the request with url and params.
    :param address: url
    :param kwargs:
    :return:
    """
    ua = UserAgent()
    headers = {"UserAgent": ua.firefox}
    cookies = dict(TIEBA_USERTYPE='524dbb4833c464a2537aac4b',
                   TIEBAUID='cb23caae14130a0d384a57f1',
                   bdshare_firstime='1492671790350',
                   BAIDUID='14178C2FAE50F996CEA1844B8F14F945:FG=1',
                   bottleBubble='1',
                   after_vcode='7388F56A1FF97DF1A82DDC2A4AFE147CBC0956D5FD05F6CCE951BBAD0BDBC08E678E82C213D784F5ACD184E261F9D99560A0883C9B713F580EF20F3846B8081FA3053DCF60EE0E818CDF65F97E2BA390577DF5E786BBB8830F54157532E546D4715010F585BDEEB4CC79F5CAD39D8C1E36F38958F538B07A06C7F52294132BF436CCE3808C71E2C55652CC643319CE71')
    response = requests.get(address, params=kwargs, cookies=cookies)

    return response


def get_bs(response):
    """
    Return the bs object.

    :param response: response of the request with get.
    :return:
    """
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_post_info(soup):
    """
    Return the post information containing title, homepage, review number, author,
    author ID, author homepage, author detail.

    :param soup: bs object
    :return:
    """
    page_data = []
    lis = soup.find_all('li', class_=' j_thread_list clearfix')
    for li in lis:
        post = li.find('a', class_='j_th_tit ')
        # 帖子标题
        post_title = post.get_text()
        print('post_title：' + post.get_text())

        # 帖子主页
        post_home = URL + post['href']
        print('post: ' + URL + post['href'])

        # 帖子回复人数
        review_num = li.find('span', class_='threadlist_rep_num center_text').get_text()
        print('review_num：' + li.find('span', class_='threadlist_rep_num center_text').get_text())

        dic = json.loads(li['data-field'])
        # 作者昵称
        nickname = dic['author_name']
        print('nickname：' + str(dic['author_name']))
        # 作者ID
        if li.find('span', class_='tb_icon_author '):
            author = li.find('span', class_='tb_icon_author ')
            au_dic = json.loads(author['data-field'])
        if li.find('span', class_='tb_icon_author no_icon_author'):
            author = li.find('span', class_='tb_icon_author no_icon_author')
            au_dic = json.loads(author['data-field'])
        user_id = str(au_dic['user_id'])
        print('ID：' + str(au_dic['user_id']))

        # 作者主页
        if li.find('a', class_='frs-author-name j_user_card '):
            index_page = li.find('a', class_='frs-author-name j_user_card ')
            home = index_page['href']
        if li.find('a', class_='frs-author-name j_user_card vip_red '):
            index_page_vip = li.find('a', class_='frs-author-name j_user_card vip_red ')
            home = index_page_vip['href']
        homepage = URL + home
        print('homepage：' + URL + home)

        # 作者详细信息
        detail = INDEX_URL + '/p/' + str(dic['author_name']) + '/detail'
        print('detail：' + INDEX_URL + '/p/' + str(dic['author_name']) + '/detail')
        data = (post_title, post_home, review_num, nickname, user_id, homepage, detail)
        page_data.append(data)
    return page_data


def get_post_homepage(soup):
    """
    Get all post title and post homepage of index page.

    :param soup: bs object
    :return: 每个页面中的所有的帖子标题和主页。其中返回类型为list，list中包含的是每个帖子标题和主页，类型为tuple
            example: [(title, homepage), (title, homepage), (tiltle, home...), (.., ..)]
    """
    datas = []
    lis = soup.find_all('li', class_=' j_thread_list clearfix')
    for li in lis:
        post = li.find('a', class_='j_th_tit ')
        # 帖子标题
        post_title = post.get_text()
        # print('post_title: ' + post.get_text())

        # 帖子主页
        post_home = URL + post['href']
        # print('post_url: ' + URL + post['href'])
        # 帖子作者
        post_author = ''
        if li.find('a', class_='frs-author-name j_user_card '):
            post_author = li.find('a', class_='frs-author-name j_user_card ').get_text()
        if li.find('a', class_='frs-author-name j_user_card vip_red '):
            post_author = li.find('a', class_='frs-author-name j_user_card vip_red ').get_text()
        # 作者主页
        author_home = HOME_PAGE + post_author
        data = (post_title, post_home, post_author, author_home)
        datas.append(data)
    return datas


def author_detail_info(soup):
    """
    Return the author information containing sex, age, city, married, education.

    :param soup:
    :return: a list contain author information
    """
    key = []
    value = []
    users = []
    tag_dl = soup.find_all('dl')
    for dl in tag_dl:
        spans = dl.find_all('span')
        for number, values in enumerate(spans):
            if number % 2 == 0:
                key.append(values.get_text())
            if number % 2 != 0:
                value.append(values.get_text().replace(' ', ''))
    for a, b in zip(key, value):
        if a == '性别':
            users.append(b)
        if a == '生日':
            today = datetime.today()
            year = str(today)[:4]
            age = int(year) - int(b[:4])
            users.append(str(age))
        if a == '居住地':
            users.append(b)
        if a == '婚姻状态':
            users.append(b)
        if a == '教育程度':
            users.append(b)
    return users


def author_post_info(soup):
    spantext = []
    userdata = soup.find('div', class_='userinfo_userdata')
    # nickname
    nickname = ''
    if soup.find('span', class_='userinfo_username '):
        nickname = soup.find('span', class_='userinfo_username ').get_text()
    if soup.find('span', class_='userinfo_username vip_red '):
        nickname = soup.find('span', class_='userinfo_username vip_red ').get_text()

    # sex
    sex = 'unknown'
    if soup.find('span', class_='userinfo_sex userinfo_sex_male'):
        sex = 'male'
    if soup.find('span', class_='userinfo_sex userinfo_sex_female'):
        sex = 'female'

    # vip
    vip = 'NO'
    if soup.find('span', class_='userinfo_username vip_red '):
        vip = 'YES'
    spans = userdata.find_all('span')
    for span in spans:
        spantext.append(span.get_text())
    members = vip

    # 吧龄
    postage = spantext[1][3:-1]
    print(postage)
    if postage == '':
        postage = '0'
    # print("吧龄：" + spantext[1][3:-1])

    # 发帖总数
    postnumber = spantext[3][3:]
    # print("发帖：" + spantext[3][3:])

    postinfo = [nickname, sex, postage, postnumber, members]
    return postinfo


def str_to_date(date):
    return datetime.strptime(date, "%Y-%m-%d")


def post_info(soup):
    # review acount
    li = soup.find('li', class_='l_reply_num')
    review_content = li.get_text().strip('\n').replace(' ', '')
    index = review_content.index('回')
    review_amount = review_content[:index]

    # post title
    title = soup.find('h1').get_text()

    # data信息中包含的内容有：作者在本题吧的等级，昵称，性别，头像，用户id，等级名称，cur_score(?)，\
    # 帖子的id，发帖使用的设备，发帖使用的终端软件，tbclient(贴吧客户端)， wap(网页端)以及发帖日期等
    data_info = soup.find('div', class_='l_post j_l_post l_post_bright noborder ')
    info = data_info['data-field']
    data = json.loads(info)

    # author and author_id
    author = data['author']['user_name']
    au_id = data['author']['user_id']

    # date and time
    date = data['content']['date']
    index = date.index(' ')
    str_date = date[:index]
    str_time = date[index + 1:]

    # client type
    ter_type = data['content']['open_type']
    post = [title, review_amount, author, au_id, str_date, str_time, ter_type]
    return post


def member_info(soup):
    span_first = soup.find_all('span', class_='member first_row')
    member_information = []
    for span in span_first:
        one_member = []
        homepage = span.find('a', class_='user_name')
        one_member.append(URL + homepage['href'])
        one_member.append(homepage['title'])
        if span.find('span', class_='forum-level-bawu bawu-info-lv1'):
            level = '1'
            one_member.append(level)
        if span.find('span', class_='forum-level-bawu bawu-info-lv2'):
            level = '2'
            one_member.append(level)
        if span.find('span', class_='forum-level-bawu bawu-info-lv3'):
            level = '3'
            one_member.append(level)
        if span.find('span', class_='forum-level-bawu bawu-info-lv4'):
            level = '4'
            one_member.append(level)
        if span.find('span', class_='forum-level-bawu bawu-info-lv5'):
            level = '5'
            one_member.append(level)
        if span.find('span', class_='forum-level-bawu bawu-info-lv6'):
            level = '6'
            one_member.append(level)
        if span.find('span', class_='forum-level-bawu bawu-info-lv7'):
            level = '7'
            one_member.append(level)
        if span.find('span', class_='forum-level-bawu bawu-info-lv8'):
            level = '8'
            one_member.append(level)
        if span.find('span', class_='forum-level-bawu bawu-info-lv9'):
            level = '9'
            one_member.append(level)
        if span.find('span', class_='forum-level-bawu bawu-info-lv10'):
            level = '10'
            one_member.append(level)
        if span.find('span', class_='forum-level-bawu bawu-info-lv11'):
            level = '11'
            one_member.append(level)
        if span.find('span', class_='forum-level-bawu bawu-info-lv12'):
            level = '12'
            one_member.append(level)
        if span.find('span', class_='forum-level-bawu bawu-info-lv13'):
            level = '13'
            one_member.append(level)
        if span.find('span', class_='forum-level-bawu bawu-info-lv14'):
            level = '14'
            one_member.append(level)
        if span.find('span', class_='forum-level-bawu bawu-info-lv15'):
            level = '15'
            one_member.append(level)
        member_information.append(one_member)

    span_two = soup.find_all('span', class_='member ')
    for span_t in span_two:
        two_member = []
        homepage = span_t.find('a', class_='user_name')
        two_member.append(URL + homepage['href'])
        two_member.append(homepage['title'])
        if span_t.find('span', class_='forum-level-bawu bawu-info-lv1'):
            level = '1'
            two_member.append(level)
        if span_t.find('span', class_='forum-level-bawu bawu-info-lv2'):
            level = '2'
            two_member.append(level)
        if span_t.find('span', class_='forum-level-bawu bawu-info-lv3'):
            level = '3'
            two_member.append(level)
        if span_t.find('span', class_='forum-level-bawu bawu-info-lv4'):
            level = '4'
            two_member.append(level)
        if span_t.find('span', class_='forum-level-bawu bawu-info-lv5'):
            level = '5'
            two_member.append(level)
        if span_t.find('span', class_='forum-level-bawu bawu-info-lv6'):
            level = '6'
            two_member.append(level)
        if span_t.find('span', class_='forum-level-bawu bawu-info-lv7'):
            level = '7'
            two_member.append(level)
        if span_t.find('span', class_='forum-level-bawu bawu-info-lv8'):
            level = '8'
            two_member.append(level)
        if span_t.find('span', class_='forum-level-bawu bawu-info-lv9'):
            level = '9'
            two_member.append(level)
        if span_t.find('span', class_='forum-level-bawu bawu-info-lv10'):
            level = '10'
            two_member.append(level)
        if span_t.find('span', class_='forum-level-bawu bawu-info-lv11'):
            level = '11'
            two_member.append(level)
        if span_t.find('span', class_='forum-level-bawu bawu-info-lv12'):
            level = '12'
            two_member.append(level)
        if span_t.find('span', class_='forum-level-bawu bawu-info-lv13'):
            level = '13'
            two_member.append(level)
        if span_t.find('span', class_='forum-level-bawu bawu-info-lv14'):
            level = '14'
            two_member.append(level)
        if span_t.find('span', class_='forum-level-bawu bawu-info-lv15'):
            level = '15'
            two_member.append(level)
        member_information.append(two_member)
    return member_information


# # 以下代码提取本贴吧中所有的会员信息 昵称，主页，本吧中的等级
def get_all_members(start, end):
    for page in range(start, end):
        url = build_url(MEMBER_URL, page=page)
        print(url)
        response = get_response(url)
        soup = get_bs(response)
        member_list = member_info(soup)
        print(member_list)
        for member in member_list:
            operate.insert_sql_member('sortmember', member)


def dict_to_json(dictionary, name='aaa.json'):
    """
    把转换为json文件

    :param dictionary: 想要转化的字典
    :param name: 存储json文件的名称
    :return: None
    """

    sorted_dict = sorted(dictionary.items(), key=lambda e: e[0])
    key = []
    value = []
    for tup in sorted_dict:
        key.append(tup[0])
        value.append(tup[1])
    result_json = json.dumps({'month': key, 'number': value})
    print({'month': key, 'number': value})
    with open(name, 'w') as file:
        file.write(result_json)
