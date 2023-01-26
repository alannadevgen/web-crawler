from unittest import TestCase
from crawler.crawler import Crawler

class TestCrawler(TestCase):
    def test_get_html_valid(self):
        # GIVEN
        url = "https://ensai.fr"
        # WHEN
        crawler = Crawler()
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
        self.assertEqual(crawler.get_urls_to_visit(), [])
        self.assertEqual(crawler.get_visited_sitemaps(), [])

    def test_get_html_invalid(self):
        # GIVEN
        url = "https://eennssaaii.fr"
        # WHEN
        crawler = Crawler()
        result = crawler.get_html_from_url(url=url)
        # THEN
        self.assertIsInstance(crawler, Crawler)
        self.assertEqual(crawler.crawl_fail, 0)
        self.assertEqual(crawler.sitemap_fail, 0)
        self.assertEqual(crawler.homepage_fail, 1)
        self.assertEqual(crawler.get_visited_urls(), [])
        self.assertEqual(crawler.get_crawled_urls(), [])
        self.assertEqual(crawler.get_urls_to_visit(), [])
        self.assertEqual(crawler.get_visited_sitemaps(), [])

    def test_get_linked_urls(self):
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
        crawler = Crawler()
        linked_urls = crawler.get_linked_urls(url, html)
        # THEN
        self.assertEqual(linked_urls, ['https://test.fr/example.html'])
        self.assertEqual(crawler.get_visited_urls(), [])
        self.assertEqual(crawler.get_crawled_urls(), [])
        self.assertEqual(crawler.get_urls_to_visit(), [])
        self.assertEqual(crawler.get_visited_sitemaps(), [])

