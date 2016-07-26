#!/usr/bin/python
import msvcrt
import time
from server import core
import threading

try:
    # https://docs.python.org/3.5/library/__main__.html
    if __name__ == "__main__":
        server = core.start_async("localhost", 8082)

        print("\nMain thread name is: %s\n" % (threading.current_thread().name))
        print("Click any key to abort the server.")
        msvcrt.getch()
        # server.stop() continue from here!
    pass
except:
    raise Exception("main thread exception!")
