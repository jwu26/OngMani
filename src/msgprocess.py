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
from msgparser import MsgParser
from saveadapter import MsgSaverAdapter

class MsgProcess(object):
    def __init__(self, req, args):
      dbg.debug("in")
      dbg.debug("exit")
      self.method = req.method.lower()
      self.params=req.environ['wsgiorg.routing_args'][1]
      self.params_1=req.params.copy()
      self.params_sig=req.params.get('signature', '0')
      self.params_ts =req.params.get('timestamp', '0')
      self.params_nonce =req.params.get('nonce', '0')
      #params_echostr =req.params.get('echostr')
      self.params_echostr =req.params.get('echostr', 'helloW!')

      #local:
      content_type = req.headers['Content-Type']
      content_length = req.headers['Content-Length']

      dbg.info("content_type: <%s> Len<%s>, args.id: %s",content_type, content_length ,args['id'])
      if content_type == 'text/plain':
        return params_echostr

      if args['id'] != 'upload':
        dbg.error("Not Support Command by Qi'e")
        return params_echostr
      else:
        dbg.debug("Upload Support")

      self.host = req.headers['Host'] 
        
      if content_type != 'text/xml':
        dbg.error("Only support xml format! <%s>", content_type)
        return 
      else:
        dbg.debug("Xml is appreicated!")
        
      
    def running(self, req, args):
      '''
      parse :
      save to :
      ack :
      '''
      dbg.debug("in")

      xmldoc = etree.fromstring(req.body)

      parser = MsgParser()
      parser.running(req.body)

      store=MsgSaverAdapter()
      store.running(parser.data)
      
      #print "req is %s\n" % req
      dbg.debug("req.body is %s",req.body)
      '''
      dbg.debug("headers is %s" , req.headers)
      dbg.debug("host is %s" , self.host)
      dbg.debug("params is %s" , self.params)
      dbg.debug("req.params is %s" , req.params)
      dbg.debug("params_1 is %s" , self.params_1)
      dbg.debug("params_sig is %s" , self.params_sig)
      dbg.debug("params_ts is %s" , self.params_ts)
      dbg.debug("params_nonce is %s" , self.params_nonce)
      dbg.debug("params_echostr is %s" , self.params_echostr)
      dbg.debug("method is %s" , self.method )
      '''

      dbg.debug("Exit")
      return self.params_echostr


if __name__ == '__main__':
  dbg.debug("Ongmani.: <%s> . verion: <%s>", __name__, __ver__)
  sys.exit(main(sys.argv))
else:
  dbg.debug("Ongmani.: <%s> . verion: <%s>", __name__, __ver__)

