from parsel import Selector
import cloudscraper
import json


def url(page: int):
    return f'https://www.olx.com.br/imoveis/aluguel/estado-pb/paraiba/joao-pessoa?o={page}'

# headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

scraper = cloudscraper.create_scraper()

for i in range(1, 101):
    r = scraper.get(url(1))
    response = Selector(text=r.text)
    html = json.loads(response.xpath(
        '//script[@id="__NEXT_DATA__"]/text()').get())
    houses = html.get('props').get('pageProps').get('ads')
    for house in houses:
        offer = {
            'cod_ads': house.get('listId'),
            'title': house.get('title'),
            'category': house.get('category'),
            'price': house.get('price'),
            'location': house.get('location'),
            'properties': house.get('properties')}
