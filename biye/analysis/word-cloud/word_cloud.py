# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import path
import jieba.analyse
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

content = open('title.txt', 'rb').read()
# tags is list type is iterable
jieba.analyse.set_stop_words('stop_word.txt')
tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
input_data = {}
for i in tags:
    weight = int(10000 * i[1]//1)
    input_data[i[0]] = weight

print(input_data)


d = path.dirname(__file__)
alice_coloring = imread("abc.jpg")
wc = WordCloud(
                font_path='abc.ttf',
                background_color="white",
                # 背景颜色max_words=2000
                mask=alice_coloring,  # 设置背景图片
                stopwords=STOPWORDS.add("said"),
                max_font_size=120,  # 字体最大值
                random_state=42,
                min_font_size=8)
wc.generate_from_frequencies(input_data)
image_colors = ImageColorGenerator(alice_coloring)

# 以下代码显示图片
plt.imshow(wc)
plt.axis("off")
# 绘制词云
plt.figure()
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
# 绘制背景图片为颜色的图片
plt.figure()
plt.imshow(alice_coloring, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
# 保存图片
wc.to_file(path.join(d, "daxue.png"))
