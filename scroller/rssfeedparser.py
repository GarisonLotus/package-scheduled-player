
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
        title = {"text": post.title, "color": "[0,0,0,0]", "blink": "false", "show": "true"}
        titlecontent = json.dumps(title)
        print("json:")
        print(str(titlecontent))
        rssTitles.append(titlecontent)
    return rssTitles

def save_rssTitles(rssTitles):
    node.write_json("rssTitles.json", rssTitles)

def filter_and_save(rssTitles):
    save_rssTitles(rssTitles)
    return rssTitles
