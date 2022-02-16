# I am interested in gathering information about Analytics job postings
# Job location: New York, NY
# To achive my goal, I created a spider 'jobs_ny'
# jobs_ny scrapes the data from indeed.com

# What I want to scrape:
# 'Job_title'
# 'Company_name'
# 'Company_rating'
# 'Company_location'
# 'Estimated_salary' (if applicable)

# The scraped data is stored into Analytics_Jobs_NY_Indeed.csv

import scrapy


class JobsNySpider(scrapy.Spider):
    name = 'jobs_ny'
    allowed_domains = ['www.indeed.com']
    start_urls = ['https://www.indeed.com/jobs?q=analytics&l=New%20York%2C%20NY&vjk=7b2f6385304ffc78']

    def parse(self, response):
        jobs = response.xpath('//div[@id="mosaic-provider-jobcards"]/a')
        for job in jobs:
            yield {
                'Job_title': job.xpath(".//td[@class='resultContent']/div/h2/span/text()").get(),
                'Company_name': job.xpath(".//span[@class='companyName']/a/text()").get(),
                'Company_rating': job.xpath(".//span[@class='ratingNumber']/span/text()").get(),
                'Company_location': job.xpath(".//div[@class='companyLocation']/text()").get(),
                'Estimated_salary': job.xpath(".//span[@class='estimated-salary']/span/text()").get()
            }
        
        # next_page helps us to deal with pagination
        # Otherwise, the spider won't scrape data from all pages

        next_page = response.xpath("//a[@aria-label='Next']/@href").get()

        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)
