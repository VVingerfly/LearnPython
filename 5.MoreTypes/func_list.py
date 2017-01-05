"""
"""

print("List slices")
print("_________________________ Test 1 _________________________")
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[0:1])
print(squares[:7])
print(squares[7:])
print(squares[::2])
print(squares[2:8:3])
print(squares[1:-1])
print(squares[::-1])

print("List comprehensions")
# a useful way to quickly creat list whose contents obey a simple rule
# but try to creat a list in a extensive range will result in a MemoryError
print("_________________________ Test 2 _________________________")
cubes = [i**3 for i in range(5)]
print(cubes)
evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

print("List functions")
# all
# any
# enumerate
print("_________________________ Test 3 _________________________")
nums = [55, 44, 33, 22, 11]
if all([i > 5 for i in nums]):
    print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")

for v in enumerate(nums):
    print(v)
