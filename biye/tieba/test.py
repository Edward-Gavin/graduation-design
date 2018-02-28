# import requests
# from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
#
# url = 'http://tieba.baidu.com/f'
# payload = {
#     'kw': '大学',
#     'ie': 'utf-8',
#     'pn': 100000
# }
# headers = {
#     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"
# }
# ua = UserAgent()
# head = ua.chrome
# print(head)
#
# response = requests.get(url, params=payload, headers=headers)
# print(response)
# print(response.text)

import requests
from fake_useragent import UserAgent

from biye.spider.forspider import get_procy

if __name__ == '__main__':
    ua = UserAgent()
    headers = {"User-Agent": ua.firefox}
    PROXY = get_procy.get_proxy_xisi()
    print(PROXY)
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
    print(res.url)
    print(dir(res.request.prepare_url))
    print(dir(res.request))
    print(res.request.prepare_headers)
