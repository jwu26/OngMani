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
  
class FileFactory(object):
    def __init__(self):
      dbg.debug("in")
      self.file='/tmp/log.xml'
      dbg.debug("exit")

    def open(self):
      dbg.debug("Open file: %s", self.file)
      return

    def write(self, data):
      dbg.debug("Write file: %s", self.file)
      return
 
    def close(self):
      dbg.debug("Close file: %s", self.file)
      return

      
 
