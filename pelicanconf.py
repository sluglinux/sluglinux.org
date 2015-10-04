#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'stevenix'
SITENAME = u'Siouxland Linux Users Group'
SITEURL = 'http://sluglinux.org'
DELETE_OUTPUT_DIRECTORY = (True)

PATH = 'content'

TIMEZONE = 'America/Chicago'
DEFAULT_DATE_FORMAT = '%b %d %Y'

RELATIVE_URLS = (True)
STATIC_PATHS = (['images', 'extra/favicon.ico', 'extra/robots.txt'])
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
#THEME = './themes/bootstrap'
THEME = './themes/new-bootstrap2'
MENUITEMS = (
        ('meetings', '/pages/meetings.html'),
        ('contact', '/pages/contact.html'),
)

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAGS_SAVE_AS = 'tags.html'

# Blogroll
#LINKS =  (
#    ('Mailing List', 'https://groups.google.com/forum/#!forum/sluglinux'),
#    ('Wiki', 'http://www.sluglinux.org/wiki/Main_Page'),
#)

# Social widget
#SOCIAL = (
#    ('Twitter', 'http://twitter.com/sluglinux'),
#    ('Feeds', 'http://sluglinux.org/feeds/atom.xml'),
#)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
