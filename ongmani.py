#!/usr/bin/python
#    Copyright 2014 Ongmani
# We...Chat backend...
#
# Support:
#         newbthzz@163.com
#
# Description:
#

#deps : python-lxml

import eventlet
import eventlet.wsgi
import routes
import routes.middleware
import webob.dec
import webob.exc
from lxml import etree
from lxml.etree import ElementTree as ET
from msgparser import MsgParser
from debug import dbg
from debug import __ver__

def wsgify_args(application):
    @webob.dec.wsgify
    def wrapper(self, req):
        return application(self, req, req.environ['wsgiorg.routing_args'][1])
    return wrapper

class Application(object):
    def __call__(self, environ, start_response):
        raise NotImplementedError("You must implement __call__")

class Middleware(Application):
    def __init__(self, application):
        self.application = application

class ParsedRoutes(Middleware):
    def __call__(self, environ, start_response):
        if environ['routes.route'] is None:
            return self.application(environ, start_response)

        # If controller was not specified, call default application.
        controller = environ['wsgiorg.routing_args'][1]['controller']
        if controller is None:
            return self.application(environ, start_response)

        # If action was not specified, call controller.
        action = environ['wsgiorg.routing_args'][1]['action']
        if action is None:
            return controller(environ, start_response)

        # Call method matching action, or controller if one doesn't exist.
        method = getattr(controller, action, controller)
        return method(environ, start_response)

class API(Application):
    def hello(self, environ, start_response):
        start_response("200 Ok", [('Content-Type', 'text/plain')])
        #start_response("200 Ok", [])
        return 'Hey , Sweet!!'

    @webob.dec.wsgify
    def two(self, req):
        dbg.info("req is %s", req)
        return 'two'

    @wsgify_args
    def three(self, req, args):
        dbg.info("req is %s", req)
        return 'three'

    @wsgify_args
    def ongmani(self, req, args):
        method = req.method.lower()
        params=req.environ['wsgiorg.routing_args'][1]
        params_1=req.params.copy()
        params_sig=req.params.get('signature', '0')
        params_ts =req.params.get('timestamp', '0')
        params_nonce =req.params.get('nonce', '0')
        #params_echostr =req.params.get('echostr')
        params_echostr =req.params.get('echostr', 'helloW!')
        content_type = req.headers['Content-Type']

        dbg.info("content_type: %s, args.id: %s",content_type, args['id'])
        if content_type == 'text/plain':
          return params_echostr

        if args['id'] != 'upload':
          dbg.error("Not Support Command by Qi'e")
          return params_echostr
        else:
          dbg.debug("Upload Support")

        content_length = req.headers['Content-Length']
        host = req.headers['Host'] 
        
        if content_type != 'text/xml':
          dbg.error("Only support xml format! <%s>", content_type)
          return 
        else:
          dbg.debug("Xml is appreicated!")
        
        xmldoc = etree.fromstring(req.body)

        parser = MsgParser()
        parser.running(req.body)

        #print "req is %s\n" % req
        dbg.debug("req.body is %s",req.body)
        dbg.debug("headers is %s" , req.headers)
        dbg.debug("headers.type is %s", content_type)
        dbg.debug("headers.length is %s" ,content_length)
        dbg.debug("host is %s" , host)
        dbg.debug("params is %s" , params)
        dbg.debug("req.params is %s" , req.params)
        dbg.debug("params_1 is %s" , params_1)
        dbg.debug("params_sig is %s" , params_sig)
        dbg.debug("params_ts is %s" , params_ts)
        dbg.debug("params_nonce is %s" , params_nonce)
        dbg.debug("params_echostr is %s" , params_echostr)
        dbg.debug("method is %s" , method )
        dbg.debug("args.id is %s" , args['id'])
        dbg.debug("args is %s" , args)
        #return 'uploaded!')

        return params_echostr


if __name__ == '__main__':
  dbg.debug("Weclome!")
  sock = eventlet.listen(('119.84.78.194', 80))
  #sock = eventlet.listen(('', 12345))
  map = routes.Mapper()
  map.connect('/v1.0/{action}/{id}', controller=API())
  eventlet.wsgi.server(sock, routes.middleware.RoutesMiddleware(ParsedRoutes(webob.exc.HTTPNotFound()), map))
