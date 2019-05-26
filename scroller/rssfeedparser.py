
import feedparser
from hosted import node
import json


def parse(url):
    print("Fetching RSS content from: " + url)
    d = feedparser.parse(url)
    print("Received " + str(len(d['entries'])) + " items. Processing...")
    rssTitles = []
    for post in d.entries:
        print("Adding RSS post title: " + post.title)
        title = {"text": post.title, "color": {"a":0,"b":0,"g":0,"hex":"000000","r":0,"rgba":[0,0,0,0]}, "blink": false, "show": true}
        titlecontent = json.dumps(title)
        rssTitles.append(titlecontent)
    data = {}
    data['texts'] = rssTitles
    json_data = json.dumps(data)
    return json_data

def save_rssTitles(rssTitles):
    node.write_json("rssTitles.json", rssTitles)

def filter_and_save(rssTitles):
    save_rssTitles(rssTitles)
    return rssTitles


"texts":[{"blink":false,"color":{"a":0,"b":0,"g":0,"hex":"000000","r":0,"rgba":[0,0,0,0]},"show":true,"text":"hello world"},{"blink":false,"color":{"a":0,"b":0,"g":0,"hex":"000000","r":0,"rgba":[0,0,0,0]},"show":true,"text":"test"},{"blink":false,"color":{"a":0,"b":0,"g":0,"hex":"000000","r":0,"rgba":[0,0,0,0]},"show":true,"text":"Why won't this work?"}]
