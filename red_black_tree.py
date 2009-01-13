class Node:
  RED = 1
  BLACK = 2
  COLORS = [RED, BLACK]

  def __init__(self, key, color = RED):
    if not color in self.COLORS:
      raise TypeError("Bad value for color parameter (%s)" % color)
    self.color = color
    self.key = key
    self.left = self.right = self.parent = NilNode.instance()

  def __str__(self, level = 0, indent = "   "):
    s = level * indent + str(self.key)
    if self.left:
      s = s + "\n" + self.left.__str__(level + 1, indent)
    if self.right:
      s = s + "\n" + self.right.__str__(level + 1, indent)
    return s
    #return "<Node @key=%s, @color=%s, @left=%s, @right=%s>" % (self.key, self.color, self.left, self.right)

  def is_red(self):
    return self.color == self.RED

  def is_black(self):
    return self.color == self.BLACK

  def is_nil(self):
    return False


class NilNode(Node):
  __instance__ = None

  @classmethod
  def instance(self):
    if self.__instance__ is None:
      self.__instance__ = NilNode()
    return self.__instance__

  def __init__(self):
    self.color = Node.BLACK
    self.key = None
    self.left = self.right = self.parent = None
  
  def is_nil(self):
    return True

class RedBlackTree:
  def __init__(self):
    self.root = NilNode.instance()
    self.size = 0
    
  def __str__(self):
    return ("(root.size = %d)\n" % self.size)  + str(self.root)

  def add(self, key):
    self.insert(Node(key))

  #def del(key):


  def insert(self, x):
    self.__insert_helper(x)

    x.color = Node.RED
    while x != self.root and x.parent.color == Node.RED:
      if x.parent == x.parent.parent.left:
        y = x.parent.parent.right
        if not y.is_nil() and y.color == Node.RED:
          x.parent.color = Node.BLACK
          y.color = Node.BLACK
          x.parent.parent.color = Node.RED
          x = x.parent.parent
        else:
          if x == x.parent.right:
            x = x.parent
            self.__left_rotate(x)
          x.parent.color = Node.BLACK
          x.parent.parent.color = Node.RED
          self.__right_rotate(x.parent.parent)
      else:
        y = x.parent.parent.left
        if not y.is_nil() and y.color == Node.RED:
          x.parent.color = Node.BLACK
          y.color = Node.BLACK
          x.parent.parent.color = Node.RED
          x = x.parent.parent
        else:
          if x == x.parent.left:
            x = x.parent
            self.__right_rotate(x)
          x.parent.color = Node.BLACK
          x.parent.parent.color = Node.RED
          self.__left_rotate(x.parent.parent)
    self.root.color = Node.BLACK

  def delete(self, z):
    if z.left.is_nil() or z.right.is_nil():
      y = z
    else:
      y = self.successor(z)
    if y.left.is_nil():
      x = y.right
    else:
      x = y.left
    x.parent = y.parent

    if y.parent.is_nil():
      self.root = x
    else:
      if y == y.parent.left:
        y.parent.left = x
      else:
        y.parent.right = x

    if y != z: z.key = y.key

    if y.color == Node.BLACK:
      self.__delete_fixup(x)

    self.size -= 1
    return y

  def minimum(self, x = None):
    if x is None: x = self.root
    while not x.left.is_nil():
      x = x.left
    return x

  def maximum(self, x = None):
    if x is None: x = self.root
    while not x.right.is_nil():
      x = x.right
    return x

  def successor(self, x):
    if not x.right.is_nil():
      return self.minimum(x.right)
    y = x.parent
    while not y.is_nil() and x == y.right:
      x = y
      y = y.parent
    return y

  def predecessor(self, x):
    if not x.left.is_nil():
      return self.maximum(x.left)
    y = x.parent
    while not y.is_nil() and x == y.left:
      x = y
      y = y.parent
    return y

  def inorder_walk(self, x = None):
    if x is None: x = self.root
    x = self.minimum()
    while not x.is_nil():
      yield x.key
      x = self.successor(x)

  def reverse_inorder_walk(self, x = None):
    if x is None: x = self.root
    x = self.maximum()
    while not x.is_nil():
      yield x.key
      x = self.predecessor(x)

  def search(self, key, x = None):
    if x is None: x = self.root
    while not x.is_nil() and x.key != key:
      if key < x.key:
        x = x.left
      else:
        x = x.right
    return x

  def is_empty(self):
    return self.root.is_nil()

  def black_height(self, x = None):
    if x is None: x = self.root
    height = 0
    while not x.is_nil():
      x = x.left
      if x.is_nil() or x.is_black():
        height += 1
    return height

  def __left_rotate(self, x):
    if x.right.is_nil():
      raise "x.right is nil!"
    y = x.right
    x.right = y.left
    if not y.left.is_nil(): y.left.parent = x
    y.parent = x.parent
    if x.parent.is_nil():
      self.root = y
    else:
      if x == x.parent.left:
        x.parent.left = y
      else:
        x.parent.right = y
    y.left = x
    x.parent = y

  def __right_rotate(self, x):
    if x.left.is_nil():
      raise "x.left is nil!"
    y = x.left
    x.left = y.right
    if not y.right.is_nil(): y.right.parent = x
    y.parent = x.parent
    if x.parent.is_nil():
      self.root = y
    else:
      if x == x.parent.left:
        x.parent.left = y
      else:
        x.parent.right = y
    y.right = x
    x.parent = y

  def __insert_helper(self, z):
    y = NilNode.instance()
    x = self.root
    while not x.is_nil():
      y = x
      if z.key < x.key:
        x = x.left
      else:
        x = x.right
    
    z.parent = y
    if y.is_nil():
      self.root = z
    else:
      if z.key < y.key:
        y.left = z
      else:
        y.right = z
    
    self.size += 1

  def __delete_fixup(self, x):
    while x != self.root and x.color == Node.BLACK:
      if x == x.parent.left:
        w = x.parent.right
        if w.color == Node.RED:
          w.color = Node.BLACK
          x.parent.color = Node.RED
          self.__left_rotate(x.parent)
          w = x.parent.right
        if w.left.color == Node.BLACK and w.right.color == Node.BLACK:
          w.color = Node.RED
          x = x.parent
        else:
          if w.right.color == Node.BLACK:
            w.left.color = Node.BLACK
            w.color = Node.RED
            self.__right_rotate(w)
            w = x.parent.right
          w.color = x.parent.color
          x.parent.color = Node.BLACK
          w.right.color = Node.BLACK
          self.__left_rotate(x.parent)
          x = self.root
      else:
        w = x.parent.left
        if w.color == Node.RED:
          w.color = Node.BLACK
          x.parent.color = Node.RED
          self.__right_rotate(x.parent)
          w = x.parent.left
        if w.right.color == Node.BLACK and w.left.color == Node.BLACK:
          w.color = Node.RED
          x = x.parent
        else:
          if w.left.color == Node.BLACK:
            w.right.color = Node.BLACK
            w.color = Node.RED
            self.__left_rotate(w)
            w = x.parent.left
          w.color = x.parent.color
          x.parent.color = Node.BLACK
          w.left.color = Node.BLACK
          self.__right_rotate(x.parent)
          x = root
    x.color = Node.BLACK
    
  

if __name__ == "__main__":
  tree = RedBlackTree()
  tree.add(10)
  tree.add(3)
  tree.add(7)
  tree.add(4)
  tree.add(20)
  tree.add(15)

  print tree

  for key in tree.inorder_walk():
    print "key = %s" % key
