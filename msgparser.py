#!/usr/bin/python
#    Copyright 2014 Ongmani
# We...Chat backend...
#
# Support:
#         newbthzz@163.com
#
# Description:
# used to parse message sent by subscriber....

#deps : python-lxml

import eventlet
import eventlet.wsgi
import routes
import routes.middleware
import webob.dec
import webob.exc
from lxml import etree
from lxml.etree import ElementTree as ET
from debug import dbg
from debug import __ver__

import inspect

def __func__():
    return inspect.stack()[1][3]


class MsgParser(object):
    def __init__(self):
      dbg.debug("<%s> in", __func__())
      dbg.debug("<%s> exit", __func__())

    def running(self, msg):
      '''
      parse :
       1. Text
       2. Picture
       3. Voice
       4. Video
       ...
      save to :
       1. console
       2. files
       3. db...
      '''
      dbg.debug("<%s> in", __func__())

      xmldoc = etree.fromstring(msg)
      msg_type = xmldoc.find('MsgType')
      if msg_type.text == 'text':
        self.text_get(xmldoc)
      else:
        dbg.debug("Not support format sent by Qi'e")

      dbg.debug("<%s> exit", __func__())

      return
      
    def text_get(self, xmldoc):
      '''
      <xml>
      <ToUserName><![CDATA[toUser]]></ToUserName>
      <FromUserName><![CDATA[fromUser]]></FromUserName> 
      <CreateTime>1348831860</CreateTime>
      <MsgType><![CDATA[text]]></MsgType>
      <Content><![CDATA[this is a test]]></Content>
      <MsgId>1234567890123456</MsgId>
      </xml>
      '''
      dbg.debug("<%s> in", __func__())
      dbg.debug("xmldoc: <%s>", xmldoc)

      to_username = xmldoc.find('ToUserName')
      from_username = xmldoc.find('FromUserName')
      create_time = xmldoc.find('CreateTime')
      text_content = xmldoc.find('Content')
      msg_id = xmldoc.find('MsgId')

      dbg.debug("to username: %s ", to_username.text)
      dbg.debug("from username: %s ", from_username.text)
      dbg.debug("create time: %s ", create_time.text)
      dbg.debug("text_content: %s ", text_content.text)
      dbg.debug("msg_id: %s ", msg_id.text)

      dbg.debug("<%s> exit", __func__())
     
      return 'text_get return'

    def print_node(node):
      '''Print Dom'''
      dbg.info("==============================================")
      if node.attrib:
        dbg.debug("node.attrib:%s" % node.attrib)
      if node.attrib.has_key("MsgId") > 0 :
        dbg.debug("node.attrib['MsgId']:%s" % node.attrib['MsgId'])
      dbg.debug("<%s>:<%s>" % (node.tag, node.text))

if __name__ == '__main__':
  dbg.debug("Ongmani.: <%s> . verion: <%s>", __name__, __ver__)
  sys.exit(main(sys.argv))
else:
  dbg.debug("Ongmani.: <%s> . verion: <%s>", __name__, __ver__)

