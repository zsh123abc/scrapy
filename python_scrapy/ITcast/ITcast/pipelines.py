# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from email.mime import audio
from shlex import split
import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import os,stat
from urllib import request


class ItcastPipeline:

    def __init__(self):
        self.txt_file = open('data.txt', 'w', encoding='utf-8')
    
    # 存储文件数据
    def process_item(self, item, spider):
        url = item['url']
        title = item['title']
        pic_url = item['pic_url']
        audio_src = item['audio_src']


        white_src = "https://scpic.chinaz.net/files/pic/pic9/201601/apic18482.jpg "
        if title == '蓝色星球':
            # 下载图片
            request.urlretrieve(white_src,"d:\img\%s.jpg"%title)  
        else:
            request.urlretrieve(pic_url,"d:\img\%s.jpg"%title)  

        # 下载音频
        request.urlretrieve(audio_src,"d:\src_audio\%s.MP3"%title)

        self.txt_file.write(str(url) + '\n' + title + '\n' + pic_url + '\n'+ audio_src +'\n\n')
        return item

        			   			
              
    def close_spider(self, spider):
        self.txt_file.close()

    