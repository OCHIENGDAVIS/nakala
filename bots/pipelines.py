# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from dateutil.parser import parse
from scrapy.exceptions import DropItem
from citizen.models import CitizenModel


class BotsPipeline:
    def process_item(self, item, spider):
        return item


class CitizenPipeline(object):

    def process_item(self, item, spider):
        link = item['image_urls'][0]
        image_properties = item['images']
        into_json = image_properties[0]
        path = into_json.get('path')
        checksum = into_json.get('checksum')
        status = into_json.get('status')
        item['image_urls'] = link
        item['path'] = path
        item['checksum'] = checksum
        item['status'] = status
        return item


class SaveCitizenCitizenPipeline(object):

    def process_item(self, item, spider):
        title = item['title']
        url = item['url']
        qs = CitizenModel.objects.filter(title__iexact=title)
        if qs.exists():
            print('article already exists .....')
            DropItem('Item Already Exists......')
        url_exists = CitizenModel.objects.filter(url__iexact=url)
        if url_exists.exists():
            print('Article already exists')
            DropItem('Item Already Exists......')
        date_raw = item['published_on']
        date_temp = date_raw.replace('(', '')
        date_clean = date_temp.replace(')', '')
        published_date = parse(date_clean)
        item['order_by'] = published_date
        return item


class DublicateCitizenCitizenPipeline(object):

    def process_item(self, item, spider):
        author = item['author']
        qs = CitizenModel.objects.filter(author__iexact=author)
        if qs.exists():
            DropItem('Item Already Exists.......')
        item.save()
        return item
