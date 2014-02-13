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
  
class MsgSaverAdapter(object):
    def __init__(self):
      dbg.debug("<%s> in", __func__())
      dbg.debug("<%s> exit", __func__())

    def running(self, msg, adapter):
      '''
      save to :
       1. console
       2. files
       3. db...
      '''
      dbg.debug("<%s> in", __func__())

      if adapter == 'file':
        saveToFiles(msg):
        dbg.debug("Sucess")
      else:
        dbg.debug("Not Support")

      dbg.debug("<%s> exit", __func__())

      return
      
    def saveToConsole(self, msg):
      '''
      print on Console
      '''
      dbg.debug("<%s> in", __func__())
      dbg.debug("<%s> exit", __func__())
     
      return 

    def saveToFiles(self, msg):
      dbg.debug("<%s> in", __func__())
      dbg.debug("<%s> exit", __func__())
      return 

    def saveToDB(self, msg):
      dbg.debug("<%s> in", __func__())
      dbg.debug("<%s> exit", __func__())
      return 

if __name__ == '__main__':
  dbg.debug("Ongmani.: <%s> . verion: <%s>", __name__, __ver__)
  sys.exit(main(sys.argv))
else:
  dbg.debug("Ongmani.: <%s> . verion: <%s>", __name__, __ver__)
