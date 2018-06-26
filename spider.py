import json
import requests
from json import loads
from headers import headers


def get_url_list():
        data = {'viewFlag':'A','sortType':'default','searchStyle':'','searchRegion':'city:','searchFansNum':'','currentPage':'1','pageSize':'100'} #post参数
        header = {'content-type':'application/jaon','user-agent':headers()}
        url = 'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8'
        r = requests.post(url,data=data,headers=header)
        html = r.text
        json = loads(html) #json转成dict
        return json['data']['searchDOList']
for i in get_url_list():
    print (i['userId'])
    exit()
    s = requests.request()