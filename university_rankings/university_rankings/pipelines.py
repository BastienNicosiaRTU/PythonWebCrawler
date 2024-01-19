# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class UniversityRankingsPipeline:
    def open_spider(self, spider):
        self.file = open('university_rankings.txt', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = f"{item['rank']}, {item['university_name']}\n"
        self.file.write(line)
        return item

