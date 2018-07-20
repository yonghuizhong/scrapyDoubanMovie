# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from doubanMovie.items import DoubanmovieItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'  # 爬虫名字，与scrapy项目名不能重复
    allowed_domains = ['movie.douban.com']  # 允许的域名，不在这个下的，不爬取
    start_urls = ['http://movie.douban.com/top250']  # 入口url

    def parse(self, response):  # 进行解析
        content = BeautifulSoup(response.text, 'html.parser')
        # print(content.text)
        item_list = content.select('div.item')  # 得到一个页面的25个item
        print(len(item_list))
        for item in item_list:
            movie_item = DoubanmovieItem()
            movie_item['id'] = item.select('div.pic em')[0].text
            movie_item['image'] = item.select('div.pic img')[0]['src']
            movie_item['href'] = item.select('div.pic a')[0]['href']
            movie_item['name'] = item.select('div.hd a span')[0].text

            introduce = item.select('div.bd p')[0].text.split()
            movie_item['introduce'] = ''.join(introduce)

            movie_item['star'] = item.select('div.star span.rating_num')[0].text
            movie_item['commentNum'] = item.select('div.star span:nth-of-type(4)')[0].text.rstrip('人评价')
            if item.find('p.quote span'):
                movie_item['quote'] = item.select('p.quote span')[0].text
            else:
                movie_item['quote'] = 'none'

            yield movie_item    # 到pipelines，存储、去重等等操作

        next_href = content.select('span.next a')
        if next_href:
            next_href = content.select('span.next a')[0]['href']
            yield scrapy.Request('http://movie.douban.com/top250' + next_href, callback=self.parse)  # 回调函数为parse
