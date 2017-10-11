# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class Dbmovtop250Pipeline(object):
    def open_spider(self,spider):
        config = {'host': 'localhost',
                  'port': 3306,
                  'user': 'root',
                  'passwd': 'password',
                  'charset': 'utf8',
                  'database': 'douban'}
        #爬虫启动时，python3连接MySQL数据库
        self.conn = pymysql.connect(**config)
        #同一类中的函数和方法中的变量如果要互相调用，用self.conn作变量，不能用conn
        self.cur = self.conn.cursor()  # 生成一个操作光标
        #用光标的execute方法执行MySQL命令
        try:
            self.cur.execute(
                'create table movies252 ('
                'rank INT, '
                'name varchar(20), '
                'score FLOAT)')
        except:
            print('表格已存在')

    def process_item(self, item, spider):
        print(spider.name,'pipelines')  #调试

        self.cur.execute("insert into movies252 (rank, name, score) "
                       "values ('{}', '{}', '{}')".format(
            item['mov_rank'],
            item['mov_name'],
            item['mov_score']))
        self.conn.commit()
        return item
    def spider_close(self,spider):
        self.cur.close()
        self.conn.close()
