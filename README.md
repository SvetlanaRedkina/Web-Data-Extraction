<img
  align="right"
  src="logo.jpg"
  style="width: 230px; height: 130px"> 
# Web Data Extraction

If you like me love working with data, then you might be interested 👀 how to extract data for Analysis in an efficient and fast way.

With the help of web scraping, you can extract data from any website, no matter how large is the data, on your computer 💻. 

For this project, I use Python's 🐍 Scrapy.

There are currently two folders in the repo:

# 1. Chewy 🐶 😹

In dogs_food.py file, you can see that DogsFoodSpider(CrawlSpider) scrapes the information from Chewy.com about dogs wet food.

The scraped data is stored into Wet_Dog_Food.csv

I can use the data to analyze the price-quality relationships of the scraped items. 

The end goal is to find the best food for my wonderful dog Yuna 🐕

# 3. Indeed 👷

In jobs_ny.py file, you will find class JobsNySpider(scrapy.Spider) that scrapes data from Indeed.com.

I am interested in gathering information about Analytics job postings.

Job location: New York, NY

The scraped data is stored into Analytics_Jobs_NY_Indeed.csv

I will use the data I have collected to explore Analytics' job market in NY 📈.
