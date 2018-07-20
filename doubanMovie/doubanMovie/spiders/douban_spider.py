# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'  # 爬虫名字，与scrapy项目名不能重复
    allowed_domains = ['movie.douban.com']  # 允许的域名，不在这个下的，不爬取
    start_urls = ['http://movie.douban.com/top250']   # 入口url

    def parse(self, response):  # 进行解析
        content = BeautifulSoup(response.text, 'html.parser')
        print(content.text)
