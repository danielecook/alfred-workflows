---
title: alfred-fakeum
layout: post
username: deanishe
categories: utility
description: "Generate fake test data in Alfred"
tags: utility
star_src: "https://ghbtns.com/github-btn.html?user=deanishe&repo=alfred-fakeum&type=star&count=true"
download_url: "https://github.com/deanishe/alfred-fakeum/releases/download/v1.2/Fakeum-1.2.alfredworkflow"
download_count: 101
release_publish_date: 2016-01-28T15:14:19Z
date_submitted: 2016-12-18
forks: 3
stars: 23
watchers: 23
version: v1.2
---
# Alfred Fakeum #

Generate fake test data in Alfred for testing.

![][demo]

## Download ##

Get the workflow from [GitHub][gh-releases] or [Packal][packal].

## Usage ##

- `fake [<query>]` — List/filter available fake data types
    - `↩`, `⌘+C` or `⌘+NUM` — Copy one fake datum to clipboard
    - `⌘+↩` — Paste fake datum into frontmost app
    - `⇥` — Specify number of datasets to copy to clipboard
    - `⌘+L` — Show generated data in Alfred's Large Text window
- `fakeconfig [<query>]` — Activate and deactivate locales for fake data
    - `↩` — Toggle selected locale on or off

If you specify multiple data, e.g. `fake Name ⟩ 10` for 10 names, the data
will be separated by newlines (`\n`).

In the case of `Paragraph` and `Address` types, the data will be separated
by two newlines (`\n\n`).

## Supported data types ##

|          Name         |                                                                                           Example                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name                  | Dr. Venie Mayer DVM                                                                                                                                                                          |
| First Name            | Mercedes                                                                                                                                                                                     |
| Last Name             | Greco                                                                                                                                                                                        |
| Email                 | jan.hettinger@yahoo.com                                                                                                                                                                      |
| Email (corporate)     | kaul.kurt@mitschke.org                                                                                                                                                                       |
| Email (free)          | xpardo@hotmail.com                                                                                                                                                                           |
| Email (safe)          | fabio.pellegrino@example.org                                                                                                                                                                 |
| Email domain (free)   | yahoo.de                                                                                                                                                                                     |
| Address               | C. de Aya Fernandez 34<br/>Palencia, 60850                                                                                                                                                   |
| Street                | Vicolo Rudy 4                                                                                                                                                                                |
| Street Name           | Pasadizo Miranda Rivero                                                                                                                                                                      |
| City                  | Witzenhausen                                                                                                                                                                                 |
| State                 | Almería                                                                                                                                                                                      |
| State abbr.           | TN                                                                                                                                                                                           |
| Country               | Bangladesh                                                                                                                                                                                   |
| TLD                   | net                                                                                                                                                                                          |
| Domain Name           | feeney.net                                                                                                                                                                                   |
| Domain Word           | milani                                                                                                                                                                                       |
| IP Address (IPv4)     | 177.119.72.157                                                                                                                                                                               |
| IP Address (IPv6)     | 4f17:280f:7cdb:0834:dac1:3841:9520:a42f                                                                                                                                                      |
| URI                   | http://greco-piras.org/search.htm                                                                                                                                                            |
| URI path              | app/posts/main                                                                                                                                                                               |
| URL                   | http://www.soeding.de/                                                                                                                                                                       |
| Corporate BS          | orchestrate magnetic eyeballs                                                                                                                                                                |
| Corporate catchphrase | Versatile global productivity                                                                                                                                                                |
| Company               | De luca, Russo e Piras s.r.l.                                                                                                                                                                |
| Company suffix        | LLC                                                                                                                                                                                          |
| Paragraph             | Vitae atque sed soluta vero culpa ut. Vero occaecati quaerat voluptas quidem at et fugit voluptas. Quam est labore vitae consequatur. Facilis deleniti quisquam accusantium quas est magnam. |
| Sentence              | Tempore distinctio quia est nam neque.                                                                                                                                                       |
| Word                  | quia                                                                                                                                                                                         |
| Date                  | 2009-09-11                                                                                                                                                                                   |
| Datetime              | 2014-11-07 10:26:03                                                                                                                                                                          |
| ISO 8601 Datetime     | 1983-08-30T00:44:16                                                                                                                                                                          |
| Time                  | 23:17:05                                                                                                                                                                                     |
| Timezone              | Africa/Porto-Novo                                                                                                                                                                            |
| UNIX timestamp        | 1171262842                                                                                                                                                                                   |




## Supported locales ##

**Note**: Not all locales support all data types.

- Bulgarian
- Czech
- German
- Danish
- Greek
- English (CA)
- English (GB)
- English (US)
- Spanish (ES)
- Spanish (MX)
- Persian
- Finnish
- French
- Hindi
- Italian
- Korean
- Lithuanian
- Latvian
- Dutch
- Polish
- Portuguese (BR)
- Russian
- Slovenian
- Chinese (CN)
- Chinese (TW)

## Licensing, thanks ##

Icons are from [Font Awesome][font-awesome] ([SIL OFL 1.1 Licence][sil]).

Alfred Fakum uses the following libraries:

- [Faker][faker] ([licence][faker-licence])
- [docopt][docopt] ([MIT Licence][mit])
- [Alfred-Workflow][alfred-workflow] ([MIT Licence][mit])

[gh-releases]: https://github.com/deanishe/alfred-fakeum/releases
[packal]: http://www.packal.org/workflow/fakeum
[mit]: http://opensource.org/licenses/MIT
[alfred-workflow]: http://www.deanishe.net/alfred-workflow/
[font-awesome]: http://fortawesome.github.io/Font-Awesome/
[docopt]: http://docopt.org/
[faker]: http://www.joke2k.net/faker/
[faker-licence]: https://github.com/joke2k/faker/blob/master/LICENSE.txt
[sil]: http://scripts.sil.org/OFL
[demo]: https://raw.githubusercontent.com/deanishe/alfred-fakeum/master/demo.gif