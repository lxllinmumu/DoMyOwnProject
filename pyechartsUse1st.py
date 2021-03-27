#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 23:07
# @Author  : Rem~
# @File    : pyechartsUse1st.py
# @function: pyecharts库的使用
# pyecharts库安装方法：https://www.jianshu.com/p/6004f298ae5e
# pandas库安装方法：https://www.jianshu.com/p/1fde1fb0b910
# 实例教程：https://mp.weixin.qq.com/s/oNFkNMvsXJG77CS9B0bbKg

import pandas as pd
from pyecharts.charts import map
import pyecharts.options as opts

frame = pd.read_csv('D:\\PycharmProjects\\DATA\\分省年度数据.csv', encoding='GBK')
Map = map()
Map.add("我国地区的GDP", frame[['地区', '2019年']].values.tolist(), "china")
Map.set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=500, max_=12000))
Map.render("2019年全国各地区GDP.html")




