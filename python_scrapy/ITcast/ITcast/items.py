# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from email.mime import audio
from turtle import title
import scrapy


class ItcastItem(scrapy.Item):
    # define the fields for your item here like:

    # 下一层链接
    url = scrapy.Field()

     # 名字
    title = scrapy.Field()

    # 图片
    pic_url = scrapy.Field()

    #音频
    audio_src = scrapy.Field()

