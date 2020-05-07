import requests
import random


#  西瓜
class Watermelon:

    headers = {
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; YAL-AL00 Build/LYZ28N) '
                      'VideoArticle/8.2.0 ttnet okhttp/3.10.0.2',
        'Cookie': 'install_id=395460135361661; ttreq=1$7bc2c6643023e2ba68447362b53b65def198a0f0; '
                  'odin_tt=6da4a27ee8267e621df0db1d153bf08a43772482c9c6c18c47d3bb99a6284e2ca9211b6e91dd6065c'
                  'fe3c43cff53c433ec3200d4075a7ad619bf9b32a011c3eb; qh[360]=1',
        'X-Khronos': '1588842390',
    }

    def __init__(self, params, url):
        self.params = params
        self.url = url

    def author_item_requests(self):
        author_item = requests.get(url=self.url, headers=self.headers, params=self.params, verify=False)
        print(author_item.text)


if __name__ == '__main__':
    # 个人详情页
    # param = {
    #     'to_user_id': '71819689634',
    #     'device_id': '3069472387378669',  # 设备生成id
    #     'channel': 'tengxun2',
    #     'aid': '32',
    #     'app_name': 'video_article',
    #     'version_code': '820',
    #     'device_platform': 'android',
    #     'device_type': 'YAL-AL00',
    #     'os_version': '5.1.1',
    # }
    # urls = 'https://is.snssdk.com/video/app/user/home/v7/'
    # 列表页
    # param = {
    #     'to_user_id': '71819689634',
    #     'tab': 'video',
    #     'next_offset': '0',
    #     'max_behot_time': '1586499046',
    #     'device_id': '3069472387378669',
    #     'channel': 'tengxun2',
    #     'aid': '32',
    #     'app_name': 'video_article',
    #     'version_code': '820',
    #     'version_name': '8.2.0',
    #     'device_platform': 'android',
    #     'device_type': 'YAL-AL00',
    #     'os_version': '5.1.1'
    # }
    # urls = 'https://is.snssdk.com/video/app/user/videolist/v2/'
    # max_behot_time对应翻页  max_behot_time是最后一条数据的behot_time字段

    param = {}
    urls = ''

    tou_ti_ao = Watermelon(param, urls)
    tou_ti_ao.author_item_requests()


