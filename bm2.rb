require 'red_black_tree'

def bm(arr)
  start = Time.now

  tree = RedBlackTree.new
  arr.each do |x|
    tree.add(x)
  end

  return Time.now - start
end

N = (ARGV[0] || 5).to_i

arr = []
$stdin.each_line {|line| arr << line.to_i }

N.times do
  puts bm(arr)
end
