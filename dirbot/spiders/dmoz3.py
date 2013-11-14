from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class DmozSpider3(CrawlSpider):
    name="dmoz3"    
    allowed_domains = ["dmoz.org"]
    rules=(Rule(SgmlLinkExtractor(allow = ()),follow=True,callback ='parse_item'),)
    body_list=[]

    def __init__(self, *a,**kwargs):
        super(DmozSpider3, self).__init__(*a,**kwargs)
        self.start_urls+=kwargs.get('start_url').split(',')
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def parse_item(self, response):       
        hxs = HtmlXPathSelector(response)
        sites = hxs.select("//body").extract()
        self.body_list.append(sites[0])
        print "length: ", len(self.body_list)
        return

    def spider_closed(self):
        f = open('lists.log','a')
        print "writing data"
	f.writelines(str(["%s\n" % item  for item in self.body_list]))
        f.close()
        print "data written"
        return
      



