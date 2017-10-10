# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib.request import urlopen
# from scrapy.pipelines.images import ImagesPipeline
from imgdb import settings

class ImgdbPipeline(object):
    def process_item(self, item, spider):
        #print(spider.name,item,'已经到达管道')
        dir_path = '%s\\%s'%(settings.IMAGES_STORE,spider.name)#存储路径
        print ('dir_path',dir_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)#输入路径dir_path作为参数，生成目录
        pic_url = item['image_urls']
        image_name = pic_url.split('/')[-1]
        #可以理解为，生成一个img_file对象，带有文件路径和文件名属性。
        with open(r'%s\\%s'%(dir_path,image_name),'wb') as img_file:
            conn = urlopen(pic_url)#下载图片,此时图片保存在内存中，同时赋值给变量conn
            img_file.write(conn.read())#读取内存的图片数据，然后写入img_file
        img_file.close()#关闭img_file对象，将图片的数据保存在相应文件名
        return item
