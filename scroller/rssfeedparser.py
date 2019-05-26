
import feedparser
from hosted import node
import json


def parse(url)
d = feedparser.parse(url)
rssTitles = []
for post in d.entries:
    print(post.title)
    title = {"text": post.title, "color": "[0,0,0,0]", "blink": "false", "show": "true"}
    title = json.loads(title)
    rssTitles.append(title)
return rssTitles

def save_rssTitles(rssTitles)
    node.write_json("rssTitles.json", rssTitles)

def filter_and_save(rssTitles):
    save_rssTitles(rssTitles)
    return rssTitles
