# Write a Python program to work with the the following functions/methods which
# operates on tuples in Python with suitable examples: i) len( ) ii) count( ) iii) index( )
# iv) sorted( ) v) min ( )vi)max( ) vii) cmp( ) viii) reversed( )

t = (5, 3, 8, 6, 3)

print("Tuple:", t)
print("Length:", len(t))
print("Count of 3:", t.count(3))
print("Index of 8:", t.index(8))
print("Sorted:", sorted(t))
print("Min:", min(t))
print("Max:", max(t))

t2 = (5, 3, 8)
print("Comparison:", t == t2)

print("Reversed:", tuple(reversed(t)))