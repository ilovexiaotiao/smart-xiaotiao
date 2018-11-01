#coding=utf8
import requests
import itchat, time
from itchat.content import *
import sys
import time
import datetime
import os
sys.path.append('')
from core.SearchEngine.Title_Search import Titlesearch
COMMAND_LIST = ['搜索：','下载：']

@itchat.msg_register(TEXT)
def WXCommander(msg):
    if (len(msg.text.split(COMMAND_LIST[0]))>1):
        name = msg.text.split("搜索：")
        print(len(name))
        if ( len(name) > 1):
            msg.user.send('搜索开始')
            search = Titlesearch(name[1])
            for i in range(len(search.search_file())):
                time.sleep(1.5)
                msg.user.send('%s' % (search.show_file_title()[i]))
            msg.user.send('搜索结束')

    if (len(msg.text.split(COMMAND_LIST[1]))>1):
        name = msg.text.split("下载：")
        print(len(name))
        if (len(name) > 1):
            msg.user.send('下载开始')
            download = Titlesearch(name[1])
            download_number=download.show_file_title().index(name[1])
            download.download_file(download_number)
            download_path = os.path.split(os.path.abspath('itchat.pkl'))[0]
            download_name = download.download_file_name + download.show_file_extention()[download_number]
            print(download_name)
            if (os.path.exists(download_path+'\\'+download_name)):
                msg.user.send('下载结束,开始接收')
                msg.user.send("@fil@%s" % download_name)
                msg.user.send('接收结束')
                os.remove(download_path+'\\'+download_name)




itchat.auto_login(True)
itchat.run(True)




