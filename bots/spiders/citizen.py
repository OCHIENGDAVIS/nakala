import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class Citizen(CrawlSpider):
    name = 'citizen'
    allowed_domains = ['citizentv.co.ke']
    start_urls = ['https://citizentv.co.ke/']
    rules = [
        Rule(LinkExtractor(deny='https://citizentv.co.ke/archives.*', allow='.*'), callback='parse_items', follow=True)
    ]

    def parse_items(self, response):
      
        main_story = response.css('div.articlestory')
      
        title = main_story.css('h1.articleh1::text').extract()[0]
        author = main_story.css('section.main-post-author').css('a::text').extract()[0]
        published_on = main_story.css('span.date-tag::text').extract()[0]
        image = main_story.css('figure.images-section').css('img').xpath('@src').get()
        summary = main_story.css('div.summary').css('li::text').extract()
        content = main_story.css('div.parallax-container').css('p::text').extract()[0]
        return {
            "title" : title,
            "author": author,
            "published_on": published_on,
            "image": image,
            "summary": summary,
            "content": content
        }
      
