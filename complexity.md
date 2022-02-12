# Algorithms

## Array
Op | Worst  | Average | Space (aux) | Notes
-- | ------ | ------- | ----------- | -----
Count Inversions | O(n logn) | . | O(n) | .
Longest Common Subsequence | O(m * n) | . | O(m * n) | if just the size of the subseq, then space is O(min(m, n))
Longest Increasing Subsequence | O(n logn) | . | O(n) | .
Next Permutation | O(n) | . | . | .

## Optimization
Op | Worst  | Average | Space (aux) | Notes
-- | ------ | ------- | ----------- | -----
0-1 (Binary) Knapsack | O(nW) | . | O(nW) | .
Activity Selection Problem (unweighted) | O(n) | . | O(n) | .



## Sorting

### Comparison Sorting ( Ω(n logn) )

Op | Worst  | Average | Space (aux) | Notes
-- | ------ | ------- | ----------- | -----
Insertion Sort | O(n^2) | . | O(1) | stable, inplace, online, approx. linear for mostly sorted input
Heap Sort | O(n logn) | . | O(1) | .
Merge Sort | O(n logn) | . | O(n) for array; O(1) for linked list | stable, online, parallel
Quick Sort | O(n^2) | O (n logn) | O(log n) | square when poorly chosen pivots

### Linear-time Sorting ( Ω(n logn) )

Op | Worst  | Average | Space (aux) | Notes
-- | ------ | ------- | ----------- | -----
Counting Sort | O(n + k) | . | O(n + k) | not inplace, good when k << n
Radix Sort | O(d * (n + k) ) | . | O(n + k) | d = digits, k = base
Bucket Sort | O(n^2) | O(n) | O(n) | good for values following uniform distribution [0, 1)

# Data Structures

## Hash

### Chaining Hash Table
Op | Worst  | Average | Notes
-- | ------ | ------- | -----
insert | O(1) | O(1) | .
search | O(n) | O(1) | .
delete(key) | O(n) | O(1) | .

## Heap

### Binary min-heap/max-heap

Op | Worst
-- | -------------
build-min-heap | O(n)
insert | O(lg n)
find-min | O(1)
extract-min | O(lg n)
decrease-key | O(lg n)

## List

### Doubly Linked List

Op | Worst
-- | -------------
insert | O(1)
search | O(n)
delete(node) | O(1)
delete(element) | O(n)

## Tree

### Binary Tree

Op | Worst  | Average | Space (aux) | Notes
-- | ------ | ------- | ----------- | -----
Preorder Traversal | O(n) | . | O(n) for stack | nodes w/o parent pointer; algo does not modify tree; iterative
Inorder Traversal | O(n) | . | O(n) for stack | nodes w/o parent pointer; algo does not modify tree; iterative
Postorder Traversal | O(n) | . | O(n) for stack | nodes w/o parent pointer; algo does not modify tree; iterative

### Binary Search Tree (Unbalanced)

Op | Worst  | Average | Space (aux) | Notes
-- | ------ | ------- | ----------- | -----
insert | O(n) | O(log n) | O(1) | complexity depends on insertion order 
search | O(n) | O(log n) | O(1) | complexity depends on insertion order
delete | O(n) | O(log n) | O(1) | complexity depends on insertion order

### Red-Black Tree

Op | Worst  | Space (aux) | Notes
-- | ------ | ----------- | -----
insert | O(log n) | O(1) | .
search | O(log n) | O(1) | .
delete | O(log n) | O(1) | .

### Order Statistic Red-Black Tree (supporting multiple values per key)

Op | Worst  | Space (aux) | Notes
-- | ------ | ----------- | -----
insert | O(log n) | O(1) | properties with O(1) complexity which only propagate changes upwards to the root dont affect the complexity from O(log n) in RB trees
search | O(log n) | O(1) | return the first value associated with keys
searchAll | O(log n) | O(1) | return list with all values for that key
delete | O(log n) | O(1) | .
rank | O(log n) | O(1) | minimum rank considering there can be multiple values (key happens multiple times)
rankRange | O(log n) | O(1) | minimum rank and maximum rank of the key given it can have multiple values
select | O(log n) | O(1) | .
