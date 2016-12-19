---
title: alfred-wikipedia
layout: post
username: rshkv
categories: search
description: "Alfred workflow for Wikipedia"
tags: wikipedia
star_src: "https://ghbtns.com/github-btn.html?user=rshkv&repo=alfred-wikipedia&type=star&count=true"
download_url: "https://github.com/rshkv/alfred-wikipedia/releases/download/v1.5/wikipedia.alfredworkflow"
download_count: 3
release_publish_date: 2016-09-17T16:37:05Z
date_submitted: 2016-12-18
forks: 0
stars: 1
watchers: 1
version: v1.5
---
# Wikipedia for Alfred 3
Search the Wikipedia with Alfred.


![Alfred wikipedia preview](https://www.dropbox.com/s/xe4opc8cj6rz07h/alfred-wikipedia.png?dl=1)

## Usage
Use `w` as keyword. Use `w de. '...'` to set the language.

Keys              | Action
----------------- | ------
`↩`               | Open Wikipedia article
`⌘ + ↩`           | Open mobile version of article
`⌃ + ↩`           | Open DBpedia page of article
`⌘ + Y` or `⇧, ⇧` | Open article in Quicklook

## Variables
- Set `maxHits` to change the number of results (default: 9, maximum: 50).
- Set `defaultLang` to change the [language](https://meta.wikimedia.org/wiki/List_of_Wikipedias) (`de`, `fr`, `ru`, ...) of the Wikipedia (default: `en`).

## Credits
This workflow sends requests with Kenneth Reitz's [Requests library](http://python-requests.org) to the [MediaWiki API](https://mediawiki.org/wiki/API:Main_page). Thanks.