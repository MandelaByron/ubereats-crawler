import scrapy
from ..store_info import get_store_ids
import json
import time

uuids = get_store_ids()
class UberSpider(scrapy.Spider):
    name = 'uber'
    allowed_domains = ['ubereats.com']

    #start_urls = ['http://ubereats.com/']
    
    def start_requests(self):
        #querystring = {"localeCode":"ke"}
        for uuid in uuids:
            payload = {
                "storeUuid": f"{uuid}",
                "sfNuggetCount": 0
            }
            url = "https://www.ubereats.com/api/getStoreV1?localeCode=ke"


            time.sleep(0.5)
            yield scrapy.Request(method ="POST", url=url, body=json.dumps(payload) , callback= self.parse)
            
        

    def parse(self, response):
        
        jsonresponse = json.loads(response.body.decode('utf-8'))
       # print(jsonresponse)
        name = jsonresponse["data"]['title']
        location = jsonresponse["data"]["location"]["address"]
        city = jsonresponse["data"]["location"]["city"]
        lat = jsonresponse["data"]["location"]["latitude"]
        longitude = jsonresponse["data"]["location"]["longitude"]
        ratingValue = jsonresponse["data"]['rating']["ratingValue"]
        reviewCount = jsonresponse["data"]['rating']["reviewCount"]
        categories = jsonresponse["data"]['categories']
        cusineList = jsonresponse["data"]["cuisineList"]
        
        yield {
            "name":name,
            "location":location,
            "city":city,
            "latitude":lat,
            "longitude":longitude,
            'ratingValue':ratingValue,
            'reviewCount':reviewCount,
            'categories':categories,
            'cusineList':cusineList
        }
    
# import requests



# print(response.text)