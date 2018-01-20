#!/usr/bin/env python

import sys

string = sys.argv[1].replace('X','{}')
count = string.count('{}')
for i in range( 2** count):
    print(string.format(*list(format(i,'b').zfill(count))))
