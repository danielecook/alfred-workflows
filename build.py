#!/usr/env/python
from csv import DictReader
from cStringIO import StringIO
import requests
import os
from pprint import pprint as pp
from dateutil.parser import parse
import re

token = open(".token", 'r').read()

out = requests.get("https://docs.google.com/spreadsheets/d/1fvURn1gixxC_VbSPr0Ne9dXshffAOKOmpMTmQ9YtGUc/pub?output=tsv")

# Save 
with open("_data/workflows.tsv", 'w') as f:
    f.write(out.text)

for repo in DictReader(StringIO(out.text), delimiter = "\t"):
    readme_url = "https://raw.githubusercontent.com/%s/master/README.md" % repo["Github repo"]
    readme = requests.get(readme_url).text

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
    release = requests.get(release_url, auth = ("danielecook", token)).json()

    if 'assets' in release:
        download_url = release["assets"][0]["browser_download_url"]
        download_count = release["assets"][0]["download_count"]
        release_publish_date = release["assets"][0]["created_at"]
        version = release["tag_name"]
    else:
        break
    

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

    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.exists("u/" + username):
        os.makedirs("u/" + username)
    with open("u/" + username + "/index.html", 'w+') as f:
        f.write(open("author_index.html").read().replace("<AUTHOR>", username))
    post_filename = "_posts/" + username + "/" + date_submitted + "-" + title + ".md"
    with open(post_filename,'w') as f:
        output = front_matter + readme.encode('utf-8').strip()
        # Identify media and fetch!
        for i in re.findall("\!\[([^\]])+]\(([^)]+)\)", output):
            "https://raw.githubusercontent.com/%s/master/README.md" % repo["Github repo"]
            requests.get("")
            print i[1]
            #print dir(i)
    
        f.write(output)


