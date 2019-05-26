
import feedparser
from hosted import node, config
import json


def parse(url):
    print("Fetching RSS content from: " + url)
    d = feedparser.parse(url)
    print("Received " + str(len(d['entries'])) + " items. Processing...")
    rssTitles = []
    for post in d.entries:
        print("Adding RSS post title: " + post.title)
        title = '{"text": "' + post.title + '", "color": {"a":0,"b":0,"g":0,"hex":"000000","r":0,"rgba":[0,0,0,0]}, "blink": false, "show": true}'
        rssTitles.append(title)
    data = {}
    data['texts'] = rssTitles
    print("returning data")
    return data

def save_rssTitles(rssTitles):
    print("loading config file...")
    with open('/space/root/scroller/config.json', 'r') as f:
        print("config file loaded.")
        localconfig = json.load(f)
        print("local var set for localconfig")
    print("Local config Type: " + str(type(localconfig)))
    print(str(len(localconfig)))
    print("Texts: ")
    print(str(localconfig['texts']))
    node.write_json("rssTitles.json", rssTitles)


def filter_and_save(rssTitles):
    print("starting filter_and_save function...")
    save_rssTitles(rssTitles)
    return rssTitles
