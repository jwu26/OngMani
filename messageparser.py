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

def print_node(node):
    '''Print Dom'''
    print "=============================================="
    if node.attrib:
      print "node.attrib:%s" % node.attrib
    if node.attrib.has_key("MsgId") > 0 :
      print "node.attrib['MsgId']:%s" % node.attrib['MsgId']
    print "node.tag:%s" % node.tag
    print "node.text:%s" % node.text

class MessagePaser(object):
    def __init__:
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
        print "req is %s\n" % req
        return 'two'

    @wsgify_args
    def three(self, req, args):
        print "req is %s\n" % req
        print "args is %s\n" % args
        return 'three'

    @wsgify_args
    def upload(self, req, args):
        method = req.method.lower()
        params=req.environ['wsgiorg.routing_args'][1]
        params_1=req.params.copy()
        params_sig=req.params.get('signature', '0')
        params_ts =req.params.get('timestamp', '0')
        params_nonce =req.params.get('nonce', '0')
        params_echostr =req.params.get('echostr', '0')
        content_type = req.headers['Content-Type']
        content_length = req.headers['Content-Length']
        host = req.headers['Host'] 
        
        if content_type != 'text/xml':
          print "Only support xml format! <%s>" % content_type
          return 
        else:
          print "Xml is appreicated!"
        
        xmldoc = etree.fromstring(req.body)
        to_username = xmldoc.find('ToUserName')
        text_content = xmldoc.find('Content')
        msg_type = xmldoc.find('MsgType')
        print_node(text_content)
        print "xmldoc is %s\n" % xmldoc
        print "to useranem is %s\n" % to_username.text
        print "text is %s\n" % text_content.text
        print "msg type is %s\n" % msg_type.text

        print "req is %s\n" % req
        print "req.body is %s\n" % req.body
        print "headers is %s\n" % req.headers
        print "headers.type is %s\n" % content_type
        print "headers.length is %s\n" % content_length
        print "host is %s\n" % host
        print "params is %s\n" % params
        print "req.params is %s\n" % req.params
        print "params_1 is %s\n" % params_1
        print "params_sig is %s\n" % params_sig
        print "params_ts is %s\n" % params_ts
        print "params_nonce is %s\n" % params_nonce
        print "params_echostr is %s\n" % params_echostr
        print "method is %s\n" % method 
        print "args.id is %s\n" % args['id']
        print "args is %s\n" % args
        if args['id'] == '1':
          print "it's Text Uploading\n"
        else:
          print "Not supported\n"
        #return 'uploaded!'
        return params_echostr


sock = eventlet.listen(('119.84.78.194', 80))
#sock = eventlet.listen(('', 12345))
map = routes.Mapper()
map.connect('/v1.0/{action}/{id}', controller=API())
eventlet.wsgi.server(sock, routes.middleware.RoutesMiddleware(ParsedRoutes(webob.exc.HTTPNotFound()), map))
