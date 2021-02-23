# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import pandas as pd
from pathlib import Path

class Work2MaoyanPipeline:
    def process_item(self, item, spider):
        movie_title = item['movie_title']
        movie_type = item['movie_type']
        movie_time = item['movie_time']
        headline = ['电影名称', '电影类型', '上映时间']
        res = [[movie_title.strip(), movie_type.strip(), movie_time.strip()]]
        print(res)
        savefile = './猫眼TOP10_scrapy.csv'
        movie1 = pd.DataFrame(data = res)
        if not Path(savefile).exists():
            movie1.to_csv(savefile, encoding='utf8', index=False, header=headline)
        movie1.to_csv(savefile, mode='a', encoding='utf8', index=False, header=False)
        return item
