from scrapy import Item, Field

class RedditItem(Item):
    title = Field()
    author = Field()
    comments = Field()
    upvotes = Field()
    subreddit = Field()
    post_url = Field()
    timestamp = Field()