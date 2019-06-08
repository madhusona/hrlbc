# -*- coding: utf-8 -*-
import scrapy


class HackSpider(scrapy.Spider):
    name = 'hack'
    allowed_domains = ['hackerrank.com']
    start_urls = ['http://localhost:8887/hack.html']

    def parse(self, response):
        print("procesing:"+response.url)
        username=response.xpath("//a[@class='cursor leaderboard-hackername rg_5']/text()").extract()
        score=response.xpath("//div[@class='span-flex-3']/p/text()").extract()
        row_data=zip(username,score)
        for item in row_data:
            score={
                'page':'infosystest7',
                'username':item[0],
                'score':item[1],
                'batch':'product',
                'mode':'test'
            }
            
            yield score
