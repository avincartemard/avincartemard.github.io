from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

LOAD_CONTENT_CACHE = False


SITEURL = 'https://avincartemard.github.io/'
AUTHOR = u'Alexandre Vincart-Emard'
SITENAME = 'My Blog'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

MARKUP = ('md', 'ipynb')

DEFAULT_DATE_FORMAT = '%B %d, %Y'

SUMMARY_MAX_LENGTH = 150
DEFAULT_PAGINATION = 3

PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']

PATH = 'content'
THEME = 'theme'

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

#PAGE_SAVE_AS = '{category}/{slug}.html'
#PAGE_URL = PAGE_SAVE_AS

MD_EXTENSIONS = ['codehilite(css_class=codehilite)', 'extra']

# Paths are relative to `content`
STATIC_PATHS = ['images', '404.html', 'robots.txt', 'pdfs', 'favicon.ico', 'datasets']

# THEME SETTINGS
#DEFAULT_HEADER_BG = '/images/station1.jpg'
TWITTER_USERNAME = 'avincartemard'
GITHUB_USERNAME = 'avincartemard'
SHOW_ARCHIVES = True
SHOW_FEED = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
	 ('My Publications', 'https://inspirehep.net/search?ln=en&as=1&m1=a&p1=vincart-emard&f1=author&op1=a&m2=a&p2=&f2=&op2=a&m3=a&p3=&f3=&action_search=Search&dt=&d1d=&d1m=&d1y=&d2d=&d2m=&d2y=&sf=&so=a&rm=&rg=25&of=hb&sf=earliestdate&so=d'),
	 ('arXiv', 'https://arxiv.org'),
         ('Python.org', 'http://python.org/'),
	 ('The Economist', 'https://www.economist.com'),
	 ('Scientific American', 'https://www.scientificamerican.com'),
	 ('Futurism', 'https://futurism.com')
)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/alexandre-vincart-emard-9a7a4497/'),
          ('GitHub', 'https://github.com/avincartemard'))

# PLUGINS SETTINGS
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'ipynb.markup', 'liquid_tags.youtube', 'liquid_tags.b64img']

SITEMAP = {
    'format': 'xml'
}

#IPYNB_EXTEND_STOP_SUMMARY_TAGS = [('h2', None), ('ol', None), ('ul', None)]
IGNORE_FILES = ['.ipynb_checkpoints']

# Custom menu items
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_SUBMENU = True

DEFAULT_CATEGORY = 'Blog'

MENUITEMS = (
    ('About', '/pages/about.html'),
    ('Curriculum Vitae', '/pages/curriculum-vitae.html'),
    ('Tags', '/tags.html'),
    ('Archives', '/archives.html')
    )

# Display the category in the article's info
DISPLAY_CATEGORIES_ON_POSTINFO = False

# Display the author in the article's info
DISPLAY_AUTHOR_ON_POSTINFO = False

# Display the search form
DISPLAY_SEARCH_FORM = False