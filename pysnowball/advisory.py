import json
import os
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls


def advisories(symbol, page=1, count=10):
    url = api_ref.advisories_latest+symbol
    url = url + '&count='+str(count)
    url = url + '&page='+str(page)

    return utls.fetch(url)


def news(symbol, page=1, count=10):
    url = api_ref.news_latest+symbol
    url = url + '&count='+str(count)
    url = url + '&page='+str(page)

    return utls.fetch(url)
