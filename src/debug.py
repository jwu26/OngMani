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
import logging

def __func__():
    return inspect.stack()[1][3]
 
dbg = logging.getLogger(__name__)
# Enable Debug
#logging.basicConfig(level=logging.ERROR, 
#logging.basicConfig(level=logging.NOTSET, 
logging.basicConfig(level=logging.DEBUG, 
      format='%(asctime)s %(filename)s[%(funcName)s] %(levelname)s %(message)s',
      datefmt='%Y %b %d:')
#format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
#logging.basicConfig(level=logging.INFO)

import inspect


__ver__=0.1

if __name__ == '__main__':
  dbg.debug("Ongmani.: <%s> . verion: <%s>", __name__, __ver__)
  sys.exit(main(sys.argv))
else:
  dbg.debug("Ongmani.: <%s> . verion: <%s>", __name__, __ver__)

