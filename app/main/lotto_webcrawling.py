from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from pprint import pprint

def lotto_webcrawling
    html = urlopen('https://dhlottery.co.kr/gameResult.do?method=statByNumber')
    obj = bs(html, 'html.parser')
    arr = []

    _tmp = obj.body.find('table', {'id': 'printTarget'}).find_all('td')
    for v in _tmp:
        for _v in v.contents:
            try:
                arr.append(int(_v))
            except TypeError:
                pass
            except ValueError:
                pass
    return arr