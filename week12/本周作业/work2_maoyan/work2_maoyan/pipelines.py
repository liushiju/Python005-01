# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import pandas as pd

class Work2MaoyanPipeline:
    def process_item(self, item, spider):
        movie_title = item['movie_title']
        movie_type = item['movie_type']
        movie_time = item['movie_time']
        headline = ['电影名称', '电影类型', '上映时间']
        res = [[movie_title.strip(), movie_type.strip(), movie_time.strip()]]
        print(res)
        # with open('./猫眼TOP10_scrapy.csv', 'a+',newline='', encoding='gbk') as f:
        #     reader = csv.reader(f)
        #     writer = csv.writer(f)
        #     for row in reader:
        #         if row[0] == '':
        #             writer.writerow(headline)
        #         else:
        #             writer.writerows(res)

        movie1 = pd.DataFrame(data = res)
        movie1.to_csv('./猫眼TOP10_scrapy.csv', mode='a', encoding='gbk', index=False, header=False)

        return item
