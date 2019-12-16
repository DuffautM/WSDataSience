import pymongo
import urllib.request
import json


def insert_data_atlas(raw_data):
    client = pymongo.MongoClient("mongodb://user1:root@clustecesi-shard-00-00-5w5zu.mongodb.net:27017,clustecesi-shard-00-01-5w5zu.mongodb.net:27017,clustecesi-shard-00-02-5w5zu.mongodb.net:27017/test?ssl=true&replicaSet=ClusteCesi-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.openWeather
    posts = db.weatherData
    posts.insert_many(raw_data)


def get_data_accuweather():
    key = "NRdqAxI7JXCBeuLdJ5OaWyS2xlVWFG9s"
    url = "http://dataservice.accuweather.com/currentconditions/v1/"
    location = "135244"
    param = "&language=fr-fr&details=true"
    request = url + location + "?apikey=" + key + param
    contents = urllib.request.urlopen(request)
    return json.load(contents)


data = get_data_accuweather()
insert_data_atlas(data)
