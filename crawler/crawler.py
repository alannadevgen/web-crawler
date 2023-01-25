from bs4 import BeautifulSoup
from dotenv import load_dotenv
import logging
import os
import requests
from time import sleep
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser
import validators
load_dotenv()


logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

class Crawler:

    def __init__(self, urls=[], max_url=os.environ.get("MAX_URL"), wait_time=5):
        self.__visited_urls = []
        self.__allowed_urls = []
        self.__urls_to_visit = urls
        self.__MAX_URL = int(max_url)
        self.wait_time = wait_time
    
    def get_visited_urls(self):
        '''
        Returns the list of all the links that have been visited
        '''
        return self.__visited_urls

    def get_allowed_urls(self):
        '''
        Returns the list of all the urls that can be crawled
        '''
        return self.__allowed_urls

    def get_urls_to_visit(self):
        '''
        Returns the temporary list of all links found on a given page
        '''
        return self.__urls_to_visit

    @staticmethod
    def get_html_from_url(url):
        '''
        Gets the text of the web page for a given URL
        '''
        return requests.get(url).text

    def get_linked_urls(self, url, html):
        '''
        Find all the links in a HTML page
        '''
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path

    @staticmethod
    def is_crawlable(url):
        '''
        Check if a url can be crawled or not
        
        Returns
        -------
        bool : True if the url can be crawled, False if not.
        '''
        rp = RobotFileParser()
        scheme = urlparse(url).scheme
        domain = urlparse(url).netloc
        link = scheme + "://" + domain + "/robots.txt"
        rp.set_url(link)
        rp.read()
        return rp.can_fetch("*", url)

    @staticmethod
    def get_homepage_url(url):
        scheme = urlparse(url).scheme
        domain = urlparse(url).netloc
        homepage_url = scheme + "://" + domain + "/"
        return homepage_url
    
    @staticmethod
    def is_valid_url(url):
        '''
        Check if the url is valid
        '''
        return validators.url(str(url))

    def add_allowed_urls(self, url):
        '''
        Add a link to the list of crawled URLs if not already in it.
        '''
        if url not in self.__allowed_urls:
            self.__allowed_urls.append(url)
    
    def add_url_to_visit(self, url):
        if url not in self.__visited_urls and url not in self.__urls_to_visit:
            self.__urls_to_visit.append(url)

    def get_sitemap_from_url(self):
        pass

    def crawl(self, url, wait_time):
        html = self.get_html_from_url(url)
        for url in self.get_linked_urls(url, html):
            self.add_url_to_visit(url)

        # politeness: waiting before crawling next url 
        logging.info(f'Waiting {wait_time} seconds')
        sleep(wait_time)

        # add to crawled URLs if it is a valid URL
        is_valid = self.is_valid_url(url)
        if is_valid:
            self.add_allowed_urls(url=url)

    def run(self):
        while self.__urls_to_visit and len(self.__allowed_urls) < self.__MAX_URL:
            url = self.__urls_to_visit.pop(0)
            logging.info(f'Crawling {url}')
            try:
                is_crawlable = self.is_crawlable(url)
                if is_crawlable:
                    self.crawl(url, wait_time=2)
                else:
                    logging.warning(f'URL {url} could not be crawled')
            except Exception:
                logging.exception(f'Failed to crawl: {url}')
            finally:
                self.__visited_urls.append(url)
        
        print()
        print(len(self.__urls_to_visit) + len(self.__visited_urls), ' links found.')
        print(len(self.__visited_urls), ' links visited.')
        print(len(self.__allowed_urls), ' links crawled.')