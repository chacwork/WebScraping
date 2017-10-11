# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy

class Dbmovtop250Item(scrapy.Item):
    # define the fields for your item here like:
    mov_rank = scrapy.Field()
    mov_name = scrapy.Field()
    mov_score = scrapy.Field()

    #image_url = scrapy.Field()
    #images = scrapy.Field()
