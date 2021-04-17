import urllib
import lxml.html


def _generate_search_url(query):
    template = "http://shiza-project.com/releases/search?%s"
    return template % (urllib.parse.urlencode({"q": query, "t": ""}))


def parse_releases_links(content):
    tree = lxml.html.fromstring(content)
    nodes = tree.xpath('//article[@class="grid-card"]/a[@class="card-box"]')
    return [n.get('href') for n in nodes]


def search(query, session):
    r = session.get(_generate_search_url(query))
    if r.status_code != 200:
        return []
    return parse_releases_links(r.content)
