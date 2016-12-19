---
title: alfred-stackoverflow
layout: post
username: deanishe
categories: search
description: "Search StackOverflow.com from Alfred"
tags: programming
star_src: "https://ghbtns.com/github-btn.html?user=deanishe&repo=alfred-stackoverflow&type=star&count=true"
download_url: "https://github.com/deanishe/alfred-stackoverflow/releases/download/v1.2/StackOverflow-1.2.alfredworkflow"
download_count: 365
release_publish_date: 2016-03-02T08:09:51Z
date_submitted: 2016-12-18
forks: 3
stars: 37
watchers: 37
version: v1.2
---
# StackOverflow Search for Alfred #

Search for answers on StackOverflow.com from [Alfred 2 & 3][alfred].

![](demo.gif "")

## Download ##

Get StackOverflow for Alfred from [GitHub][gh-releases] or
[Packal][packal-page].

## Usage ##

- `.so <query>` — Search StackOverflow.com for `<query>`.
    See below for syntax.
    - `↩` or ` ⌘+NUM` — Open result in default browser
    - `⌘+L` — Show full question title in Alfred's Large Text window

## Query syntax ##

By default, words in `<query>` will be search for in the title of posts. To
specify a tag, prefix it with `.`, e.g. `python` will search for `python` in
the post title, `.python` will search for the tag `python`.

## Results ##

Answered questions will be shown first in the list of results (and have a
tick on their icon).

## Licensing, thanks ##

This workflow is released under the [MIT Licence][mit].

It is heavily based on [Alfred-Workflow][alfred-workflow], also
[MIT-licensed][mit].


[alfred]: https://www.alfredapp.com/
[mit]: http://opensource.org/licenses/MIT
[alfred-workflow]: http://www.deanishe.net/alfred-workflow/
[gh-releases]: https://github.com/deanishe/alfred-stackoverflow/releases
[packal-page]: http://www.packal.org/workflow/stackoverflow-search
[demo]: https://raw.githubusercontent.com/deanishe/alfred-stackoverflow/master/demo.gif