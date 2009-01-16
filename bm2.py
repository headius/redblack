import sys
import time
import random
from red_black_tree import RedBlackTree
import sys

def bm(arr):
  start = time.time()

  tree = RedBlackTree()
  for x in arr:
    tree.add(x)

  return time.time() - start

if len(sys.argv) > 1:
  n = int(sys.argv[1])
else:
  n = 5

arr = []
for line in sys.stdin:
  arr.append(int(line))

for i in range(0, n):
  print("%02f" % bm(arr))

