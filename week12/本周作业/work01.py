#!/usr/bin/env python
import csv
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
from collections import Counter
'''
安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
'''

ua = UserAgent()


def crawl_maoyan(url):
    # user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    # headers = {}
    # headers['user-agent'] = user_agent
    headers = {
        "User-Agent": ua.random,
        "Cache - Control": "no - cache",
        "Connection": "keep - alive",
        "Host": "maoyan.com",
    }
    response = requests.get(url, headers=headers)
    print(response.status_code)
    bs_info = bs(response.text, 'html.parser')
    # print(bs_info)
    return bs_info


def get_htmls(url):
    bs_info = crawl_maoyan(url)
    baseurl = 'https://maoyan.com'
    urls = []
    for tags in bs_info.find_all('div', attrs={'class': 'main'}):
        for atag in tags.find_all('a'):
            url = baseurl + atag.get('href')
            urls.append(url)
    return urls


def parse(url):
    all_urls = get_htmls(url)
    htmls = Counter(all_urls)
    urls = [html for html in htmls]
    # for url in all_urls:
    #     if url not in urls:
    #         urls.append(url)
    print(urls)
    result = []
    for url in urls:
        bs_info = crawl_maoyan(url)
        for tags in bs_info.find_all('div', attrs={'class':'movie-brief-container'}):
            # 获取电影名称
            movie_name = tags.find('h1').text
            # 获取电影类型
            movie_t = tags.find('li').text
            movie_type = movie_t.replace('\n','、').strip('、')
            # 上映时间
            movie_t = tags.find('ul').text
            movie_time = movie_t.split('分钟')[1].replace('\n','').strip()
            res = [f"{movie_name}", f"{movie_type}", f"{movie_time}"]
            result.append(res)
    print(result)
    return result


def save_to_csv(url):
    result = parse(url)
    title = ['电影名称', '电影类型', '上映时间']
    with open("猫眼TOP10.csv", 'w', newline='', encoding='utf-8') as t:
        writer = csv.writer(t)
        writer.writerow(title)
        writer.writerows(result)


if __name__ == '__main__':
    url = 'https://maoyan.com/board'
    save_to_csv(url)