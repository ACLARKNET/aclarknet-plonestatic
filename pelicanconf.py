#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Alex Clark"
SITENAME = u"Alex Clark"
SITEURL = 'http://blog.aclark.net'
DEFAULT_LANG = 'en'
SOCIAL = (
    ('atom feed (Mozilla)', 'http://blog.aclark.net/Mozilla.atom.xml'),
    ('atom feed (Plone)', 'http://blog.aclark.net/Plone.atom.xml'),
    ('atom feed (Python)', 'http://blog.aclark.net/Python.atom.xml'),
    ('GitHub', 'http://github.com/aclark4life'),
    ('Gittip', 'https://www.gittip.com/aclark4life'),
    ('PythonPackages', 'https://pythonpackages.com/user/aclark4life'),
    ('Twitter', 'http://twitter.com/aclark4life'),
)

DEFAULT_PAGINATION = 10

# Default category AKA header configuration
DEFAULT_CATEGORY = "Blog"

# Generate feeds for tags instead of categories
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_RSS = None

# Generate fancy permalinks
ARTICLE_PERMALINK_STRUCTURE = '/%Y/%m/%d/'
# Disable .html
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = "{slug}/index.html"



ARTICLE_URL = ‘/{date:%Y}/{date:%b}/{date:%d}/{slug}/’
ARTICLE_SAVE_AS = ‘/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html’

