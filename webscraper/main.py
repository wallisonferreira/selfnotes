# import urllib.request
from bs4 import BeautifulSoup
import requests


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        # r = urllib.request.urlopen(self.site)
        # html = r.read()
        
        page = requests.get(self.site)
        print("Status code " + page.status_code)
        html = page.content
        
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)
                

news = Scraper("https://globo.com/")
scraper = Scraper(news)
scraper.scrape()
# scrape.scrape()