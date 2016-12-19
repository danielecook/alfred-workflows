---
title: alfred-transmit
layout: post
username: deanishe
categories: search
description: "Rapidly search Transmit favourites in Alfred"
tags: ftp ssh
star_src: "https://ghbtns.com/github-btn.html?user=deanishe&repo=alfred-transmit&type=star&count=true"
download_url: "https://github.com/deanishe/alfred-transmit/releases/download/v0.1/Transmit-Favourites-0.1.alfredworkflow"
download_count: 2
release_publish_date: 2016-11-06T22:19:19Z
date_submitted: 2016-12-18
forks: 0
stars: 0
watchers: 0
version: v0.1
---
Alfred Transmit
===============

Rapidly search Transmit favourites in [Alfred][alfredapp].


Usage
-----

- `ftp [<query>]` — View/filter favourites.
    - `↩` — Open favourite in Transmit.


Configuration
-------------

The workflow is pre-configured to use the `Favorites.xml` saved by the non-Mac App Store version of Transmit at `~/Library/Application Support/Transmit/Favorites/Favorites.xml`.

If you bought Transmit from the Mac App Store, you'll need to change the `FAVES_PATH` variable in the workflow configuration sheet to point to your `Favorites.xml` file.


Licencing & thanks
------------------

- [Transmit][transmit] goes without saying.
- The update icon is from the [Material Design Iconic Font][material] ([SIL licence and others][material-licence]) by [Sergey Kupletsky][sergey].
- The [AwGo library][awgo] ([MIT Licence][mit]) takes care of the workflowy stuff.


[alfredapp]: https://www.alfredapp.com/
[awgo]: https://godoc.org/gogs.deanishe.net/deanishe/awgo
[mit]: https://raw.githubusercontent.com/deanishe/alfred-ssh/master/LICENCE.txt
[octicons]: https://octicons.github.com/
[sil]: http://scripts.sil.org/OFL
[material]: https://zavoloklom.github.io/material-design-iconic-font/
[material-licence]: https://zavoloklom.github.io/material-design-iconic-font/license.html
[sergey]: http://twitter.com/zavoloklom
[transmit]: https://panic.com/transmit/