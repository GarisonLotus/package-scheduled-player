
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
        t = {}
        c = {}
        t['text'] = post.title
        c["a"] = 0
        c["b"] = 0
        c["g"] = 0
        c["hex"] = 000000
        c["rgba"] = [0, 0, 0, 0]
        t['color'] = c
        t['blink'] = False
        t['show'] = True
        rssTitles.append(t)
    data = {}
    data['texts'] = rssTitles
    return data

def save_rssTitles(rssTitles):
    node.write_json("rssTitles.json", rssTitles)

def filter_and_save(rssTitles):
    save_rssTitles(rssTitles)
    return rssTitles
