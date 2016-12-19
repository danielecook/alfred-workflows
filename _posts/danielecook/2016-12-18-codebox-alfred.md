---
title: codebox-alfred
layout: post
username: danielecook
categories: snippets
description: "An alfred workflow for accessing codebox snippets."
tags: codebox
star_src: "https://ghbtns.com/github-btn.html?user=danielecook&repo=codebox-alfred&type=star&count=true"
download_url: "https://github.com/danielecook/codebox-alfred/releases/download/0.1/Codebox-Alfred.alfredworkflow"
download_count: 40
release_publish_date: 2015-06-17T22:19:44Z
date_submitted: 2016-12-18
forks: 0
stars: 4
watchers: 4
version: 0.1
---
# codebox-alfred

An alfred workflow for accessing codebox snippets.

### [Download the latest version](https://github.com/danielecook/codebox-alfred/releases)

## Important!

The workflow works fairly well, but there are a few caveats. You should not do the following with your codebox libraries:

* Don't put spaces into tag, list, or folder names. Use an underscore instead. I could have allowed spaces, but it would have made the alfred commands a lot messier (folders, tags, and lists would have to of been quoted). 
* Don't nest folders/lists with the same name. 

## Usage

__Set the codebox source using `cb_src`__

![set source](img/set_src.png)

__Invoke the workflow by typing `ff`__

![search directory](img/browse_directory.png)

__Browse tags with `ff #<search>`__
![search tags](img/search_tags.png)

__Search all Snippets: `ff <search>`__

![search all](img/search_snippets.png)