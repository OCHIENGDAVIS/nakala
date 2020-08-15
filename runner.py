# import os
# import threading
# def startCrawler():
#     os.system('scrapy crawl citizen')
#
# def set_interval(func, sec):
#     def func_wrapper():
#         set_interval(func, sec)
#         func()
#     t = threading.Timer(sec, func_wrapper)
#     t.start()
#     return t
#
# set_interval(startCrawler, 3)


# RUNNING SPIDERS A DIFERENT WAY
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())
process.crawl('citizen', domain='citizentv.co.ke')
process.start()
