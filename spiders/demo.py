# -*- coding: utf-8 -*-
"""
Created on 2024-03-25 00:00:31
---------
@summary:
---------
@author: cainiao
"""

import feapder

from items.item import DemoDataItem


class Demo(feapder.AirSpider):
    def start_requests(self):
        yield feapder.Request("https://spidertools.cn")

    def parse(self, request, response):
        # 提取网站title
        print(response.xpath("//title/text()").extract_first())
        # 提取网站描述
        print(response.xpath("//meta[@name='description']/@content").extract_first())
        print("网站地址: ", response.url)
        item = DemoDataItem()
        item.url = response.url
        item.update_key = response.url
        yield item


if __name__ == "__main__":
    Demo().start()