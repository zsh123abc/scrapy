# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os,stat
from urllib import request

class ScrapyJsonPipeline:
    def process_item(self, item, spider):

        title = item["title"]
        # audio = item["audio"]
        # img = item["img"]

        # white_src = "https://scpic.chinaz.net/files/pic/pic9/201601/apic18482.jpg "
        # if title == '蓝色星球':
        #     # 下载图片
        #     request.urlretrieve(white_src,"D:\zsh\python\scrapy_json\json_scarpy_img\%s.jpg"%title)  
        # else:
        #     request.urlretrieve(img,"D:\zsh\python\scrapy_json\json_scarpy_img\%s.jpg"%title)  

        # # 下载音频
        # request.urlretrieve(audio,"D:\zsh\python\scrapy_json\json_scarpy_audio\%s.MP3"%title)

        # 下载视频
        video = item["video"]
        request.urlretrieve(video,"D:\zsh\python\scrapy_json\json_scarpy_video\%s.MP4"%title)  

        return item
