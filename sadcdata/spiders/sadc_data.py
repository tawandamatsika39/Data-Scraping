# -*- coding: utf-8 -*-
import scrapy


class SadcDataSpider(scrapy.Spider):
    name = 'sadc_data'
    allowed_domains = ['www.sadc.int']
    start_urls = ['https://www.sadc.int/themes/natural-resources/water']

    def parse(self, response):
        #pass
        print("Fetching Data at :"+response.url)
        countries = response.xpath("//tr/td[@class='table']/p/text()").extract()
        
        row_data = zip(countries)
        #print (row_data) 'page':response.url,
        for item in row_data:
        	scraped_info = {
        					
        					'data':item

        					}
        	yield scraped_info