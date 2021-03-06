#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Helio Perroni Filho'
SITENAME = u'Home Page of Helio Perroni Filho'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

INDEX_SAVE_AS = 'posts.html'

THEME = 'themes/gum'

# See: https://nosferalatu.com/Pelican.html
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['render_math', 'tag_cloud']

# See: https://github.com/getpelican/pelican-plugins/pull/1094
MATH_JAX = {
    'equation_numbering': 'AMS'
}

MENUITEMS = (
    ('Posts', '/posts.html'),
)

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
         #('Python.org', 'http://python.org/'),
         #('Jinja2', 'http://jinja.pocoo.org/'),
         #('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
          #('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
