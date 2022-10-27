import json
from ..items import ScrapyJsonItem
import scrapy


class JsonSpiderSpider(scrapy.Spider):
    # 爬虫名
    name = 'json_spider'

    # 限制范围
    # allowed_domains = ['json_spider.cn']

    # 起始位置
    start_urls = ['https://tide.fm/api/v2/web/explorer/scene_pages/all?tag=&offset=0&limit=512']

    url = ['https://tide.fm/api/v2/web/explorer/scene_pages/all?tag=&offset=0&limit=512',
    "https://tide.fm/api/v2/web/explorer/scene_pages/all?tag=Video&offset=0&limit=512",
    "https://tide.fm/api/v2/web/explorer/scene_pages/all?tag=Free&offset=0&limit=512",
    "https://tide.fm/api/v2/web/explorer/scene_pages/all?tag=Melody&offset=0&limit=512",
    "https://tide.fm/api/v2/web/explorer/scene_pages/all?tag=Nature&offset=0&limit=512",
    "https://tide.fm/api/v2/web/explorer/scene_pages/all?tag=Modern&offset=0&limit=512",
    "https://tide.fm/api/v2/web/explorer/scene_pages/all?tag=Meditation&offset=0&limit=512",
    "https://tide.fm/api/v2/web/explorer/scene_pages/all?tag=Sleep&offset=0&limit=512",
    "https://tide.fm/api/v2/web/explorer/scene_pages/all?tag=Focus&offset=0&limit=512",
    'https://tide.fm/api/v2/web/explorer/scene_pages/all?tag=Relax&offset=0&limit=512']

    def parse(self, response):
        pageData = json.loads(response.text)
        for node in pageData["scenes"]:

            item = ScrapyJsonItem()
            # # 标题
            img_name = node["name"]
            item["title"] = img_name["zh-Hans"] 
             
            # # 音频  
            # audio_src = node["resource"]
            # item["audio"] = audio_src["demo_sound_url"]   

            # 图片
            # item["img"] = node["image"]

            item['video'] = node["video_cover_demo_url"]

            yield item
                       
        if self.url is not None:
            index = 0
            index = index + 1
            next_url = self.url[index]    
            yield scrapy.Request(next_url, callback= self.parse)
        
        