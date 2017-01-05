"""
The module itertools is a standard library that containing sevaral functions
that are useful in functional programming.
"""

print("_________________________ Test 1 _________________________")
# One type of function it produces is infinite iterators.
# count: counts up to infinitely from a Value
# cycle: iterates infinitely through an iterable (for instance a list or string)
# repeat: repeats an object, either infinitely or a specific number of times.
from itertools import count

for i in count(3):
    print(i)
    if i >= 6:
        break



print("_________________________ Test 2 _________________________")
# There are many functions in itertools that operate on iterables, in a simliar way to map or filter
# takewhile: take items from an iterable while a predicate function remains true
# chain: combines several iterables into one long one
# accumulate: returns a running total of values in an iterable
from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x <=6, nums)))


print("_________________________ Test 3 _________________________")
# There are also several combinatoric functions in itertool, such as product and permutation
# There are used when you want to accomplish a task with all possible combinations of some items.
from itertools import product, permutations

letters = {"A", "B"}
print(list(product(letters, range(2))))
print(list(permutations(letters)))
