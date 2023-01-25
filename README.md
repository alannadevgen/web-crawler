# Web crawler :computer:

The aim of this project is to perform a single-threaded web crawler using a single start point, where with the [ENSAI's URL](https://ensai.fr). The program searches for other pages to explore by analyzing the link tags found in the previously explored documents. It will stop once the number of crawled URLs defined by the user is reached (by default 50). Finally, it will output the URLs in a file.

The crawler has to respect a simple politeness rule: wait five seconds before downloading the next one.

## Quick start

First, you will need to clone the repo.
```bash
git clone https://github.com/alannagenin/web-crawlergit
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
URL=https://ensai.fr/
MAX_URL = 50
```

Finally, we will launch the crawler:
```python
python3 -m main
# or python3 main.py
```

## Areas of improvement

Get the crawler to multi-thread.

## Contributors

Alanna DEVLIN-GENIN