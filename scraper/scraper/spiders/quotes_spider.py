import scrapy
from scrapy.exceptions import CloseSpider


class QuotesSpider(scrapy.Spider):
    QUOTES_TO_LOAD = 3

    quotes_loaded = 0
    name = 'quotes_spider'
    start_urls = ['https://quotes.toscrape.com/']

    # start_urls = ['https://www.sreality.cz/hledani/prodej/byty']
    # https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=60&tms=1687358646532

    def parse(self, response, **kwargs):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }
            self.quotes_loaded += 1
            if self.quotes_loaded >= self.QUOTES_TO_LOAD:
                print("CLOSING DOWN \n\n\n\n")
                raise CloseSpider(f"Required number of quotes ({self.QUOTES_TO_LOAD} loaded.")
