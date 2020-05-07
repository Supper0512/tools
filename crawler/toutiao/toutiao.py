import requests
import random


#  头条
class TouTiAo:

    headers = {
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; YAL-AL00 Build/LYZ28N) NewsArticle/7.1.2 okhttp/3.10.0.2',
        'Cookie': 'install_id=8432019592920; ttreq=1$0c5b0f1439b782077c3ec74acff14f55b057c014; odin_tt=6f79593b5ec6f'
                  '247e7cf688c767fb74bb6758092f017884bb0d3fb06e0b6b152e621ba932dc0ef7e6215b558d3b492a138c3badb6ef7fb40'
                  '1529ecac3e747036; history=alrvlFic6pJZXJCTWBmSmZt6KW7ziqlLPUtSc4vvMYhcjtuo9m4%2BAxPLJTFTBofLcZu2v%'
                  '2BhpYOK4JJoB4q1tmsF%2BgInjEqsbiLe5qEwAJMfAAOZpLlcHyfEJMARcjttUdkemgYn3EnMLWC7Lcp0DE8sl%2Fksgufm%2F'
                  'nr5zYGK%2BxNXD4HCZgfW1ZiHXEo5LHKdYDoB46tVWNXyXGA%2BxHLgct3n%2FcRMHJr5L4oxgM6doKoDMFGYGu2zuYb0DTOyXR'
                  'OaAbSj0283AxH5J%2FBxI5ebmxGUMTByX2DlAcuvy3uxkYOK7JJgF1ify4C7ILTx%2BYH3FXw%2BCXC18Hiz3gH0PyBSBeRD%2F'
                  'ifaB7BMyZ3AAAAAA%2F%2F8%3D; qh[360]=1',
    }

    def __init__(self, params, url):
        self.params = params
        self.url = url

    def author_item_requests(self):
        author_item = requests.get(url=self.url, headers=self.headers, params=self.params, verify=False)
        print(author_item.text)


if __name__ == '__main__':
    param = {
        'category': 'profile_all',
        'visited_uid': '50502346173',
        'stream_api_version': '88',
        'count': '20',
        'offset': '0',
        'device_id': '3069472387378669',
        'channel': 'baidu',
        'aid': '13',
        'app_name': 'news_article',
        'version_code': '712',
        'device_platform': 'android',
        'device_type': 'YAL-AL00',
        'os_version': '5.1.1',
    }
    # 个人主页介绍
    # urls = 'https://lf.snssdk.com/user/profile/homepage/v7/?user_id=50025817786&refer=all'
    # 文章列表页 今日头条极速版
    # urls = 'https://is.snssdk.com/pgc/ma_mobile/?page_type=1&max_behot_time=1588833675000&
    # aid=35&media_id=50044041847&count=10&version=2&as=A1E5FE3BA3EBC83&cp=5EB39BDC18633E1&timestamp=1476282741654'
    # 文章列表页 今日头条
    urls = 'https://is-hl.snssdk.com/api/feed/profile/v1/?'

    tou_ti_ao = TouTiAo(param, urls)
    tou_ti_ao.author_item_requests()


