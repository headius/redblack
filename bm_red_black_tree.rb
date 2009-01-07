$:.unshift(File.expand_path(File.dirname(__FILE__) + "/../../lib"))

require 'red_black_tree'

def rbt_bm

  start = Time.now

  n = 100_000

  tree = RedBlackTree.new

  n.times { tree.insert(RedBlackTree::Node.new(n)) }
  n.times { tree.delete(tree.root) }

  tree = RedBlackTree.new
  n.times { tree.insert(RedBlackTree::Node.new(rand(100_000))) }
  n.times { tree.search(rand(100_000)) }
  tree.each {|node| node.key + 1 }
  tree.inorder_walk {|node| node.key + 1 }
  tree.reverse_each {|node| node.key + 1 }
  tree.reverse_inorder_walk {|node| node.key + 1 }
  n.times { tree.minimum }
  n.times { tree.maximum }

  return Time.now - start
end

N = (ARGV[0] || 5).to_i

N.times do
  puts rbt_bm
end
