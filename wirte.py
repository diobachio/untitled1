import requests
import re
import os
from headers import headers
from multiprocessing import Pool,cpu_count
import time
import asyncio

now = lambda: time.time()
header = {'content-type': 'application/jaon', 'user-agent': headers()}
def main(page):
    url = 'https://wall.alphacoders.com/by_category.php?'
    params = {'id': 1, 'name': 'Abstract Wallpapers', 'page': page}
    data = {'view': 'paged', 'min_resolution': 0x0, 'resolution_equals': '>=', 'sort': 'rating'}
    response = requests.post(url, params=params, data=data, headers=header)
    html = response.text
    image_url_list = re.findall(r'download-button" data-href="(.*?)">', html)
    for i in image_url_list:
        image = requests.get(i, headers=header)
        file_name = re.findall(r'wallpaper/(.*?)/images', i)[0]
        if not os.path.exists('D:\desktop\wallpaper\%d' % page):  # 判断存在文件夹是否r存在
            os.mkdir('D:\desktop\wallpaper\%d'% page)  # 不存在则新建文件夹
        with open('D:\desktop\wallpaper\%d\%s.jpg' % (page,file_name), 'wb') as file:
            file.write(image.content)
        print('图片:%s 下载完毕' % file_name)
    print('第%d页下载完毕' % page)

if __name__=="__main__":
    p =Pool(cpu_count())
    start = now()
    p.apply_async(main,(1,))
    p.close()
    p.join()
    print('用时%d秒'%( now() - start))









