#coding=utf8
import requests
import itchat, time
from itchat.content import *
import sys
sys.path.append('')
from core.SearchEngine.Title_Search import Titlesearch





@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    msg.user.send('%s: %s' % (msg.type, msg.text))

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text))



sss=Titlesearch("质量管理")

@itchat.msg_register(TEXT,ATTACHMENT)
def goto_go(msg):
    msg.user.send("@fil@%s" % "181031-223731.png")
    #return "@fil@%s" % '新建文本文档.txt'


itchat.auto_login(True)
itchat.send_file(sss.download_file(2))
itchat.send_file("/tmp/test.txt")
itchat.run(True)