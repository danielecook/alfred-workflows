---
title: alfred-reddit
layout: post
username: deanishe
categories: social
description: "Browse Reddit from Alfred"
tags: reddit
star_src: "https://ghbtns.com/github-btn.html?user=deanishe&repo=alfred-reddit&type=star&count=true"
download_url: "https://github.com/deanishe/alfred-reddit/releases/download/v1.4/Reddit-1.4.alfred3workflow"
download_count: 20
release_publish_date: 2016-11-01T15:03:07Z
date_submitted: 2016-12-18
forks: 4
stars: 22
watchers: 22
version: v1.4
---

Reddit for Alfred
=================

Find subreddits and browse hot posts on [Reddit][reddit].

![][demo]


Download
--------

Get Reddit for Alfred from [GitHub][gh-releases] or [Packal][packal-page].

**Note**: Version 1.4 (and above) is *not* compatible with Alfred 2. Please download [v1.3][v13] if you're using Alfred 2.


Usage
-----

- `r/` — Show list of popular subreddits
	- `⇥`, `↩` or `⌘+NUM` — Show 50 hottest posts in selected subreddit
	- `⌘+↩` — Open subreddit in browser
	- `⇧` or `⌘+Y` — Show Quick Look preview of subreddit
- `r/<query>` — Search for subreddits matching `<query>`
    - `⇥` — Show 50 hottest posts in selected subreddit (same as appending `/`)
    - `↩` or `⌘+NUM` — Open subreddit in browser
    - `⇧` or `⌘+Y` — Show Quick Look preview of subreddit
- `r/<subreddit>/[<query>]` — Show 50 hottest posts on subreddit `<subreddit>`, filtered by `<query>` if present
    - `↩` or `⌘+NUM` — Open article in default browser
    - `⌘+↩` — Open Reddit comments in default browser
    - `⌥+↩` — Open article and Reddit comments in default browser
    - `⌘+L` — Show full post title in Alfred's Large Type window
    - `⇧` or `⌘+Y` — Show Quick Look preview of comments page (or post. See [

**Note:** OS X's "delete word" shortcut (`⌥+⌫`) is very handy for backing out of a subreddit.


Description
-----------

A basic workflow to browse subreddits.

The subreddit search, `r/<query>`, uses Reddit's API to search for subreddits that match `<query>`. 25 results are retrieved by default.

The subreddit search can be a bit odd, which is due to the legendary crapness of Reddit's search function.

Search within a subreddit, `r/subreddit/<query>`, only filters the list of hot results. 50 results are retrieved by default.


Configuration
-------------

There is one option, `QUICKLOOK_POST`, in the workflow's configuration sheet (in Alfred Preferences). Set `QUICKLOOK_POST` to `1` for the Quick Look preview to show the article instead of the Reddit comment page.


Licensing, thanks etc.
----------------------

Alfred-Reddit is released under the [MIT Licence][mit].

I found the logo in a [Font Awesome issue][logo-source] on GitHub.

It's heavily based on [Alfred-Workflow][alfred-workflow], also [MIT-licensed][mit].


[reddit]: http://www.reddit.com
[mit]: http://opensource.org/licenses/MIT
[alfred-workflow]: http://www.deanishe.net/alfred-workflow/
[logo-source]: https://github.com/FortAwesome/Font-Awesome/issues/372
[gh-releases]: https://github.com/deanishe/alfred-reddit/releases
[packal-page]: http://www.packal.org/workflow/reddit
[demo]: https://raw.githubusercontent.com/deanishe/alfred-reddit/master/demo.gif
[v13]: https://github.com/deanishe/alfred-reddit/releases/tag/v1.3
