from pathlib import Path

import scrapy


class PubmedSpider(scrapy.Spider):
    name = 'test_pubmeddoc'

    custom_settings = {
        'CONCURRENT_REQUESTS_PER_IP': 3,
        'DOWNLOAD_DELAY': 0.33,
        'JOBDIR': 'crawlstest/test_pubmeddoc'
    }

    def extract_data():
        with open('pubmedxml/spiders/testpubmed.txt', 'r') as f:
            train_pid = f.read()

            train_pids = train_pid.split('\n')
            train_pid_data = [x.split(' ')[-1] for x in train_pids]
            data = sorted(list(set(train_pid_data)))
            data = data

        for pids in data:
            yield f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pids}&rettype=xml&retmode=xml'

    data = extract_data()

    def start_requests(self):
        for url in self.data:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split('&')[-3].split('=')[-1]
        filename = f'pubmed-{page}.xml'
        Path('pid_doc_test/'+filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')
