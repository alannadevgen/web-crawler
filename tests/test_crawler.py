from unittest import TestCase
from crawler.crawler import Crawler

class TestCrawler(TestCase):
    def test_get_html_valid(self):
        # GIVEN
        url = "https://ensai.fr"
        # WHEN
        crawler = Crawler(max_url=5)
        result = crawler.get_html_from_url(url=url)
        # THEN
        self.assertIsInstance(crawler, Crawler)
        self.assertIsNotNone(result)
        self.assertIn('<!DOCTYPE html>', result)
        self.assertIn('</html>', result)
        self.assertEqual(crawler.crawl_fail, 0)
        self.assertEqual(crawler.sitemap_fail, 0)
        self.assertEqual(crawler.homepage_fail, 0)
        self.assertEqual(crawler.get_visited_urls(), [])
        self.assertEqual(crawler.get_crawled_urls(), [])
        self.assertEqual(crawler.get_visited_sitemaps(), [])

    def test_get_html_invalid(self):
        # GIVEN
        url = "https://mytinyurl.com"
        # WHEN
        crawler = Crawler(max_url=5)
        result = crawler.get_html_from_url(url=url)
        # THEN
        self.assertIsInstance(crawler, Crawler)
        self.assertEqual(crawler.crawl_fail, 0)
        self.assertEqual(crawler.sitemap_fail, 0)
        self.assertEqual(crawler.homepage_fail, 1)
        self.assertEqual(crawler.get_visited_urls(), [])
        self.assertEqual(crawler.get_crawled_urls(), [])
        self.assertEqual(crawler.get_visited_sitemaps(), [])

    def test_get_linked_urls_valid(self):
        # GIVEN
        url = 'https://test.fr/'
        html = """<!DOCTYPE html>
        <html>   
        <head>
            <title>Example</title>
        </head>
            
        <body>
            <a href = "https://test.fr/example.html" </a>
        </body>	
        </html>"""
        # WHEN
        crawler = Crawler(max_url=5)
        linked_urls = crawler.get_linked_urls(url, html)
        # THEN
        self.assertIsInstance(crawler, Crawler)
        self.assertEqual(linked_urls, ['https://test.fr/example.html'])
        self.assertEqual(len(linked_urls), 1)
        self.assertEqual(crawler.get_visited_urls(), [])
        self.assertEqual(crawler.get_crawled_urls(), [])
        self.assertEqual(crawler.get_visited_sitemaps(), [])

    def test_get_linked_urls_invalid(self):
        # GIVEN
        url = 'https://test.fr/'
        html = """<!DOCTYPE html>
        <html>   
        <head>
            <title>Example</title>
        </head>
            
        <body>
            Some text
        </body>	
        </html>"""
        # WHEN
        crawler = Crawler(max_url=5)
        linked_urls = crawler.get_linked_urls(url, html)
        # THEN
        self.assertIsInstance(crawler, Crawler)
        self.assertEqual(linked_urls, [])
        self.assertEqual(len(linked_urls), 0)
        self.assertEqual(crawler.get_visited_urls(), [])
        self.assertEqual(crawler.get_crawled_urls(), [])
        self.assertEqual(crawler.get_visited_sitemaps(), [])
        self.assertEqual(len(crawler.get_urls_to_visit()), 1)
        self.assertEqual(len(crawler.get_visited_urls()), 0)
        self.assertEqual(len(crawler.get_crawled_urls()), 0)

    def test_add_url_to_visit_valid(self):
        # GIVEN
        url = 'https://test.fr/example.html'
        # WHEN
        crawler = Crawler(max_url=1)
        crawler.add_url_to_visit(url)
        # THEN
        self.assertIsInstance(crawler, Crawler)
        self.assertEqual(crawler.get_urls_to_visit(), [url])
        self.assertEqual(crawler.get_visited_urls(), [])
        self.assertEqual(crawler.get_crawled_urls(), [])
        self.assertEqual(len(crawler.get_urls_to_visit()), 1)
        self.assertEqual(len(crawler.get_visited_urls()), 0)
        self.assertEqual(len(crawler.get_crawled_urls()), 0)

    def test_is_crawlable_valid(self):
        # GIVEN
        url = 'https://ensai.fr/'
        # WHEN
        crawler = Crawler(max_url=1)
        result = crawler.is_crawlable(url=url)
        # THEN
        self.assertIsInstance(crawler, Crawler)
        self.assertTrue(result)

    def test_is_crawlable_invalid(self):
        # GIVEN
        url = 'https://facebook.com/'
        # WHEN
        crawler = Crawler(max_url=1)
        result = crawler.is_crawlable(url=url)
        # THEN
        self.assertIsInstance(crawler, Crawler)
        self.assertFalse(result)

    def test_get_homepage_url(self):
        # GIVEN
        url = 'https://ensai.fr/double-diplome-universite-rome-sapienza/'
        # WHEN
        crawler = Crawler(max_url=1)
        result = crawler.get_homepage_url(url=url)
        # THEN
        self.assertIsInstance(crawler, Crawler)
        self.assertEqual(result, 'https://ensai.fr/')
        
