import re
import requests

_link_re = re.compile(r"^https:\/\/shiza-project\.com\/releases\/([@\w-]+)\/?$")


def match_link(link: str) -> bool:
    return _link_re.match(link) is not None


def _get_torrent_links(slug: str, session: requests.Session) -> list[str]:
    q = """
query fetchRelease($slug: String!) {
    release(slug: $slug) {
        torrents {
            file {
                url
            }
        }
    }
}
"""
    v = {"slug": slug}
    p = {"query": q, "variables": v}
    r = session.post('https://shiza-project.com/graphql', json=p)
    if r.status_code != 200:
        return []
    j = r.json()
    if not j['data']['release']:
        return []
    return [t["file"]["url"] for t in j['data']['release']['torrents'] if t["file"]]


def _get_torrent_file_name(link: str) -> str:
    return link[link.rfind('=')+1:]


def _download_torrent_file(link: str, session: requests.Session) -> tuple[str, bytes]:
    r = session.get(link)
    filename = _get_torrent_file_name(link)
    return (filename, r.content)


def download_torrents(link: str, session: requests.Session = None) -> list[tuple[str, bytes]]:
    m = _link_re.match(link)
    if not m:
        return []
    if not session:
        session = requests.Session()
    torrent_links = _get_torrent_links(m.group(1), session)
    return [_download_torrent_file(t, session) for t in torrent_links]
