import time
import sys
import os
import asyncio
import django
import schedule
from asgiref.sync import sync_to_async
from crochet import setup
setup()
from pathlib import Path
# DJANGO_DIR = Path(Path(__file__).resolve(strict=True))

# sys.path.append(DJANGO_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'newsnet.settings'
django.setup()
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from bots.spiders.citizen import Citizen


configure_logging()
runner = CrawlerRunner(get_project_settings())

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(Citizen)
    # yield runner.crawl(MySpider2)
    # reactor.stop()


def start_crawl():
    crawl()
    # reactor.run()


# SHEDULING THE CRAWLER EVERY 30 MINUTES
schedule.every(2).minutes.do(start_crawl)


# @sync_to_async
# def run():
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

import asyncio
import threading


def worker():
    second_loop = asyncio.new_event_loop()
    while True:
        schedule.run_pending()
        time.sleep(1)
    return

threads = []
t = threading.Thread(target=worker)
threads.append(t)
t.start()

loop = asyncio.get_event_loop()
# execute_proxy_coroutines_forever(loop)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
