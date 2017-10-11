#coding:utf-8
import scrapy
from dbmovTop250.items import Dbmovtop250Item

class PictSpider(scrapy.Spider):
    name = 'Pict'

    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250/']


    def parse(self, response):#负责处理response并返回处理的数据以及(/或)跟进的URL
        pictitem = Dbmovtop250Item()
        pictitem['image_url']=response.xpath(
        '//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@src').extract()
        print(pictitem['image_url'])
