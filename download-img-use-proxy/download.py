# coding: utf8

import urllib.request
from httplib2 import socks
import socket
import sys


def download_img(img_url, filename, download_path):

    full_filename = download_path + '/' + filename
    print("Download", img_url, "to "+full_filename)
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    try:
        request = urllib.request.Request(img_url, headers=header)
        reponse = urllib.request.urlopen(request).read()
        fh = open(full_filename, "wb")
        fh.write(reponse)
        fh.close()
        return True
    except:
        print("Unexpected error:", sys.exc_info())
        return False


def set_proxy():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080)
    socket.socket = socks.socksocket


if __name__ == '__main__':

    set_proxy()

    img_url = "https://danadarurat-files-prod.oss-ap-southeast-5.aliyuncs.com/face/id_card_face/811100370020210428161039_3i0sx2sk3s.jpg"
    filename = '123.png'
    download_path = './images'
    ret = download_img(img_url, filename, download_path)
    print(ret)
