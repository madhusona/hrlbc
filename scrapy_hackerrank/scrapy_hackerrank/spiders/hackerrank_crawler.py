# -*- coding: utf-8 -*-
import scrapy


class HackerrankCrawlerSpider(scrapy.Spider):
    name = 'hackerrank_crawler'
    allowed_domains = ['hackerrank.com']
    start_urls = ['http://hackerrank.com/']

    def parse(self, response):
        pass
