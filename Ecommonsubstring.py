"""
Define a function commonsubstring that takes a list of DNA strings as an input.

-First the function should check if all strings in the list are valid DNA strands (use the function defined in the 1st part). If it's not, return "error".

-If all strings in the list are valid, the function then finds the longest nucleotide substring that is in all of the strings in the list and returns it as a list. If multiples such strings exist, the function should include them all in the returned list.

For example,
commonsubstring("ACGCT", "CGCCA", "ATTACGCT") should return ["CGC"]
"""
from Antcheck import isDNA

def shared(find, items):
  for s in items:
    if not find in s:
      return ""
  return find


def commonsubstring(dnalist):
  for st in dnalist:
    if not isDNA(st):
      return "error"
  dnalist.sort(key=len)
  short = dnalist[0]
  dnalist.pop(0)
  great = 0
  final = []
  for p in range(1, len(short)+1):
    for i in range(len(short)):
      test = short[:len(short)-i]
      if len(test) < great:
        break
      coms = shared(test, dnalist)
      if len(coms) > great:
        final = [coms]
        great = len(coms)
        break
      if len(coms) == great and len(coms) > 0:
        final.append(coms)
        break
    short = short[1:]
  final = list(set(final))
  return final












