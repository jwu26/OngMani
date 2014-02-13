#!/usr/bin/python
# We...Chat backend fo balabalabala

#deps : python-lxml

import eventlet
import eventlet.wsgi
import routes
import routes.middleware
import webob.dec
import webob.exc
from lxml import etree
from lxml.etree import ElementTree as ET
import logging

_log = logging.getLogger(__name__)
# Enable Debug
logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.INFO)

import inspect

def __func__():
    return inspect.stack()[1][3]

_ver=0.1

class msgparser(object):
    def __init__(self):
      _log.debug("<%s> in\n", __func__())
    def text_get:
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
      _log.debug("<%s> in\n", __func__())
    return

    def print_node(node):
    '''Print Dom'''
      print "=============================================="
      if node.attrib:
        _log.debug("node.attrib:%s" % node.attrib)
      if node.attrib.has_key("MsgId") > 0 :
        _log.debug("node.attrib['MsgId']:%s" % node.attrib['MsgId'])
      _log.debug("<%s>:<%s>.\n" % (node.tag, node.text))

if __name__ == '__main__':
  _log.debug("Ongmani: <messageparser> \n")
  sys.exit(main(sys.argv))
else:
  _log.debug("Ongmani: <messageparser> %d\n" % _ver_)

