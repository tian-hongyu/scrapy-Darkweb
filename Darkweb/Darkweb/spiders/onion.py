# -*- coding: utf-8 -*-
import scrapy
from Darkweb.items import DarkwebItem


class OnionSpider(scrapy.Spider):
    name = 'onion'
    allowed_domains = ['http://jamiewebgbelqfno.onion/']
    start_urls = ['http://jamiewebgbelqfno.onion']

    def parse(self, response):
        it = DarkwebItem()
        url_str = '/html/body/nav/div/ul/li[3]/div/h4/a[{}]/text()'
        for i in range(1,33):
            it["title"] = response.xpath(url_str.format(i)).extract_first()
            yield it

