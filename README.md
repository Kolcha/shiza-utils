simple Python package to download torrent files from https://shiza-project.com/

```python
import shiza

ts = shiza.download_torrents('https://shiza-project.com/releases/fairy-tail-tv-1/')

for name, data in ts:
    with open(name, "wb") as f:
        f.write(data)
```
