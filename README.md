# About
My implementation of algorithms and data structures for learning and use in programming problems. This is not production-ready code.

Data structures are in the ds folder.

The following is a summary of the implemented algorithms and data structures and their complexities.



# Algorithms

## Array
Op | Worst  | Average | Space (aux) | Notes
-- | ------ | ------- | ----------- | -----
Count Inversions | O(n logn) | . | O(n) | .
Longest Common Subsequence | O(m * n) | . | O(m * n) | if just the size of the subseq, then space is O(min(m, n))
Longest Increasing Subsequence | O(n logn) | . | O(n) | .
Longest Subarray Satisfying Sum Bound | O(n) | . | O(n) | can be adapted to find longest/shortest segments satisfying sum or avg constraint; Chen and Chao's algorithm
Maximum Subarray | O(n) | . | O(1) | contiguous subarray (substring) of A with the largest possible sum; Kadane's algorithm
Monotonic Stack | O(n) | . | O(n) | e.g. find next greater for each element, find previous smaller for each, ...
Next Permutation | O(n) | . | . | generates next permutation in lexicographic order
Quick Select | O(n^2) | O(n) | O(log n) | randomized quickselect algorithm; square when poorly chosen pivots

## Bitwise
Op | Worst  | Average | Space (aux) | Notes
-- | ------ | ------- | ----------- | -----
Count Set Bits | O(bits) | . | O(1) | Kernighan's algorithm
Find Single Duplicate Number in Sequence | O(n) | . | O(1) | XOR
Find Single Missing Number in Sequence | O(n) | . | O(1) | XOR
Find Two Missing Numbers in Sequence | O(n) | . | O(1) | XOR
Swap Without Extra Space | O(1) | . | 0 | XOR swap; not applicable in Python

## Graph
Op | Worst  | Average | Space (aux) | Notes
-- | ------ | ------- | ----------- | -----
Breadth-First Search | O(V + E) | . | O(V) | .
Depth-First Search | O(V + E) | . | O(V) | .
Find Connected Components | O(V + E) | . | O(V) | uses BFS
Find Strongly Connected Components | O(V + E) | . | O(V) | Kosaraju's algorithm whose simplicity is offset by its need for two DFS passes
Is Cyclic Graph? | O(V + E) | . | O(V) | just looks for back edges during DFS
Is Two Colorable? | O(V + E) | . | O(V) | uses BFS
Topological Sort | O(V + E) | . | O(V) | uses DFS

## Optimization
Op | Worst  | Average | Space (aux) | Notes
-- | ------ | ------- | ----------- | -----
0-1 (Binary) Knapsack | O(nW) | . | O(nW) | .
Activity Selection Problem (unweighted) | O(n) | . | O(n) | .

## Parsing
Op | Worst  | Average | Space (aux) | Notes
-- | ------ | ------- | ----------- | -----
Infix to Postfix Expression (Shunting Yard) | O(n) | . | O(n) | .
Parse Postfix Expression | O(n) | . | O(n) | transform expression into an AST

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

## String
### Z-algorithm
Op | Worst  | Average | Space (aux) | Notes
-- | ------ | ------- | ----------- | -----
Build Z Array | O(n) | . | O(n) | for a string S, find the longest prefix-substring at each index of S
Count Distinct Substrings | O(n^2) | . | O(n) | .
Find All Matches | O(n + m) | . | O(n + m) | n = len(text) and m = len(pattern)



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

### Merge Lists
Op | Worst  | Average | Space (aux) | Notes
-- | ------ | ------- | ----------- | -----
K-way merge | O(n lgk) | . | O(n) | prefer the heap impl


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
