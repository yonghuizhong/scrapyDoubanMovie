# -*- coding: utf-8 -*-
import scrapy
from doubanMovie.items import DoubanmovieItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'  # 爬虫名字，与scrapy项目名不能重复
    allowed_domains = ['movie.douban.com']  # 允许的域名，不在这个下的，不爬取
    start_urls = ['http://movie.douban.com/top250']  # 入口url

    def parse(self, response):  # 进行解析
        print(response.status, response.headers)
        item_list = response.xpath("//div[@class='item']")  # 得到一个页面的25个item
        print(len(item_list))
        for item in item_list:
            movie_item = DoubanmovieItem()
            movie_item['id'] = item.xpath("./div/em/text()").extract_first()
            movie_item['image'] = item.xpath("./div/a/img/@src").extract_first()
            movie_item['href'] = item.xpath("./div/a/@href").extract_first()
            movie_item['name'] = item.xpath(".//div[@class='hd']/a/span[1]/text()").extract_first()

            introduce = item.xpath(".//div[starts-with(@class, 'bd')]/p[1]/text()").extract()
            movie_item['introduce'] = [''.join(i.strip('...').split()) for i in introduce]

            movie_item['star'] = float(item.xpath(".//span[@class='rating_num']/text()").extract_first())
            movie_item['commentNum'] = int(item.xpath(".//div[@class='star']/span[last()]/text()").extract_first().rstrip("人评价"))
            movie_item['quote'] = item.xpath(".//p[@class='quote']/span[@class='inq']/text()").extract_first()

            yield movie_item  # 到pipelines，存储、去重等等操作

        next_href = response.xpath(".//span[@class='next']/a/@href").extract()
        if next_href:
            next_href = next_href[0]
            yield scrapy.Request('http://movie.douban.com/top250' + next_href, callback=self.parse)  # 回调函数为parse
