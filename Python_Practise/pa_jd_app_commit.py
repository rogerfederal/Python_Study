import requests
#
#
# 文件路径
path = '/Users/u44084750/Desktop/mp3/'
num = 1788


def response(flow):
    global num
    # 经测试发现视频url前缀主要是3个
    target_urls = ['http://v1-dy.ixigua.com/', 'http://v9-dy-z.ixigua.com/',
                   'http://v3-dy-y.ixigua.com/','http://v3-dy.ixigua.com/',
                   'http://v9-dy-x.ixigua.com/','http://v6-dy.ixigua.com/',
                   'http://v3-dy-x.ixigua.com/','http://v3-dy-z.ixigua.com/',
                   'http://v9-dy.ixigua.com/','http://v9-dy-z.ixigua.com/']
    for url in target_urls:
        if flow.request.url.startswith(url):
            # with open("/Users/u44084750/Desktop/mp33/url.txt",'a') as f:
            #     f.write(flow.request.url+"\n")
            filename = path + str(num) + '.mp4'
            # 使用request获取视频url的内容
            # stream=True作用是推迟下载响应体直到访问Response.content属性
            # res = requests.get(flow.request.url, stream=True)
            res = requests.get(flow.request.url)
            # 将视频写入文件夹
            with open(filename, 'ab') as f:
                f.write(res.content)
                f.flush()
                print(filename + '下载完成')
            num += 1


# def request(flow):
#
#  flow.request.headers['User-Agent'] = 'MitmProxy'
#
#  print(flow.request.headers)