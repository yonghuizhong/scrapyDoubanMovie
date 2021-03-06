# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    image = scrapy.Field()
    href = scrapy.Field()
    name = scrapy.Field()
    introduce = scrapy.Field()
    star = scrapy.Field()
    commentNum = scrapy.Field()
    quote = scrapy.Field()
