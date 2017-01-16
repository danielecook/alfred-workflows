---
title: alfred-resolve-url
layout: post
username: deanishe
categories: search
description: "Alfred workflow to resolve HTTP redirects and return the canonical URL"
tags: search
star_src: "https://ghbtns.com/github-btn.html?user=deanishe&repo=alfred-resolve-url&type=star&count=true"
download_url: "https://github.com/deanishe/alfred-resolve-url/releases/download/v1.4/Resolve.URL-1.4.0.alfredworkflow"
download_count: 10
release_publish_date: 2015-03-17T20:20:42Z
date_submitted: 2016-12-18
forks: 2
stars: 5
watchers: 5
version: v1.4
---
Resolve HTTP Redirects in Alfred
================================

Follows any HTTP redirects and returns the canonical URL. Also displays information about the primary host (hostname, IP address(es), aliases).

![](https://raw.githubusercontent.com/deanishe/alfred-resolve-url/master/demo.gif "demo.gif")

You can paste a URL into Alfred's query box or grab a URL directly from the
clipboard. If the URL contains no scheme (`http://`, `https://`, etc.),
`http://` will be assumed.

## Usage ##

- `resolve URL` — Find and display the canonical URL after all redirects.
	+ `↩` — Open the new URL in your default browser
	+ `⌘+↩` — Copy the new URL to the clipboard
- `resolvepb` — Grab the URL from the clipboard and resolve any redirects as above.

If the URL has no redirects, a "URL is canonical" message will be displayed.

## Licence, thanks ##

This workflow is released under the [MIT licence](http://opensource.org/licenses/MIT). It uses [Alfred-Workflow](http://www.deanishe.net/alfred-workflow/index.html) for the plumbing and to resolve HTTP redirects.