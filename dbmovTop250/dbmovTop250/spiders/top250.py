# -*- coding: utf-8 -*-
import scrapy
from dbmovTop250.items import Dbmovtop250Item


class Top250Spider(scrapy.Spider):
    name = 'top250'

    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250/']


    def parse(self, response):#负责处理response并返回处理的数据以及(/或)跟进的URL
        #print(response)
        movieset = Dbmovtop250Item()
        dbrank = response.xpath(
            '//*[@id="content"]/div/div[1]/ol/li/div/div[1]/em/text()').extract()
        # print(movies_rank)
        dbname = response.xpath(
            '//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()').extract()
        #print(movies_name)
        dbscore = response.xpath(
            '//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]/text()').extract()
        #print(movies_score)
        #movieset['image_url'] = response.xpath(
            #'//*[@id="content"]/div/div[1]/ol/li/div/div[1]/a/img/@src').extract()
        for x,y,z in zip(dbrank,dbname,dbscore):
            movieset['mov_rank']=int(x)
            movieset['mov_name']=y
            movieset['mov_score']=float(z)

            yield movieset
        try:
            nextlink = 'https://movie.douban.com/top250'+response.xpath(
            '//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract()[0]
        except:
            nextlink =False

        if nextlink:
            #如果有下一页，就用scrapy.Request发起请求，定义当前的parse为回调函数，用于解释请求回来的response
            yield scrapy.Request(nextlink, callback=self.parse)

        # for x,y,z in zip(dbrank,dbname,dbscore):
        #     movieset['mov_rank']=int(x)
        #     movieset['mov_name']=y
        #     movieset['mov_score']=float(z)
        #     yield movieset
