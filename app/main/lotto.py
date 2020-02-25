import numpy as np
import scipy.stats as stats
import random
from app.main.lotto_webcrawling import lotto_webcrawling

def lotto():
    arr = lotto_webcrawling()

    _dic = {}
    for i, v in enumerate(arr):
        _dic[i + 1] = v
    _dic = dict(sorted( _dic.items(), key=lambda k: k[1]))
    std_stats = sorted(stats.zscore(arr))

    _result = ''
    n = 5

    for i in range(n):
        lotto = []
        _c = 0
        while _c < 7:
            if _c == 6:
                lotto = sorted(lotto)
            _tmp = random.gauss(np.mean(std_stats), np.std(std_stats))
            for k in range(len(std_stats) - 1):
                if _tmp >= std_stats[k] and _tmp < std_stats[k + 1]:
                    if not(list(_dic.keys())[k] in lotto):
                        lotto.append(list(_dic.keys())[k])
                        _c += 1
                        break

        # 출력 : [random]
        for _ in lotto:
            _result += '{:02d} '.format(_)
        _result = _result[:-1] + '<br/>'
    return _result