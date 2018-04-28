import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    
def start_requests(self):
        urls = [
            'https://www.amazon.com/dp/B01DFKC2SO',
            'http://www.bestbuy.com/site/amazon-echo-dot/5578851.p?skuId=5578851',
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

def parse(self, response):
        item = response.meta.get('item', {})
        item['url'] = response.url
        item['title'] = response.css("span#productTitle::text").extract_first("").strip()
        item['price'] = float(
            response.css("span#priceblock_ourprice::text").re_first("\$(.*)") or 0
        )
        yield item