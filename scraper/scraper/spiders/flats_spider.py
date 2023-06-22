import json

import scrapy
from scrapy.exceptions import CloseSpider


class FlatsSpider(scrapy.Spider):
    FLATS_TO_LOAD = 500

    flats_loaded = 0
    name = 'flats_spider'
    start_urls = [
        f'https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page={FLATS_TO_LOAD}&tms=1687358646532'
    ]

    def parse(self, response, **kwargs):
        data = json.loads(response.text)
        for flat in data["_embedded"]["estates"]:
            yield {
                "title": flat["name"],
                "image": flat["_links"]["images"][0]["href"]
            }
            self.flats_loaded += 1
            if self.flats_loaded >= self.FLATS_TO_LOAD:
                print("Closing down the spider.\n")
                raise CloseSpider(f"Required number of flats ({self.FLATS_TO_LOAD} loaded.")
