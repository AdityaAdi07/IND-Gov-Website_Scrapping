import scrapy

class InfospiderSpider(scrapy.Spider):
    name = "infospider"
    allowed_domains = ["www.india.gov.in"]
    start_urls = ["https://www.india.gov.in/people-groups/life-cycle/senior-citizens"]

    def parse(self, response):
        
        h3_elements = response.xpath('//*[@id="metadata_3rd_level"]/div[2]/div/div[1]/div/div/div/div/ol//h3')

        for h3 in h3_elements:
            
            h3_text = h3.xpath('.//a/text()').get(default='').strip()

            
            url = h3.xpath('.//a/@href').get()
            if url:
                
                url = response.urljoin(url)

           
            yield {
                'text': h3_text,
                'url': url
            }

        
        li_elements = response.xpath('//*[@id="metadata_3rd_level"]/div[2]/div/div[3]/div/div/div/div[2]/ol/li')
        for li in li_elements:
           
            text = li.xpath('.//a/text()').get(default='').strip()
            url = li.xpath('.//a/@href').get()
            if url:
                url = response.urljoin(url)

            
            abt = li.xpath('.//div[contains(@class, "field-content")]/p/text()').get(default='').strip()

           
            yield {
                'SCHEME': text,
                'URL': url,
                'DESCRIPTION': abt
            }
        next_page = 'https://www.india.gov.in/people-groups/life-cycle/senior-citizens?page='
        for i in range (2,5):
            next_page_url = next_page+f'{i}'
            yield response.follow(next_page_url, callback=self.parse)
