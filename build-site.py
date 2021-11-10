from __future__ import unicode_literals, print_function

import json
import os
from codecs import open
from datetime import datetime

from mako.template import Template
from markdown import markdown
from dateutil.parser import parse
from glob import glob

post_tmpl = Template(open("post.tmpl", "r", "utf-8").read())
main_tmpl = Template(open("main.tmpl", "r", "utf-8").read())
post_index_tmpl = Template(open("post_index.tmpl", "r", "utf-8").read())

with open("metadata.json", "r", "utf-8") as f:
    metadata = json.load(f)
    title = metadata["title"]
    name = metadata["name"]
    tagline = metadata["tagline"]

# def title_to_filename(title):
#     return "".join([c for c in title.lower().replace(" ", "_")
#                     if c in "abcdefghijklmnopqrstuvwxyz_"])

class Post(object):
    def __init__(self, fn, title, date, content, attributes=list()):
        self.title = title
        self.date = date
        self.content = content
        self.url = fn.replace(".md", ".html")
        self.attributes = attributes
    def __repr__(self):
        if self.attributes["publish"] == "no":
            return "Draft post: %s" % self.title
        else:
            return "Published post: %s" % self.title

delim_line = "<!-- Post Markdown begins here -->"

posts = []

sources = glob("sources/*.md")

sources = [source for source in sources
           if source != "sources/draft.md"]

if not os.path.exists("posts"):
    os.mkdir("posts")
    
for fn in sources:
    
    lines = open(fn, "r", "utf-8").readlines()

    in_content = False

    content = []
    attributes = {}

    for i in range(len(lines)):

        line = str(lines[i])

        if line.startswith(delim_line):
            in_content = True
        else:
            if in_content:
                content.append(line)
            else:
                elements = line.split(":")
                attributes[elements[0]] = ":".join(elements[1:]).strip()

    content = "".join(content)

    post = Post(fn.split("/")[-1],
                attributes["title"],
                attributes["date"],
                markdown(content, output_format="xhtml"),
                attributes = attributes)

    posts.append(post)

def datecmp(b, a):
    try:
        return cmp(parse(a.attributes["date"]).toordinal(),
                   parse(b.attributes["date"]).toordinal())
    except ValueError:
        return 0

def titlecmp(a, b):
    try:
        return cmp(a.title, b.title)
    except ValueError:
        return 0

os.system("rm posts/*")

def post_ordering(p):
    d = parse(p.attributes["date"]).toordinal()
    return 0 - d

posts.sort(key=post_ordering)

for post in posts:
    if post.attributes["publish"] != "no":
        post_html = post_tmpl.render(title=title,
                                     name=name,
                                     tagline=tagline,
                                     post=post,
                                     date=post.attributes["date"])
        open("posts/%s" % post.url,
             "w",
             "utf-8").write(post_html)

index_html = main_tmpl.render(title=title,
                              name=name,
                              tagline=tagline,
                              posts=[
                                  post for post in posts
                                  if post.title.lower() not in ["about", "about me", "links"]
                                  and post.attributes["publish"] != "no"][:3],
                              date="2015-present")

open("posts/index.html", "w", "utf-8").write(index_html)

posts.sort(key=lambda p: p.title)

post_index_html = post_index_tmpl.render(
    title=title,
    name=name,
    tagline=tagline,
    posts=[post for post in posts
           if post.attributes["publish"] != "no"],
    date=datetime.now().strftime("%B %d, %Y"))
open("posts/post_index.html", "w", "utf-8").write(post_index_html)

os.system("cp *.css posts/")
os.system("cp robots.txt posts/")
os.system("cp favicon.ico posts/")
os.system("cp files/* posts/")
