#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2020/6/23 21:21
# FileName: run.py
# Description: 基于Python Flask Web实现的疫情数据可视化平台
# Question:


# 使用绝对路径导入
import sys,os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')
# 报错可忽略
from Covid19_data_get import getForeignData, getChinaData, getProvinceData
from pyecharts.charts import Bar, Line, Map, Pie
import pyecharts.options as opts
from flask import Flask, render_template

app = Flask(__name__)

# 国外：国家，累计确诊，累计死亡
foreign_data = getForeignData.ForeignData()
foregin_name, foregin_total_confirm, _, foregin_dead, _ = foreign_data.foreign_total_data()

# 国内：日期，累计确诊，累计死亡
china_data = getChinaData.ChinaData()
date_list, china_confirm, _, china_dead, china_heal, china_importedCase = china_data.china_total_data()

# 国内：累计确诊成分，包括治愈、死亡、现存确诊
china_abs_info = china_data.china_abstract_data()

# 国内各省 ： 省名，累计确诊数据
province_data = getProvinceData.ProvinceData()
province_name, province_total_confirm = province_data.province_total_data()


def bar_base():
    foreignBar = (
        Bar()
            .add_xaxis(foregin_name[:10])
            .add_yaxis('确诊数', foregin_total_confirm[:10])
            .add_yaxis('死亡数', foregin_dead[:10])
            .set_global_opts(title_opts=opts.TitleOpts(title="国外疫情确诊Top10", subtitle="数据来源：腾讯新闻"))
    )
    return foreignBar


def line_base():
    chinaLine = (
        Line()
            .add_xaxis(date_list)
            .add_yaxis('确诊', china_confirm, is_symbol_show=True, label_opts=opts.LabelOpts(is_show=False),
                       markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"), ]))
            .add_yaxis('死亡', china_dead, is_symbol_show=True, label_opts=opts.LabelOpts(is_show=False),
                       markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]))
            .add_yaxis('治愈', china_heal, is_symbol_show=True, label_opts=opts.LabelOpts(is_show=False),
                       markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]))
            .add_yaxis('输入病例', china_importedCase, is_symbol_show=True, label_opts=opts.LabelOpts(is_show=False),
                       markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]))
            .set_global_opts(title_opts=opts.TitleOpts(title="国内疫情走势", subtitle="数据来源：腾讯新闻"),
                             yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=7, interval=3)))
    )
    return chinaLine


def map_base():
    chinaMap = (
        Map()
            # .add("累计确诊", maptype="world")
            .add("累计确诊", [list(z) for z in zip(province_name, province_total_confirm)], maptype="china", is_roam=True)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="中国累计确诊数据"),
            visualmap_opts=opts.VisualMapOpts(max_=3600,
                                              is_piecewise=True,
                                              pieces=[{"max": 0, "label": '0人'}, {"min": 1, "max": 9, "label": '1-9人'},
                                                      {"min": 10, "max": 99, "label": '10-99人'},
                                                      {"min": 100, "max": 499, "label": '100-499人'},
                                                      {"min": 500, "max": 999, "label": '500-999人'},
                                                      {"min": 1000, "max": 9999, "label": '1000-9999人'},
                                                      {"min": 10000, "label": '10000人及以上'}]),
        )
    )
    return chinaMap


def pie_base():
    chinaAbsPie = (
        Pie()
            .set_global_opts(title_opts=opts.TitleOpts(title="中国疫情数据构成分析", subtitle="数据来源：腾讯新闻"))
            .add(series_name="中国疫情构成",
                 data_pair=china_abs_info
                 )
    )
    return chinaAbsPie


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/foreignbar")
def barChart():
    return render_template("barChart.html")


@app.route("/chinaline")
def lineChart():
    return render_template("lineChart.html")


@app.route("/chinapie")
def pieChart():
    return render_template("pieChart.html")



@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()


@app.route("/lineChart")
def get_line_chart():
    l = line_base()
    return l.dump_options_with_quotes()


@app.route("/mapChart")
def get_map_chart():
    m = map_base()
    return m.dump_options_with_quotes()


@app.route("/pieChart")
def get_pie_chart():
    p = pie_base()
    return p.dump_options_with_quotes()


if __name__ == "__main__":
    app.run(host='localhost', port=776)
