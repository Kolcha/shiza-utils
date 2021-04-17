simple Python package to download torrent files from http://shiza-project.com/

```python
import shiza.session
import shiza.download

s = shiza.session.login('email@example.com', 'password')
ts = shiza.download.download_torrents('http://shiza-project.com/releases/view/492', s)
shiza.session.logout(s)

for name, data in ts:
    with open(name, "wb") as f:
        f.write(data)
```
