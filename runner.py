import os
import threading
def startCrawler(): 
    os.system('scrapy crawl citizen')

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

set_interval(startCrawler, 10)
