import cgi
import lxml.html


def _parse_release_id(link):
    return int(link[link.rfind('/')+1:])


def _parse_torrent_ids(content):
    tree = lxml.html.fromstring(content)
    nodes = tree.xpath('//li/a[@data-toggle="tab"]')
    return [int(n.get('href')[9:]) for n in nodes]


def _generate_torrent_links(release, torrents):
    template = "http://shiza-project.com/download/torrents/%d/%d"
    return [template % (release, tid) for tid in torrents]


def _get_torrent_file_name(headers):
    _, params = cgi.parse_header(headers['Content-Disposition'])
    return params['filename'].encode('latin1').decode('utf-8')


def _download_torrent_file(link, session):
    r = session.get(link)
    filename = _get_torrent_file_name(r.headers)
    return (filename, r.content)


def download_torrents(link, session):
    r = session.get(link)
    if r.status_code != 200:
        return []
    release_id = _parse_release_id(link.rstrip('/'))
    torrent_ids = _parse_torrent_ids(r.content)
    torrent_links = _generate_torrent_links(release_id, torrent_ids)
    return [_download_torrent_file(t, session) for t in torrent_links]
