# -*- coding: utf-8 -*-
import scrapy
from work2_maoyan.items import Work2MaoyanItem
from scrapy.selector import Selector


class MaoyanmovieSpider(scrapy.Spider):
    name = 'maoyanmovie'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/board']

    # 解析主页获取电影链接
    def parse(self, response):
        baseurl = 'https://maoyan.com'
        links = Selector(response=response).xpath('//div[@class="main"]')
        for link in links:
            url = link.xpath('.//dd/a/@href')
            urls = [baseurl + link for link in url.extract()]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse2)

    def parse2(self, response):
        item = Work2MaoyanItem()
        movies = Selector(response=response).xpath(
            '//div[@class="movie-brief-container"]')
        for movie in movies:
            # 获取电影名称
            title = movie.xpath('./h1/text()')
            movie_title = ''.join(t for t in title.extract())
            # print(movie_title)
            # 获取电影类型
            movie_t = movie.xpath('.//li[1]/a/text()')
            movie_type = ','.join(m for m in movie_t.extract())
            # print(movie_type)
            # 获取电影上映时间
            t = movie.xpath('.//li[3]/text()')
            movie_time = ''.join(d for d in t.extract())
            # print(movie_time)
            
            item['movie_title'] = movie_title
            item['movie_type'] = movie_type
            item['movie_time'] = movie_time
            yield item