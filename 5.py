#!/usr/bin/env python

import pickle, pprint

fo = open("banner.p")
data = pickle.load(fo)

for i in data:
    for j in i:
        for k in range(j[1]):
            print j[0],
    print ""

