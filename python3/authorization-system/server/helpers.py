#!/usr/bin/python

def are_headers_legal(headers):
    """
    Verify whether the headers contains legal values which the server can handle and serve by.
    """
    result = None
    for headerName, headerValue in headers.items():
        if headerName == "Content-Type":
            if headerValue != "text/html":
                result = headerValue
                break
        elif headerName == "Host":
            if headerValue != "localhost:8082":
                result = headerValue
                break
        elif headerName == "Accept":
            if "text/html" not in headerValue:
                result = headerValue
                break
