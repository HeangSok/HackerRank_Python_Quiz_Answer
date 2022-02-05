# Task
# You are given two arrays: A and B.
# Your task is to compute their inner and outer product.

# Sample Input

# 0 1
# 2 3
# Sample Output

# 3
# [[0 0]
#  [2 3]]

# Answer: 
import numpy

A = numpy.array(input().split(), dtype=int)
B = numpy.array(input().split(), dtype=int)

print(numpy.inner(A, B))
print(numpy.outer(A, B))
