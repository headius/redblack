$:.unshift(File.expand_path(File.dirname(__FILE__) + "/../../lib"))

require 'red_black_tree'

def rbt_bm
  n = 100000
  a1 = []; n.times { a1 << rand(999_999) }
  a2 = []; n.times { a2 << rand(999_999) }
  start = Time.now

  n = 100_000

  tree = RedBlackTree.new

  n.times {|i| tree.add(i) }
  n.times { tree.delete(tree.root) }

  tree = RedBlackTree.new
  a1.each {|e| tree.add(e) }
  a2.each {|e| tree.search(e) }
  tree.inorder_walk {|key| key + 1 }
  tree.reverse_inorder_walk {|key| key + 1 }
  n.times { tree.minimum }
  n.times { tree.maximum }

  return Time.now - start
end

N = (ARGV[0] || 5).to_i

N.times do
  puts rbt_bm
end
