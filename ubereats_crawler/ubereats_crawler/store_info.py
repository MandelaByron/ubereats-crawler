import json
import requests


    
    
def get_store_ids():
    url = "https://www.ubereats.com/api/getSeoFeedV1"

    querystring = {"localeCode":"ke"}

    payload = {"pathname": "/ke/category/nairobi-nairobi/fast-food"}
    headers = {
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

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
    result = []
    jsondata = json.loads(response.text)
    ids = jsondata["data"]['elements'][4]
    ids = ids["feedItems"]
    
    [result.append(i["uuid"]) for i in ids]
    
    return result






# with open(r"C:\Users\HP\Desktop\Ubereats\ubereats.json") as fp:
#     jsondata = json.load(fp)
    
# data= jsondata["data"]["elements"][4]

# for i in data["feedItems"]:
#     print(i['uuid'])
  
    
# with open(r"C:\Users\HP\Desktop\Ubereats\ubereats1.json") as fp:
#     jsondata = json.load(fp)
    
# name = jsondata["data"]['title']
# location = jsondata["data"]["location"]["address"]
# city = jsondata["data"]["location"]["city"]
# lat = jsondata["data"]["location"]["latitude"]
# longitude = jsondata["data"]["location"]["longitude"]
# ratingValue = jsondata["data"]['rating']["ratingValue"]
# reviewCount = jsondata["data"]['rating']["reviewCount"]
# categories = jsondata["data"]['categories']
# cusineList = jsondata["data"]["cuisineList"]
# print(cusineList)
#print(name, location , city , lat , longitude)

