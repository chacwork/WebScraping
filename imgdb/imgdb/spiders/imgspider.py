# -*- coding: utf-8 -*-
import scrapy
from imgdb.items import ImgdbItem

class ImgspiderSpider(scrapy.Spider):
    name = 'imgspider'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        imgs = ImgdbItem()
        x = response.xpath(
            '//*[@id="content"]/div/div[1]/ol/li/div/div[1]/a/img/@src').extract()
        for i in x:
            imgs['image_urls'] = i
            # print('spider.name',imgs['image_urls'])
            yield imgs
        try:
            nextlink = 'https://movie.douban.com/top250'+response.xpath(
            '//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract()[0]
        except:
            nextlink =False
        if nextlink:
            #如果有下一页，就用scrapy.Request发起请求，定义当前的parse为回调函数，用于解释请求回来的response
            yield scrapy.Request(nextlink, callback=self.parse)
