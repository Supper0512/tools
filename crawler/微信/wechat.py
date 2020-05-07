import requests
import time
import random

from lxml import etree


class WeChat:

    cookies = {
        'SUID': '674FFF3A5433B00S5E782300000A6B85',
        'SUV': '00907A6F3AFC054F5E7B17CFDEA4E188',
        'SNUID': '79128CF880852484C16A994981A052CB'
    }

    headers = {
        'Referer': 'https://weixin.sogou.com/weixinwap?query=%E4%BA%BA%E6%B0%91%E6%97%A5%E6%8A%A5&'
                   'type=1&ie=utf8&_sug_=y&_sug_type_=&s_from=input',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.149 Safari/537.36'
    }

    def __init__(self, url):
        self.url = url
        self.urls = []
        self.encrypted_urls = []
        self.item_requests()
        time.sleep(5)
        self.encrypted_requests()
        time.sleep(5)

    def item_requests(self):
        self.urls = []
        item_response = requests.get(url=self.url, cookies=self.cookies, headers=self.headers).json()
        for item in item_response['items']:
            xml = etree.XML(item.encode('utf-8'))
            url = xml.xpath('//encArticleUrl/text()')
            url_h = 'https://weixin.sogou.com' + url[0]
            self.urls.append(url_h)

    def encrypted_requests(self):
        self.encrypted_urls = []
        for url in self.urls:
            encrypted_response = requests.get(url=url, cookies=self.cookies, headers=self.headers).text
            new_url = ''
            for line in encrypted_response.split('\n'):
                if 'url +=' in line:
                    new_url += line.split("'")[1]
                else:
                    new_url.replace('@', '')
            self.encrypted_urls.append(new_url)

    def article_requests(self):
        """
        :return: dict
        :arg 如果返回数量过多 可改为流式处理 yield
        """
        article = dict()
        for url in self.encrypted_urls:
            article_response = requests.get(url=url, cookies=self.cookies, headers=self.headers).text
            html = etree.HTML(article_response)
            yield article_response


if __name__ == '__main__':
    url_we_chat = 'https://weixin.sogou.com/weixinwap?page=1&_rtype=json&query=%E4%BA%BA%E6%B0%91%E6%97%A5%E6%8A%A5&' \
          'type=1&ie=utf8&_sug_=y&_sug_type_=&s_from=input&'
    we_chat = WeChat(url_we_chat)
    we_chat.article_requests()

