# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


class BotsPipeline:
    def process_item(self, item, spider):

        return item


class CitizenPipeline(object):

    def process_item(self, item, spider):

        print('ITEM FROM FIRST PIPELINE....', item)
        return item


class SaveCitizenCitizenPipeline(object):

    def process_item(self, item, spider):

        print('FROM SECOND PIPELINE', item)
        item.save()
        return item
