# -*- coding: utf-8 -*-
import scrapy
from spongebob.items import SpongebobItem


class ExampleSpider(scrapy.Spider):
    name = 'spongebob_me_boy'

    start_urls = ['https://spongebob.fandom.com/wiki/Category:Episode_transcripts?from=The+Grill+is+Gone%2Ftranscript']

    def next_page(self, response):
        for href in response.xpath("//a[cotains(@class, 'category-page__pagination-next')//@href"):
            url = href.extract()
            yield scrapy.Request(url, callback=self.parse)


    def parse(self, response):
        print("yeet")
        for href in response.xpath("//a[contains(@class, 'category-page__member-link')]//@href"):
            print(href)# add the scheme, eg http://
            url  = "https://spongebob.fandom.com/" + href.extract()
            yield scrapy.Request(url, callback=self.parse_dir_contents)


    def parse_dir_contents(self, response):
    	item = SpongebobItem()

    	item['transcript'] = response.xpath("//div[contains(@class, 'mw-content-text')]//li//text()").extract()

    	yield item