#!/usr/bin/python
# https://wiki.python.org/moin/BaseHttpServer
# https://www.djangoproject.com/
# http://www.linuxjournal.com/content/tech-tip-really-simple-http-server-python
# https://wiki.python.org/moin/WebProgramming
# https://hg.python.org/cpython/file/2.7/Lib/BaseHTTPServer.py
# https://docs.python.org/3/library/http.server.html
# https://docs.python.org/3/tutorial/modules.html
# The BaseHTTPServer module has been merged into http.server in Python 3.

import time
import http.server

HOST_NAME = "localhost"
PORT_NUMBER = "8082" #unpreseved unofficial port

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
