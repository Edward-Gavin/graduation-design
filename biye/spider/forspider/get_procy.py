# !/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent


PROXY =[]
ua = UserAgent()
header = ua.firefox
headers = {'User-Agent':header}


def get_proxy_xisi():
    """
    Get proxy pool from the URL.(http://www.xicidaili.com/)

    :return:
    """

    url = 'http://www.xicidaili.com/'
    response = requests.get(url, headers=headers)
    bsobj = bs(response.text, 'lxml')
    abc = bsobj.find_all('tr', {'class': 'odd'})
    for table in abc:
        agent = []
        content = table.find_all('td')
        for i in content:
            con = i.get_text().strip('\n').replace(' ', '')
            agent.append(con)
        PROXY.append(agent)
    return PROXY


def get_proxy_kuaidaili():
    """
    Get
    :return:
    """
    url = 'http://www.kuaidaili.com/proxylist/1/'
    reponse = requests.get(url, headers=headers, timeout=10)
    print(reponse)
    bsobj = bs(reponse.text, 'lxml')
    abc = bsobj.find_all('tr', {'class': 'odd'})
    print(abc)


if __name__ == '__main__':
    get_proxy_xisi()
    print(PROXY[1][1])
    print(PROXY[2][1])

    proxies = {
        'http': 'http://'+PROXY[3][1]
    }

    ip = 'http://www.douban.com'
    res = requests.get(ip, proxies=proxies, headers=headers)
    print(res.headers)
    print(res.text)
    print(res.request.headers)
    print(dir(res.request.prepare_url))
    print(dir(res.request))
    print(res.request.prepare_headers)
