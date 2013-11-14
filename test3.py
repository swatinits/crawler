from twisted.internet import reactor
from scrapy.crawler import Crawler
#from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings
from scrapy import log, signals
from dirbot.spiders.dmoz3 import DmozSpider3
from scrapy.xlib.pydispatch import dispatcher

def stop_reactor():
    reactor.stop()

def call_spider(start_urls):
  dispatcher.connect(stop_reactor, signal=signals.spider_closed)
  spider = DmozSpider3(start_url=start_urls)
  #crawler = Crawler(Settings())
  crawler = Crawler(get_project_settings())
  crawler.install()
  crawler.configure()
  crawler.crawl(spider)
  crawler.start()
  log.start(logfile="debug.log", loglevel=log.DEBUG, crawler=crawler, logstdout=False)
  log.msg("------------>Running reactor")
  result = reactor.run()
  #print result
  log.msg("------------>Running stoped")

def main():
  start_urls="http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"
  call_spider(start_urls)
  return

if __name__ == '__main__':
  main()


