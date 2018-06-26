import requests
from headers import headers
from html.parser import HTMLParser
import pyperclip
from win10toast import ToastNotifier
import time


weapon = []
status = []
seller = []
toaster = ToastNotifier()
now = time.time()
class Myparser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = 0

    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for each in attrlist:
                if attrname == each[0]:
                    return each[1]

        if tag == 'div' and _attr(attrs, 'data-wtype'):
            datas = {}
            datas['武器'] = str(_attr(attrs, 'data-weapon'))
            datas['紫卡名'] = _attr(attrs, 'data-weapon') + ' ' + _attr(attrs, 'data-name')
            datas['极性'] = _attr(attrs, 'data-polarity')
            datas['正属性'] = [_attr(attrs, 'data-stat1'), _attr(attrs, 'data-stat1val'),_attr(attrs, 'data-stat2'),_attr(attrs, 'data-stat2val'), _attr(attrs, 'data-stat3'),_attr(attrs, 'data-stat3val')]
            datas['负属性'] = [_attr(attrs, 'data-stat4'),_attr(attrs, 'data-stat4val')]
            datas['roll'] = _attr(attrs, 'data-rerolls')
            datas['price'] = _attr(attrs, 'data-price')
            weapon.append(datas)
        if tag == 'div' and _attr(attrs, 'title'):
            status.append(_attr(attrs, 'title'))
        if tag == 'div' and _attr(attrs, 'class') in ['attribute seller ','attribute seller patreon-badge']:
            self.flag = 1

    def handle_endtag(self, tag):
        if self.flag == 1:
            self.flag = 0

    def handle_data(self, data):
        data = data.strip()
        if self.flag and data:
            seller.append(data)


class RivenMarket():

    def __init__(self,wp):
        self.wp = wp
        self.url = 'http://riven.market/_modules/riven/showrivens.php?'
        self.header = {'content-type': 'application/jaon', 'user-agent': headers()}
        self.params = 'baseurl=aHR0cHM6Ly9yaXZlbi5tYXJrZXQv&platform=PC&limit=200&recency=-1&veiled=false&onlinefirst=true&polarity=all&rank=all&mastery=16&weapon=%s&stats=Any&neg=all&price=20000&rerolls=-1&sort=price&direction=ASC&page=1&time=%d' % (
            str(self.wp), int(1000 * now))


    def get_data(self):
        html = requests.get(self.url, params=self.params, headers=self.header, verify=False).text
        myparser = Myparser()
        myparser.feed(html)
        for i in range(0, len(weapon)):
            weapon[i]['seller'] = seller[i]
            weapon[i]['status'] = status[i]

    def ShowTheStatusSeller(self,maxprice,stat1,stat2='',stat3='',stat4=None):
        if stat2 == '':
            stat2 = stat1
        if stat3 == '':
            stat3 = stat1
        if stat4 == None:
            stat4 = []
        for each in weapon:
            if   ((stat1 in each['正属性']) and (stat2 in each['正属性']) and (stat3 in each['正属性'])) and (
                    int(each['price']) <= maxprice) and (each['负属性'][0] not in stat4) and (
                    each['status'] == 'Online and set to currently INGAME within the last 30 minutes.'):
                hi = '/w %s hey,wtb %s for %s ' % (each['seller'], each['紫卡名'], each['price'])
                print(
      '''____________________________________________________________________________
     %s   |||   %s''' % (each, hi))
                pyperclip.copy(hi)
                toaster.show_toast( '%s 有符合要求的货了' % self.wp)



    def ShowTheCheap(self,maxprice,roll=0):

        for each in weapon:
            if  (int(each['price']) <= maxprice) and (int(each['roll'])<=roll) and(each['status']== 'Online and set to currently INGAME within the last 30 minutes.'):
                hi = '/w %s hey,wtb %s for %s ' % (each['seller'], each['紫卡名'], each['price'])
                print(
    '''________________________________________________
    %s   |||   %s''' % (each,hi))
                pyperclip.copy(hi)
                toaster.show_toast('%s有便宜货了'% self.wp)

# stat英文列表
# Ammo	弹药
# ChannelDmg	引导伤害
# ChannelEff	引导效率
# Cold	冰
# Combo	连击数
# Corpus	c佬
# CritChance	爆率
# CritDmg	爆伤
# Damage	基伤
# Electric	电
# Finisher	处决
# Flight	飞行速度
# Grineer	g佬
# Heat	火
# Impact	冲击
# Infested	i佬
# Magazine	弹夹
# Multi	多重
# Punch	穿透
# Puncture	穿刺
# Range	范围
# Recoil	后坐力
# Reload	上弹
# Slash	切割
# Slide	滑砍爆率
# Speed	射速 攻速
# StatusC	触发率
# StatusD	触发时间
# Toxin	毒
# Zoom	变焦

#参数说明
# Spider(wp) 武器名第一个字母大写
# ShowTheStatusSeller(self,maxprice,stat1,stat2='',stat3='',stat4=None) stat4为负属性,如果有的话需要是list 123为正属性
# ShowMeTheSellerMin(self,maxprice,roll=0)
# wp 武器英文名

if __name__ == '__main__': #兰卡为例
    lanka = RivenMarket('Lanka')
    while True:
        lanka.get_data()
        lanka.ShowTheStatusSeller(10000,'Multi')
        lanka.ShowTheCheap(1000)
        time.sleep(300) #过多少秒循环1次


