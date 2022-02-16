# For this project, I am interested in collecting data about pets food
# Food type: Wet Dog Food
# In order to achive my goal, I created a crawler 'dogs_food'
# dogs_food scrapes the data from chewy.com

# What I want to scrape:
# 'Title'
# 'Price'
# 'Price_autoship' (if applicable)
# 'Ingredients_list'
# 'Item_url'
# It is important that 'Ingredients_list' should include information from all subcategories within the position
# For example, 'Beef', 'Filet Mignon', 'Grilled Chicken', and 'Porterhouse Steak' for 'Cesar Classic Loaf in Sauce'
# Listing the ingredients only for 'Beef' is not accepted

# The scraped data is stored into Wet_Dog_Food.csv


import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DogsFoodSpider(CrawlSpider):
    name = 'dogs_food'
    allowed_domains = ['www.chewy.com']
    start_urls = ['https://www.chewy.com/b/wet-food-293']

    # Rule that restricts xpath to 
    # "//a[@class='kib-pagination-new-item kib-pagination-new-item--interactive kib-pagination-new-item--next']" deals with pagination
    # The pagination Rule comes second, otherwise, the first page will be skipped
     
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h2[@class='ProductListing_plpProductCardTitleWrapper__vNDZF']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//a[@class='kib-pagination-new-item kib-pagination-new-item--interactive kib-pagination-new-item--next']"))
    )

    def parse_item(self, response):
        yield {
            'Title': response.xpath("normalize-space(//div[@id='product-title']/h1/text())").get(),
            'Price': response.xpath("normalize-space(//span[@class='ga-eec__price']/text())").get(),
            'Price_autoship': response.xpath("normalize-space(//p[@class='autoship-pricing p']/text())").get(),
            'Ingredients_list': response.xpath("//section[@class='cw-tabs__content--left']/p[normalize-space(text())]/text()").getall(),
            'Item_url': response.url
        }

