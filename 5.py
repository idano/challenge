#!/usr/bin/env python

import pickle, pprint

fo = open("banner.p")
data = pickle.load(fo)
print data
pprint.pprint(data)
