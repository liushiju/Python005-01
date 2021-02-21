"""
安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，
并以 UTF-8 字符集保存到 csv 格式的文件中。
"""
import csv

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

proxies = {"http": "58.220.95.86:9401"}
ua = UserAgent()


def crawl_maoyan():
    headers = {
        "User-Agent": ua.random,
        "Cache - Control": "no - cache",
        "Connection": "keep - alive",
    }
    response = requests.get('https://maoyan.com/films?showType=3', headers=headers, proxies=proxies)
    html = response.text
    parse(html)


def parse(html):
    html = html.replace('\r', "").replace('\n', "").replace('\t', "")
    soup = BeautifulSoup(html, 'lxml')
    item_array = soup.select('.movie-hover-info')

    for item in item_array:
        item = list(item.children)
        res = {
            'title': item[1].attrs['title'],
            'tag': item[3].text.split(':')[1].strip(' ') if item[3] else '未知',
            'release_time': item[-2].text.split(':')[1].strip(' ') if item[-2] else '待定'
        }

        write_csv(res)

    # item_array = soup.find_all('div', attrs={'class':'movie-hover-info'})
    # for item in item_array:
    #     res = {
    #         'title': item.find_all('div', attrs={'class':'movie-hover-title'})[0].find('span').text,
    #         'tag': item.find_all('div', attrs={'class':'movie-hover-title'})[1].contents[-1],
    #         'release_time': item.find_all('div', attrs={'class':'movie-hover-title'})[-1].contents[-1]
    #     }


def write_csv(res):
    with open('movies.csv', 'a+', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'tag', 'release_time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(res)


def run():
    with open('movies.csv', 'a+', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'tag', 'release_time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

    crawl_maoyan()


if __name__ == '__main__':
    run()