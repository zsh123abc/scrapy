from io import BytesIO
import scrapy

import os,stat
from urllib import request

from ..items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'

    # allowed_domains = ['https://tide.fm/sounds/']

    start_urls = ["https://tide.fm/sounds"]


    def parse(self, response):
        # 拿到 section 下的所有 div
        node_list = response.xpath("//section[@class='scenes']/div")
    
        for node in node_list:
            # 创建item对象，用来储存信息
            item = ItcastItem()
            # extract()[0]把第1项数据取出来，总共一项，取出来就可以去除[]括号
            url = node.xpath("a/@href").extract()[0]
            item["url"] = self.start_urls[0] + url
            
            
            title = node.xpath("a/div/span/text()").extract()[0]
            item["title"] = title
            
            pic_url = node.xpath("a/div/div/img/@data-srcset").extract()[0]
            str_pic_url = ''
            for p in pic_url:
                if p == ' ':
                    break
                else :
                    str_pic_url = str_pic_url+p
            item["pic_url"] = str_pic_url   

            yield scrapy.Request(
                item["url"],
                callback=self.parse_audio,
                meta={"item": item}
            )



    def parse_audio(self,response):
        
        item = response.meta["item"]
        
        audio = response.xpath("//*[@id='__layout']/div/div[1]/div[1]/div/div[2]/div[1]/audio")
        audio_src = audio.xpath("@src").extract()[0]
        item["audio_src"] = audio_src

        yield item
            
