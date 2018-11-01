#coding=utf8
import requests
import urllib
import re
from urllib import parse
import datetime
import time
import json
LOCAL_URL = 'http://192.168.3.10:8099/'
USER_AGENT ='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core'
HEADERS = {'Authorization':'Basic YWRtaW46MTIzNA=='}
TITLE_SORT = ['name','path','data_modified','size']
WHOLE_WORD = [1,2]
PATH_COLUMN = [1,2]
DATE_MODIFIED_COLUMN = [1,2]
DATE_CREATED_COLUMN = [1,2]
FILE_TYPE = {'.doc','.docx','xls','xlsx','txt','csv','pdf'}
#INITIAL_REG =


class Titlesearch(object):
    def __init__(self,msg):
        super(Titlesearch, self).__init__()
        self.msg=msg
        self.url=LOCAL_URL
        self.headers=HEADERS
        self.useragent=USER_AGENT
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ts = str(int(time.mktime(time.strptime(now_time, "%Y-%m-%d %H:%M:%S"))))
        download_file_name = 'temp' + ts + '.'
        self.download_file_name = download_file_name

        #self.get_http = requests.get(self.url,headers=self.headers,params=self.params)

    def search_whole(self):
        search_params = {'j': '2', 's': self.msg, 'path_column': PATH_COLUMN[1],
                         'date_modified_column': DATE_MODIFIED_COLUMN[1], 'date_created_column': DATE_CREATED_COLUMN[1]}
        get_http = requests.get(self.url, headers=self.headers, params=search_params)
        whole_json = json.loads(get_http.text)
        return whole_json

    def search_range(self):
        return self.search_whole()['totalResults']

    def search_set(self):
        return self.search_whole()['results']

    def search_file(self):
        file_list=[]
        ranger = self.search_range()
        for i in range(ranger):
            if self.search_set()[i]['type'] == 'file':
                # print(i)
                file_list.append(self.search_set()[i])
               # title_list.append(search_set[i]['name'])
        return file_list

    def search_filetype(self,**kwargs):
        return "ok"

    def show_file_title(self):
        title_list=[]
        for i in range(len(self.search_file())):
            title_list.append(self.search_file()[i]['name'])
        return title_list

    def show_file_path(self):
        path_list=[]
        for i in range(len(self.search_file())):
            path_list.append(self.search_file()[i]['path'])
        return path_list

    def show_file_extention(self):
        extention_list=[]
        for i in range(len(self.search_file())):
            extention_content = self.show_file_title()[i].split('.')
            extention_list.append(extention_content[len(extention_content)-1])
        return extention_list



    def download_file(self,number):
        download_path = self.show_file_path()[number].replace('\\','/').replace(' ','%20')
        download_name = self.show_file_title()[number].replace(' ','%20')
        pan_routin = download_path.split(':')
        #download_name_split = download_name.split('.')
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ts = str(int(time.mktime(time.strptime(now_time, "%Y-%m-%d %H:%M:%S"))))
        pan_name =self.download_file_name + self.show_file_extention()[number]
        download_url = self.url + pan_routin[0]+'%3A'+pan_routin[1]+'/'+ download_name
        #print(download_url)
        #download_url2 = self.url + self.file_list[number]['path'].replace('\\','/')+ self.title_list[number]
        #print(download_url2)
        #download_params = {'j':'2',path_column':'2','date_modified_column':'2','date_created_column':'2'}
        download_file = requests.get(download_url,headers=self.headers)
        with open(pan_name, "wb") as code:
            code.write(download_file.content)








ss=Titlesearch("范围管理")
ss.download_file(5)



