from scrapy.cmdline import execute
import os
import sys

if __name__ == '__main__':
    #sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
    ffpath = os.path.abspath(os.path.join(fpath,".."))
    sys.path.append(ffpath)
    execute(['scrapy','crawl','itcast'])