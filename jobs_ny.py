# -*- coding: utf-8 -*-
import scrapy


class JobsNySpider(scrapy.Spider):
    name = 'jobs_ny'
    allowed_domains = ['www.indeed.com']
    start_urls = ['https://www.indeed.com/jobs?q=data&l=New%20York%2C%20NY&vjk=40af8feeac4a6e5a']

    def parse(self, response):
        jobs = response.xpath("//td[@id='resultsCol']")
        for job in jobs:
            yield {
                'Job_title': job.xpath(".//h2[contains(@class, 'jobTitle')]/span/text()").get(),
                'Company_name': job.xpath(".//span[@class='companyName']/a/text()").get(),
                'Company_rating': job.xpath(".//span[contains(@class, 'rating')]/span/text()").get(),
                'Company_location': job.xpath(".//div[@class='companyLocation']/text()").get(),
                'Estimated_salary': job.xpath(".//span[@class='estimated-salary']/span/text()").get(),
            }

        next_page = response.urljoin(response.xpath("//ul[@class='pagination-list']/li[position() = last()]/a/@href").get())

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
