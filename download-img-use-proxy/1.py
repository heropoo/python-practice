# coding: utf8

from download import download_img
from download import set_proxy

import csv

set_proxy()

download_path = './images'
with open('./export_urls.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        # print(row)
        img_url = row[1]
        filename = row[0]
        ret = download_img(img_url, filename, download_path)
        print(ret)




