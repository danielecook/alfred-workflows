#!/usr/env/python
from csv import DictReader
from cStringIO import StringIO
import requests
import yaml
import os
import json
from pprint import pprint as pp
from dateutil.parser import parse
import shutil

token = open(".token", 'r').read()

out = requests.get("https://docs.google.com/spreadsheets/d/1fvURn1gixxC_VbSPr0Ne9dXshffAOKOmpMTmQ9YtGUc/pub?output=tsv")

print out.text
# Save 
with open("_data/workflows.tsv", 'w') as f:
    f.write(out.text)

for repo in DictReader(StringIO(out.text), delimiter = "\t"):
    readme_url = "https://raw.githubusercontent.com/%s/master/README.md" % repo["Github repo"]
    readme = requests.get(readme_url)

    # Format variables
    post_out = "_posts/" + repo["Github repo"]
    directory = os.path.dirname("_posts/" + repo["Github repo"])
    title = repo["Github repo"].split("/")[1]
    username = repo["Github repo"].split("/")[0]

    date_submitted = str(parse(repo["Timestamp"]).date())
    categories = repo["Categories (space delimited)"]
    tags = repo["Tags (space delimited)"]
    star_src = "https://ghbtns.com/github-btn.html?user=" +  username  + "&repo=" + title + "&type=star&count=true"

    # Release Info
    release_url = "https://api.github.com/repos/" + username + "/" + title + "/releases/latest"
    print release_url
    release = requests.get(release_url, auth = ("danielecook", token)).json()
    print pp(release)
    download_url = release["assets"][0]["browser_download_url"]
    download_count = release["assets"][0]["download_count"]
    release_publish_date = release["assets"][0]["created_at"]
    version = release["tag_name"]
    

    # Repo Info
    repo_info = requests.get("https://api.github.com/repos/" + username + "/" + title, auth = ("danielecook", token)).json()
    repo_url = repo_info["html_url"]
    description = repo_info["description"]
    forks = repo_info["forks"]
    stars = repo_info["stargazers_count"]
    watchers = repo_info["watchers"]

    front_matter = """---
title: {title}
layout: post
username: {username}
categories: {categories}
description: "{description}"
tags: {tags}
star_src: "{star_src}"
download_url: "{download_url}"
download_count: {download_count}
release_publish_date: {release_publish_date}
date_submitted: {date_submitted}
forks: {forks}
stars: {stars}
watchers: {watchers}
version: {version}
---

""".format(**locals())
    print front_matter

    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.exists(username):
        os.makedirs(username)
    with open(username + "/index.html", 'w') as f:
        f.write(open("author_index.html").read().replace("<AUTHOR>", username))

    with open("_posts/" + username + "/" + date_submitted + "-" + title + ".md", 'w') as f:
        output = front_matter + readme.text
        output = output.encode('utf-8')
        f.write(output)


