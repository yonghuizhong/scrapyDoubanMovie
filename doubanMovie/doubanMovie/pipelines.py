# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

client = pymongo.MongoClient('localhost', 27017)
doubanMovieDB = client['doubanMovieDB']
top250 = doubanMovieDB['top250']


class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        data = dict(item)
        top250.insert(data)
        return item
