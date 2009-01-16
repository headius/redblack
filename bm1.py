import sys
import time
import random
from red_black_tree import RedBlackTree
import sys

minor = sys.version_info[0]
if minor >= 3:
  xrange = range

def rbt_bm():
  n = 100000
  a1 = [random.randint(0, 999999) for x in xrange(0, n)]
  a2 = [random.randint(0, 999999) for x in xrange(0, n)]

  start = time.time()

  tree = RedBlackTree()

  for i in xrange(0, n):
    tree.add(i)
  for i in xrange(0, n):
    tree.delete(tree.root)

  tree = RedBlackTree()
  for x in a1:
    tree.add(x)
  for x in a2:
    tree.search(x)
  for key in tree.inorder_walk():
    key + 1
  for key in tree.reverse_inorder_walk():
    key + 1
  for i in xrange(0, n):
    tree.maximum()
  for i in xrange(0, n):
    tree.minimum()

  return time.time() - start

if len(sys.argv) > 1:
  n = int(sys.argv[1])
else:
  n = 5

for i in xrange(0, n):
  print("%02f" % rbt_bm())

