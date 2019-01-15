import requests
import json
from concurrent.futures import ProcessPoolExecutor
from time import sleep

urls = ["https://mp.weixin.qq.com/cgi-bin/appmsg?token=2127896997&lang=zh_CN&f=json&ajax=1&random=0.23389815718580276&action=list_ex&begin={}&count=5&query=&fakeid=MzI0Njc5ODkxMA%3D%3D&type=9".format(n) for n in range(0,300,5)]
header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
cook = {
        "Cookie": "pgv_pvi=6323830784; RK=nOpQDB+hTu; ptcz=52a05679c144f17ba94ceb9dd6d9448e6843e9d54d62f25708e877153ad8dcb4; pgv_pvid=3218546916; o_cookie=3065482; pac_uid=1_3065482; ua_id=w8K2nKg50V7XX2PCAAAAAAuarDb2zbHsFSTgVC2oakU=; mm_lang=zh_CN; ts_uid=3004905248; _ga=GA1.2.1482780196.1533950593; tvfe_boss_uuid=979c6ce8f1b64e45; ptui_loginuin=3065482@qq.com; noticeLoginFlag=1; openid2ticket_oKPsS5uHmp9M-RLXF8UzZASd0vLg=pBHDFSubOeIg+5baEI8MfiumfQlZUSQCCBSjXGd2tpQ=; pgv_si=s4355736576; uuid=41d253ceb024d665a71db10630eebb0b; data_bizuin=3860003624; bizuin=3860003624; data_ticket=iUqIDOk4Ll8h+EPiw2ThLJfPxg+lMF4suki9U14T+WRhg4lslwNy2yhKAAd+0p42; slave_sid=QlBUNGZfWkJKSmgwZDdjVlhlQmR0NWRjdWoyRHBpcVFTV3hOMUpnZU4yMzhVbDRmdldhSklmZWZfNHMxeHV2RWR1VFViNVF1UVg3UFhQa0NOdUJVUl95QXcwaEsxdkI0cWtUaHlyVWdZVXR5aVc5bW13c0Jaa1Jrb2g2SXM5bTdkdkRMT081YlZhbnY1SzFU; slave_user=gh_5e8e9e916841; xid=9845cb26e5ce23f727079534a7f2cb23"
}

def GetInfo(url):
    response = requests.get(url,headers=header,cookies=cook, verify=False).content
    print(response)
    result = json.loads(response.decode())
    for i in range(len(result['app_msg_list'])):
        name = result['app_msg_list'][i]['title']
        link = result['app_msg_list'][i]['link']
        data = name+"\n"+":"+link+"\n"
        print(data)
        sleep(3)
        with open('/Users/u44084750/Desktop/mp3/devops.txt','a') as f:
            f.write(data)


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=10) as pool:
        pool.map(GetInfo, urls)