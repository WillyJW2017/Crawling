from urllib import request
import requests
from bs4 import BeautifulSoup
import os
import threading

gLock = threading.Lock()
BASE_URL = 'http://www.doutula.com/photo/list/?page='
PAGE_URL_LIST = []
IMG_URL_LSIT = []
for i in range(1,4):
    url = BASE_URL + str(i)
    PAGE_URL_LIST.append(url)

def procuder():
    # global PAGE_URL_LIST
    while True:
        gLock.acquire()
        if len(PAGE_URL_LIST) == 0:
            gLock.release()
            break
        else:
            page_url = PAGE_URL_LIST.pop()
            gLock.release()
            response = requests.get(page_url)
            res = response.content
            soup = BeautifulSoup(res, 'html.parser')
            # 获取图片的地址
            imglist = soup.find_all('img', attrs={'class': 'img-responsive lazy image_dta'})
            gLock.acquire()
            for img in imglist:
                img_url = img['data-original']
                IMG_URL_LSIT.append(img_url)
            gLock.release()

def customer():
    # 下载图片
    # global IMG_URL_LSIT
    while True:
        gLock.acquire()
        if len(IMG_URL_LSIT) == 0:
            gLock.release()
            continue
        else:
            img_url = IMG_URL_LSIT.pop()
            gLock.release()
            split_list = img_url.split('/')
            file_name = split_list.pop()
            path = os.path.join('images', file_name)
            request.urlretrieve(img_url, filename=path)

def main():
    # 创建5个线程作为生产者，去爬取图片的url
    for i in range(5):
        th = threading.Thread(target=procuder)
        th.start()

    # 创建8个线程作为消费者，下载图片
    for i in range(4):
        th = threading.Thread(target=customer)
        th.start()


if __name__ == '__main__':
    main()