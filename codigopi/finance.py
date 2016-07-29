#!/usr/bin/env python

import urllib
import re

symbols = ['aapl','spy','googl','nflx']

for name in symbols:
    print re.findall(re.compile('<span id="yfs_l84_%s">(.+?)</span>'%name),urllib.urlopen('http://finance.yahoo.com/q?uhb=uhb2&fr=uh3_finance_vert_gs&type=2button&s=%s'%name).read())
