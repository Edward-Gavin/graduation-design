# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


def dict_to_json(dictionary: object, name: object = 'aaa.json') -> object:
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
    result_json = json.dumps({'keys': key, 'value': value})
    print({'keys': key, 'value': value})
    with open(name, 'w') as file:
        file.write(result_json)

