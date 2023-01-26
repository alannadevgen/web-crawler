# Web crawler :computer:

The aim of this project is to perform a single-threaded web crawler using a single start point, where with the [ENSAI's URL](https://ensai.fr). The program searches for other pages to explore by analyzing the link tags found in the previously explored documents. It will stop once the number of crawled URLs defined by the user is reached (by default 50). Finally, it will output the URLs in a file.

The crawler has to respect a simple politeness rule: wait five seconds before downloading the next one.

## Quick start

First, you will need to clone the repo.
```bash
git clone https://github.com/alannagenin/web-crawler.git
cd web-crawler
```

Then, we will set a virtual environment and download the necessary packages.
```python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Before lanching the crawler, you should create an `.env` file containing the default values:
```
URL = https://ensai.fr/
MAX_URL = 50
```

Finally, to launch the crawler there are several options:
```python
# to get some help
python3 main.py --help
# with default parameters
python3 main.py
# with specified parameters
python3 main.py --start_point "https://www.ensae.fr/" --max_url 100
```

## Description of the program

The goal here is to build a simple web crawler, with the purpose of retrieving URLs from a starting URL.

From an input URL that the user enters, the crawler finds other pages to crawl by first analyzing the *robots.txt* file of the requested URL. If this file does not exist, or if it does not contain a sitemap allowing easy retrieval of URLs, the crawler parses the HTML code of the requested URL and retrieves the link tags (`a` tags) found in the code.

The crawler then takes one of the retrieved URLs and starts its scan again, until the program ends. It ends when the web crawler reaches the limit of URLs to be found (limit set by the user), or if it finds no more links to explore.

Once finished, the program writes all the URLs found to a file *crawled_webpages.txt*.

## Unit tests

To launch tests:
```python
python3 -m unittest
```


## Areas of improvement

Get the crawler to multi-thread.

## Contributor

[Alanna DEVLIN-GENIN](https://github.com/alannagenin/)