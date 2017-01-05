"""
Lambda functions are knows as anonymous, are most commonly used
when passing a simple function as an argument to another function.
They can only do things that require a single expression,
usually equivalent to a single line of code.
"""

print("_________________________ Test 1 _________________________")
# named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

# lambda
print((lambda x: x**2 + 5*x + 4)(-4))


