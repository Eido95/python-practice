#!/usr/bin/python
from server import core

try:
    # https://docs.python.org/3.5/library/__main__.html
    if __name__ == "__main__":
        server = core.start_async("localhost", 8082)
        #threading.Thread(target=core.start("localhost",8082), name="Thread-1-server").start()
        #message = "\n%s\n" % __name__
        print("%s" % (__name__))
        print("\nMain thread name is: %s\n" % (threading.current_thread().name))
    pass
except Exception as exception:
    raise exception
