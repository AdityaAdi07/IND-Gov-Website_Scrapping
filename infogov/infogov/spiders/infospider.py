import scrapy

class InfospiderSpider(scrapy.Spider):
    name = "infospider"
    allowed_domains = ["www.india.gov.in"]
    start_urls = ["https://www.india.gov.in/people-groups/life-cycle/senior-citizens"]

    def __init__(self, state='', *args, **kwargs):
        super(InfospiderSpider, self).__init__(*args, **kwargs)
        self.state = state.lower() 

    def parse(self, response):
        li_elements = response.xpath('//*[@id="metadata_3rd_level"]/div[2]/div/div[5]/div/div/div/div[2]/ol/li')

        for li in li_elements:
            text = li.xpath('.//a/text()').get(default='').strip()
            url = li.xpath('.//a/@href').get()
            if url:
                url = response.urljoin(url)
            abt = li.xpath('.//div[contains(@class, "field-content")]/p/text()').get(default='').strip()

            
            is_highlighted = self.state in abt.lower()

            yield {
                'SCHEME': text,
                'URL': url,
                'DESCRIPTION': abt,
                'HIGHLIGHT': is_highlighted  
            }

        next_page = 'https://www.india.gov.in/people-groups/life-cycle/senior-citizens?page='
        for i in range(0, 4):
            next_page_url = next_page + f'{i}'
            yield response.follow(next_page_url, callback=self.parse)
