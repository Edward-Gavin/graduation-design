# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib.parse


def member_info(soup):
    span_first = soup.find_all('span', class_='member first_row')
    member_information = []
    for span in span_first:
        one_member = []
        homepage = span.find('a', class_='user_name')
        one_member.append(INDEX_URL+homepage['href'])
        print(INDEX_URL+homepage['href'])
        one_member.append(homepage['title'])
        print(homepage['title'])
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
            print(INDEX_URL + homepage['href'])
            two_member.append(INDEX_URL+homepage['href'])
            print(homepage['title'])
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
        print(member_information)

URL = 'http://tieba.baidu.com/bawu2/platform/listMemberInfo'
INDEX_URL = 'http://tieba.baidu.com'

payload = {
    'word': '%B4%F3%D1%A7',
    'pn': '2'
}
params = urllib.parse.urlencode(payload)
a = '?'.join([URL, params.replace('25', '')])
print(a)

response = requests.get(a)
print(response.status_code)
soup = BeautifulSoup(response.text, 'lxml')
member_info(soup)


