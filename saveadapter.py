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
from filefactory import FileFactory 
  
class MsgSaverAdapter(object):
    def __init__(self):
      dbg.debug("in")
      dbg.debug("exit")
      self.config = {'file':'1'}

    def saveToConsole(self, data):
      '''
      print on Console
      '''
      dbg.debug("in")
      dbg.debug("exit")
     
      return 

    def saveToFiles(self, data):
      dbg.debug("in")

      file=FileFactory()
      file.write(data)
      file.close

      dbg.debug("exit")
      return 

    def saveToDB(self, data):
      dbg.debug("in")
      dbg.debug("exit")
      return 

    def running(self, data):
      '''
      save to :
       1. console
       2. files
       3. db...
      '''
      dbg.debug("in")

      if data.has_key('text'):
        dbg.debug("Got a text to saving")
      elif data.has_key('picture'):
        dbg.debug("Got a picture to saving")
      else:
        dbg.debug("Not support format!!")
        return

      if self.config.has_key('file'):
        saveToFiles(data)
        dbg.debug("Sucess")

      if self.config.has_key('console'):
        printToConsole(data)
        dbg.debug("Sucess")

      if self.config.has_key('db'):
        dbg.debug("Not Support")

      dbg.debug("exit")

      return
      
if __name__ == '__main__':
  dbg.debug("Ongmani.: <%s> . verion: <%s>", __name__, __ver__)
  sys.exit(main(sys.argv))
else:
  dbg.debug("Ongmani.: <%s> . verion: <%s>", __name__, __ver__)
