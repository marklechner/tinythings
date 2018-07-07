#!/usr/local/bin/python3

# an unelegant way of checking a list of BOL patterns against a list of strings

import re

strings = ['fb-3259','MS4000','trg-9483','zb-2980','FoO213']
patterns = ['fb','ms','trg']

for i in strings:
  for p in patterns:
    regex = "(^{})(.*)$".format(p)
    match = re.match(regex, i, re.IGNORECASE)
    if match:
      print("{} matched pattern '{}': {}".format(i,p,match.group(1)))
      break