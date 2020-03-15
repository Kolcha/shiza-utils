# -*- coding: utf-8 -*-

import urllib
from lxml import html


def _generate_search_url(query):
    template = "http://shiza-project.com/releases/search?%s"
    return template % (urllib.parse.urlencode({"q": query, "t": ""}))


def _parse_release_id(release):
    return int(release[release.rfind('-')+1:])


def _parse_releases_ids(content):
    tree = html.fromstring(content)
    nodes = tree.xpath('//article[@class="grid-list"]')
    return [_parse_release_id(n.get('id')) for n in nodes]


def _generate_releases_links(ids):
    template = "http://shiza-project.com/releases/view/%d"
    return [template % (i) for i in ids]


def search(query, session):
    r = session.get(_generate_search_url(query))
    if r.status_code != 200:
        return []
    releases = _parse_releases_ids(r.content)
    return _generate_releases_links(releases)
