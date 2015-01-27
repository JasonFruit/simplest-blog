import os
from codecs import open
from datetime import datetime

from Cheetah.Template import Template
from markdown import markdown
from dateutil.parser import parse
from glob import glob

title = "On Taking an Interest"

def title_to_filename(title):
    return "".join([c for c in title.lower().replace(" ", "_")
                    if c in u"abcdefghijklmnopqrstuvwxyz_"])

class Post(object):
    def __init__(self, title, content, attributes=list()):
        self.title = title
        self.content = content
        self.url = "%s.html" % title_to_filename(title)
        self.attributes = attributes
    def __repr__(self):
        if self.attributes["publish"] == "no":
            return "Draft post: %s" % self.title
        else:
            return "Published post: %s" % self.title

delim_line = u"<!-- Post Markdown begins here -->"

posts = []

for fn in glob("sources/*.md"):
    
    lines = open(fn, "r", "utf-8").readlines()

    in_content = False

    content = []
    attributes = {}

    for i in range(len(lines)):

        line = unicode(lines[i])

        if line.startswith(delim_line):
            in_content = True
        else:
            if in_content:
                content.append(line)
            else:
                elements = line.split(":")
                attributes[elements[0]] = ":".join(elements[1:]).strip()

    content = u"".join(content)

    post = Post(attributes["title"],
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

posts.sort(datecmp)

for post in posts:
    if attributes["publish"] != "no":
        post_html = unicode(
            Template(open("post.tmpl", "r", "utf-8").read(),
                     searchList = [{"title": title,
                                    "post": post,
                                    "date": post.attributes["date"]}]))

        open("posts/%s" % post.url,
             "w",
             "utf-8").write(post_html)

index_html = unicode(
    Template(open("main.tmpl", "r", "utf-8").read(),
             searchList = [{"title": title,
                            "posts": [post for post in posts
                                      if post.title.lower() not in ["about", "links"]
                                      and post.attributes["publish"] != "no"][:3],
                            "date": "2015-present"}]))

open("posts/index.html", "w", "utf-8").write(index_html)

posts.sort(titlecmp)

post_index_html = unicode(
    Template(open("post_index.tmpl", "r", "utf-8").read(),
             searchList = [{"title": title,
                            "posts": [post for post in posts
                                      if post.attributes["publish"] != "no"],
                            "date": datetime.now().strftime("%B %d, %Y")}]))
open("posts/post_index.html", "w", "utf-8").write(post_index_html)

os.system("cp *.css posts/")
os.system("cp robots.txt posts/")
os.system("cp favicon.ico posts/")
