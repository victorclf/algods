# Algorithms

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

# Data Structures

## Heap

### Binary min-heap/max-heap

Op | Worst
-- | -------------
build-min-heap | O(n)
insert | O(lg n)
find-min | O(1)
extract-min | O(lg n)
decrease-key | O(lg n)
