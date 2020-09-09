import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from Clickfunnels.items import ScrapyloginItem

class DuifLogin(scrapy.Spider):
    name = "clickfunnels"
    start_urls = ['https://app.clickfunnels.com/users/sign_in']
    
    def parse(self, response):
        token = response.css('input[name=authenticity_token]::attr(value)').extract_first()
        yield FormRequest.from_response(response,formdata={
            'user[email]' : 'support@restrictedmembersonly.com',
            'user[password]' : '1HhtVM0@XW&L3T!'
            'authenticity_token': token,
            'username' : '*****',
            'password' : '*****',
        },callback=self.after_login)

    def after_login(self, response):
        open_in_browser(response)
        
        card = response.xpath('//div[@class="row myaccountrow"]')

        if card:
            print('success')

        else:
            print(':(')