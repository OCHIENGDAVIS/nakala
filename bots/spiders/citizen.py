
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from pyquery import PyQuery as pq
from ..items import CitizenArticleItem


class Citizen(CrawlSpider):
    name = 'citizen'
    allowed_domains = ['citizentv.co.ke']
    start_urls = ['https://citizentv.co.ke/']
    rules = [
        Rule(LinkExtractor(deny='https://citizentv.co.ke/archives.*', allow='.*'), callback='parse_items', follow=True)
    ]

    def parse_items(self, response):
        q = pq(response.text)
        q('.votd-title').remove()
        q('.votd-content-title').remove()
        q('.mid-content-also-read').remove()
        title = q('h1.articleh1').text()
        if title is None:
            return
        author = q('.main-post-author').text()
        if author is None:
            return
        published_on = q('.date-tag').text()
        if published_on is None:
            return
        body = q('.parallax-container p').text()
        if body is None:
            return
        item = CitizenArticleItem()
        item['title'] = title
        item['author'] = author
        item['published_on'] = published_on
        item['body'] = body
        yield item
