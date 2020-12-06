import requests
from queue import Queue
from bs4 import BeautifulSoup
import json
import re

urlQueue = Queue()
parseQueue = Queue()

# 下载网页链接数据并推送至队列
def zhihuScrapy():
    url = 'https://www.zhihu.com/question/25906401'
    answerURL = 'https://www.zhihu.com/api/v4/questions/25906401/answers?include=data[*].is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata[*].mark_infos[*].url%3Bdata[*].author.follower_count%2Cbadge[*].topics%3Bsettings.table_of_content.enabled%3B&limit=20&offset=0&platform=desktop&sort_by=default'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }
    urlQueue.put(answerURL)
    is_end = False
    r = requests.get(url, headers=headers).text
    bs = BeautifulSoup(r, "html.parser")
    title = bs.title
    filename_old = title.string.strip()
    filename = re.sub('[\/:*?"<>|]', '-', filename_old)
    filename = filename.split('-')[0]
    while not is_end and not urlQueue.empty():
        answer_url = urlQueue.get()
        response = requests.get(answer_url, headers=headers).text
        # print(response)
        json_to_dict = json.loads(response)
        is_end = json_to_dict['paging']['is_end']
        answer_url = json_to_dict['paging']['next']
        urlQueue.put(answer_url)
        data = json_to_dict['data']
        parseQueue.put(data)
    return filename

# 解析数据
def parsedata():
    filename = zhihuScrapy()
    fname = filename.strip()
    with open(f'{fname}.json', 'a+') as f:
        json_dict = {}
        while not parseQueue.empty():
            data = parseQueue.get()
            for d in data:
                name = d['author']['name']
                comment = d['excerpt']

                response = {
                    name: comment
                }

                json_dict.update(response)
        json.dump(json_dict, fp=f, ensure_ascii=False)

if __name__ == "__main__":
    parsedata()
