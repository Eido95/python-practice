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
from http import server

HOST_NAME = "localhost"
PORT_NUMBER = "8082" #unpreseved unofficial port

class EidoHTTPRequestHandler(server.BaseHTTPRequestHandler):
    """This class is used to handle the HTTP requests that arrive at the server."""
    def __init__(self):
        """Called after the instance has been created (by __new__()), but before it is returned to the caller."""
        super().__init__ # This is useful for accessing inherited methods that have been overridden in a class.
        self.server_version = "EidoHTTP/" + __version__
        self.protocol_version = "HTTP/1.1" #https://tools.ietf.org/html/rfc2616

    # The handler will parse the request and the headers, then call a method specific to the request type. The method name is constructed from the request. For example, for the request method POST, the do_POST() method will be called with no arguments.
    def do_GET(self):
        """
        Serve a GET request - client requests data from the server.
        The GET method means retrieve whatever information (in the form of an entity) is identified by the Request-URI (identifies the resource upon which to apply the request).
        """
        self.send_response(200) # Status code OK - Successful class
        # An entity corresponding to the requested resource should be sent in the response;
        # Continue with the following tabs:
        # https://tools.ietf.org/html/rfc2616
        # http://www.w3schools.com/tags/ref_httpmethods.asp
        # https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3/
        # https://www.python.org/dev/peps/pep-0008/
        # https://docs.python.org/3.5/
        # https://docs.python.org/3.5/tutorial/
        # https://docs.python.org/3/library/http.server.html


    def do_POST(self):
        # client submits data to to the server to be proccessed.

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

print("I'm a python server!")
