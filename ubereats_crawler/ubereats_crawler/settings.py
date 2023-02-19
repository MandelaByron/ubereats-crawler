# Scrapy settings for ubereats_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ubereats_crawler'

SPIDER_MODULES = ['ubereats_crawler.spiders']
NEWSPIDER_MODULE = 'ubereats_crawler.spiders'

RETRY = 3

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ubereats_crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "cookie": "uev2.id.xp=af1ae106-e9e8-436e-a9dc-8bcd3db4df99; dId=8ac04387-b5c7-4762-af98-e65cba818384; uev2.id.session=7e2b3109-d61d-401f-a175-7803c2df365f; uev2.ts.session=1676596195497; marketing_vistor_id=45e6898f-790b-423a-89dd-7f5cf8fceec4; jwt-session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7Il9fand0X3JwY19wcm90ZWN0aW9uX2V4cGlyZXNfYXRfbXMiOjE2NzY1OTgxNjU1MTUsIl9fand0X3JwY19wcm90ZWN0aW9uX3V1aWQiOiIyMGM5NDNhZC0yOTNlLTRkY2MtOTM5Mi04MjU5ZWFlNjYyMjQiLCJfX2p3dF9ycGNfcHJvdGVjdGlvbl9jcmVhdGVkX2F0X21zIjoxNjc2NTk2MTk1NTE1fSwiaWF0IjoxNjc2NTk2MTk1LCJleHAiOjE2NzY2ODI1OTV9.jsnWWvPVOBQZ85ICmIXJT5epsyEsLTwzGh-836NDAxs; uev2.gg=true; utm_medium=undefined; fm_conversion_id=undefined; utm_source=undefined; CONSENTMGR=c1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1676596198788%7Cconsent:true; _userUuid=; uev2.diningMode=DELIVERY; utag_main=v_id:01865cebbd3a007da387c6f101100406f001b06700bd0$_sn:1$_se:5$_ss:0$_st:1676598036949$ses_id:1676596198725%3Bexp-session$_pn:1%3Bexp-session",
    "authority": "www.ubereats.com",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.5",
    "content-type": "application/json",
    "origin": "https://www.ubereats.com",
    "referer": "https://www.ubereats.com/ke/category/nairobi-nairobi/fast-food",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "x-csrf-token": "x"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ubereats_crawler.middlewares.UbereatsCrawlerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'ubereats_crawler.middlewares.UbereatsCrawlerDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'ubereats_crawler.pipelines.UbereatsCrawlerPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 30
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
