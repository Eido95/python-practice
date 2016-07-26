#!/usr/bin/python
# https://wiki.python.org/moin/BaseHttpServer
# https://www.djangoproject.com/
# http://www.linuxjournal.com/content/tech-tip-really-simple-http-server-python
# https://wiki.python.org/moin/WebProgramming
# https://hg.python.org/cpython/file/2.7/Lib/BaseHTTPServer.py
# https://docs.python.org/3/library/http.server.html
# https://docs.python.org/3/tutorial/modules.html
# https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3/
## The BaseHTTPServer module has been merged into http.server in Python 3.
# http_URL = "http:" "//" host [ ":" port ] [ abs_path [ "?" query ]]

__version__ = "0.1"

import time
from http import server, HTTPStatus
from socketserver import ThreadingMixIn
import threading

HOST_NAME = "localhost"
PORT_NUMBER = "8082" #unpreseved unofficial port

class EidoHTTPRequestHandler(server.BaseHTTPRequestHandler):
    """This class is used to handle the HTTP requests that arrive at the server."""
    # def __init__(self):
    #     """Called after the instance has been created (by __new__()), but before it is returned to the caller."""
    #     #super().__init__ # super() is useful for accessing inherited methods that have been overridden in a class.
    server_version = "EidoHTTP/" + __version__
    protocol_version = "HTTP/1.1" #https://tools.ietf.org/html/rfc2616

    # The handler will parse the request and the headers, then call a method specific to the request type. The method name is constructed from the request. For example, for the request method POST, the do_POST() method will be called with no arguments.
    def do_GET(self):
        try:
            """
            Serve a GET request - client requests data from the server.
            The GET method means retrieve whatever information (in the form of an entity) is identified by the Request-URI (identifies the resource upon which to apply the request).
            """
            # TODO:0 analyze self.path (request path) which indicates the absoluteURI (abs_path) https://tools.ietf.org/html/rfc2616#section-5.1.2
            self.send_response(HTTPStatus.OK) # Status code OK - Successful class (https://tools.ietf.org/html/rfc2616#section-10.2.1)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.append_message_body("Welcome to my server! your path is %s" % (self.path),"utf-8")
            #print(self.path)
            #print("My path is %s" (self.path))
            # self.end_headers(); # an empty line (i.e., a line with nothing preceding the CRLF) indicating the end of the header fields, and possibly a message-body.
            # An entity corresponding to the requested resource should be sent in the response;
        except:
            server_thread.shutdown()
            server_thread.close()
            raise Exception("wtf!")

    def do_POST(self):
        # client submits data to to the server to be proccessed.
        pass

    def append_message_body(self, message, encoding):
        self.wfile.write(bytes(message, encoding))
        pass

class AsyncHTTPServer(ThreadingMixIn, server.HTTPServer):
    """
    This class is used to create an asynchronous HTTP server.
    """
    # https://docs.python.org/3.5/library/socketserver.html#asynchronous-mixins
    # http://www.openbookproject.net/books/bpp4awd/index.html
    daemon_threads = False;
    pass

def start_async(host_name, port_number):
    """
    Starts an asynchronous HTTP server daemon. use .stop() to stop it.
    """
    # Tuple sequence type
    server_address = (host_name, port_number)
    # daemon - https://en.wikipedia.org/wiki/Httpd
    # synchronous version is server.HTTPServer(server_address, EidoHTTPRequestHandler)
    async_daemon = AsyncHTTPServer(server_address, EidoHTTPRequestHandler)
    # Start a thread with the server -- that thread will then start one more thread for each request
    server_thread = threading.Thread(target=async_daemon.serve_forever, name="Thread-1-server_main")
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)
    #async_daemon.serve_forever(poll_interval=0.5)
    return async_daemon

def stop():
    if server_thread is not None:
        server_thread.shutdown()
        server_thread.close()

# class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
#     def do_head(s):
#         s.send_response(200); # Sends a response header and logs the accepted request. The HTTP response line is sent, followed by Server and Date headers. The values for these two headers are picked up from the version_string() and date_time_string() methods, respectively.
#         s.send_header("Content-type", "text/html") # Writes a specific HTTP header to the output stream. keyword should specify the header keyword, with value specifying its value.
#         s.end_headers(); # Sends a blank line, indicating the end of the HTTP headers in the response.
#
#     def do_get(s):
#         """Respond to GET request."""
#         s.send_response(200)
#         s.send_header("Content-type", "text/html")
#         s.end_headers()
#         s.wfile.write("""\
#         <html>
#             <head>
#                 <title>Welcome!</title>
#             </head>""")
#         s.wfile.write("<body><p>This is my paragraph</p>")
#         s.wfile.write("<p>You accessed path: %s</p>" % (s.path))
