import requests

post_url = "http://hd.chinatax.gov.cn/fagui/action/InitCredit.do"

post_data = {
    "articleField01": "",
    "articleField02": "",
    "articleField03": "2017",
    "articleField06": "",
    "taxCode": "110000",
    "cPage": "2",
    "randCode": "",
    "flag": "1",
    "scount": "0"
}

header = {
    "POST": "/fagui/action/InitCredit.do HTTP/1.1",
    "Host": "hd.chinatax.gov.cn",
    "Connection": "keep-alive",
    "Content-Length": "123",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Origin": "http://hd.chinatax.gov.cn",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer": "http://hd.chinatax.gov.cn/fagui/action/InitCredit.do",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
    "Cookie": "qd80-cookie=qdyy33-80; yfx_c_g_u_id_10003701=_ck18121819454914295421555304074; yfx_f_l_v_t_10003701=f_t_1545133549400__r_t_1545918075597__v_t_1545918075597__r_c_3; _Jo0OQK=77B0773BF8A77B72DB81AFF4CA57D3621A4D8B6CD693E8E72C36BC6A37C7470901FDE8CCD4778461B380EA5729157A752D32CA650CADE73883BA64E3B12FC0C90F71B918CCA8FE3BB9470EE0D297309F84070EE0D297309F8406FEBA99E062224F16F0DFB7DA5A877C2GJ1Z1IQ==; JSESSIONID=Qv_v97yEFXSK__R_aaR5Rz8Y_QFgArscFQjcdgstZC9x5YFzr2ru!377127501"
}

cook = {
    "Cookie":'qd80-cookie=qdyy33-80; yfx_c_g_u_id_10003701=_ck18121819454914295421555304074; JSESSIONID=q6Lv5IONHeaQ3TBuswCR1obC9PxETNKxPbyxiNYTP3e0eWfcWbfS!377127501; yfx_f_l_v_t_10003701=f_t_1545133549400__r_t_1545918075597__v_t_1545918075597__r_c_3; _Jo0OQK=77B0773BF8A77B72DB81AFF4CA57D3621A4D8B6CD693E8E72C36BC6A37C7470901FDE8CCD4778461B380EA5729157A752D32CA650CADE73883BA64E3B12FC0C90F71B918CCA8FE3BB9470EE0D297309F84070EE0D297309F8406FEBA99E062224F16F0DFB7DA5A877C2GJ1Z1IQ=='
}


response = requests.post(post_url,data=post_data,headers=header,cookies=cook).content
print(response.decode('utf-8'))