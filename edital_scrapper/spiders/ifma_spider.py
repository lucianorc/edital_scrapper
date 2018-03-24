import scrapy


class IfmaSpider(scrapy.Spider):
    name = 'ifma'

    def start_requests(self):
        url = 'https://portal.ifma.edu.br/concursos-e-seletivos/'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        editais = response.css('div.tile-list-1 div.video-item.row-fluid div.tileItem')

        for edital in editais:
            attachment_block = edital \
                .css('div.row-fluid div.catItemAttachmentsBlock') \
                .css('ul.catItemAttachments li')
            attachments = dict()

            items = attachment_block.css('a::text').extract()[1::2]

            for i in range(len(attachment_block.css('a::attr(href)'))):
                attachments[i] = dict(
                    item=items[i],
                    link=response.url+attachment_block.css('a::attr(href)').extract()[i]
                )


            yield {
                'title': edital.css('div.tileHeader h2 a::text').extract_first(),
                'description': edital.css('span::text').extract_first(),
                'attachments': attachments,
                'information': {
                    'date': edital.css('div.tileInfo ul li::text').extract()[0],
                    'type': edital.css('div.tileInfo ul li::text').extract()[1],
                    'campus': edital.css('div.tileInfo ul li::text').extract()[2],
                    'situation': edital.css('div.tileInfo ul li span::text').extract_first()
                }
            }
