import re

url_re = re.compile(r"^https?:\/\/shiza-project\.com\/releases\/view\/(\d+)\/?$")


def generate_url(release_id):
    return f"http://shiza-project.com/releases/view/{release_id}"


def parse_id(url):
    return int(url_re.match(url).group(1))
