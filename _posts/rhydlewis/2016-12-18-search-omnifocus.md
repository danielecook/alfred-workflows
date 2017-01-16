---
title: search-omnifocus
layout: post
username: rhydlewis
categories: productivity
description: "Alfred workflow that allows free text searching of OmniFocus tasks"
tags: omnifocus
star_src: "https://ghbtns.com/github-btn.html?user=rhydlewis&repo=search-omnifocus&type=star&count=true"
download_url: "https://github.com/rhydlewis/search-omnifocus/releases/download/v1.2.3/Search.OmniFocus.v1.2.3.alfredworkflow"
download_count: 44
release_publish_date: 2017-01-09T09:32:30Z
date_submitted: 2016-12-18
forks: 5
stars: 70
watchers: 70
version: v1.2.3
---
# Search OmniFocus Alfred Workflow

## What is this?

This is a workflow for [Alfred](http://www.alfredapp.com/) that performs free text searches on [OmniFocus](http://www.omnigroup.com/omnifocus) data.

## Why would I want such a thing?

Well, I want it because I can't quickly search for, say, a task within OmniFocus using OmniFocus' search field. OmniFocus restricts search results to the current perspective or selection. [Other people have noticed this too](https://discourse.omnigroup.com/t/how-to-search-all-content-a-via-changed-perspective/366).

## How to install

[Download the `.workflow` file from the Releases page](https://github.com/rhydlewis/search-omnifocus/releases/).

## How to use

### Searching for tasks

* Search for all tasks within OmniFocus (irrespective of status) with `.s`:

![](search-for-tasks.png)

### Searching for tasks in the Inbox and the Library 

* Search for all tasks within OmniFocus (whether you've processed them or not) with `.se`.

### Searching the inbox

* Search the OmniFocus inbox with `.i`:

![](search-inbox.png)

### Searching for projects

* Search for projects with `.p`:

![](search-for-project.png)

### Searching for contexts

* Search for a specific context with `.c`:

![](search-for-context.png)

or just list all contexts with `.lc`:

![](list-contexts.png)

### Searching for perspectives

* Search for a specific perspective with `.v`:

![](search-for-perspectives.png)

or just list all perspectives with `.lv`:

![](list-perspectives.png)

### Searching for folders

* Search for a specific folder with `.f`:

![](search-for-folders.png)

or just list all folders with `.lf`:

![](list-folders.png)

### Searching for task or projects notes
 
* Search for a specific note in a task or project with `.n`:

![](search-note.png)

* Search for a specific note in a flagged task `.ng`
* Search for a specific note in active task `.na`

### Narrowing results

* Search just for *active* tasks with `.sa`:

![](search-for-active-tasks.png)

or just for *active* projects with `.pa`:

![](search-for-active-projects.png)

* Search all *flagged* tasks with `.g`:
 
![](search-for-flagged-tasks.png)

or for *flagged* and *active* tasks with `.ga`:

![](search-for-flagged-active-tasks.png)

* Show the 10 most recently modified tasks with `.r`:

![](show-recent-tasks.png)

or show the 10 most recently modfified and non-completed tasks or projects with `.ra`:

![](show-recent-active-tasks.png)

## Thanks to...

* [Dean Jackson](https://github.com/deanishe): the [Python library for Alfred workflows](https://github.com/deanishe/alfred-workflow) does most of the heavy lifting. Excellent stuff, thank you.
* [Marko Kaestner](https://github.com/markokaestner): I used the [in-depth workflow](https://github.com/markokaestner/of-task-actions) to provide some insight into how to search Omnifocus.
* [Danny Smith](https://github.com/dannysmith): for providing a new, and quite frankly, much improved workflow icon.