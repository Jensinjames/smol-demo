# Importing necessary libraries from Scrapy
import scrapy
from scraper_project.scraper_project.items import RedditItem

class RedditSpider(scrapy.Spider):
    name = 'reddit_spider'
    allowed_domains = ['reddit.com']
    start_urls = ['https://www.reddit.com/']

    def parse(self, response):
        # Extracting the content using css selectors
        posts = response.css('div.Post')
        for post in posts:
            item = RedditItem()
            item['title'] = post.css('h3::text').get()
            item['author'] = post.css('a._2tbHP6ZydRpjI44J3syuqC::text').get()
            item['comments'] = post.css('a.FHCV02u6Cp2zYL0fhQPsO::text').get()
            yield item

        # Handling pagination
        next_page = response.css('a.next-button::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    # You can implement parse_item method if you need to handle more complex data extraction
    # def parse_item(self, response):
    #     # Your code to parse individual items
    #     pass
