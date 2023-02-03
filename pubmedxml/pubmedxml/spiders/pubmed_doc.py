from pathlib import Path

import scrapy


class PubmedSpider(scrapy.Spider):
    name = 'pubmeddoc'  

    def start_requests(self):
        urls = []

        with open('pubmedxml/spiders/trainpubmed.txt','r' ) as f:
            train_pid = f.read()

            train_pids = train_pid.split('\n')
            train_pid_data = [x.split(' ')[-1] for x in train_pids]
        

        for pids in train_pid_data[:3]:
            urls.append(
                f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={int(pids)}&rettype=xml&retmode=xml')

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = f'pubmed-{page}.xml'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')