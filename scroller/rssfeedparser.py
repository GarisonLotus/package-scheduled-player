
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
    print("Here is rssTitles: ")
    print(rssTitles)
    data = {}
    data['texts'] = rssTitles
    print("Data being sent to json file:")
    print(data)
    return data

def save_rssTitles(rssTitles):
    node.write_json("rssTitles.json", rssTitles)
    with open('config.json', 'r') as f:
        localconfig = json.load(f)
        print("Local config:")
        print(localconfig)

def filter_and_save(rssTitles):
    save_rssTitles(rssTitles)
    return rssTitles
