#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#AUTHOR = u'stevenix'
AUTHORS = {
        u'stevenix': 'https://mooncitylabs.org'
}
#AUTHOR_URL = 'author/{slug}.html'
SITENAME = u'Siouxland Linux Users Group'
SITEURL = 'http://sluglinux.org'
DELETE_OUTPUT_DIRECTORY = (True)
INDEX_SAVE_AS = 'news.html'

PATH = 'content'

TIMEZONE = 'America/Chicago'
DEFAULT_DATE_FORMAT = '%b %d %Y'

DELETE_OUTPUT_DIRECTORY = False
RELATIVE_URLS = (True)
STATIC_PATHS = (['images', 'extra/favicon.ico', 'extra/robots.txt'])
FAVICON = u'/extra/favicon.ico'
FAVICON_TYPE = u'png'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
THEME = './themes/pelican-chameleon'
MENUITEMS = [
    ('home', '/'),
    ('news', '/news.html'),
    ('meetings', '/pages/meetings.html'),
    ('archives', [
        ('tags', '/tags.html'),
        ('news', '/category/news.html'),
        ('minutes', '/category/minutes.html'),
        ]),
    ('feeds', [
        ('all', '/feeds/all.atom.xml'),
        ('minutes', '/feeds/minutes.atom.xml'),
        ('news', '/feeds/news.atom.xml'),
        ]),
    ('social', [
        ('irc', '/pages/IRC.html'),
        ('mailing list', 'http://groups.google.com/group/sluglinux'),
        ('twitter', 'https://twitter.com/sluglinux'),
        ]),
    ('Search', '002787820322374053553:rxnx0aoei9s'),
    ]

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAGS_SAVE_AS = 'tags.html'

# Social widget
#SOCIAL = (
#    ('Twitter', 'http://twitter.com/sluglinux'),
#    ('Feeds', 'http://sluglinux.org/feeds/atom.xml'),
#)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
