
print("_________________________ Test 1 _________________________")
print(1)
assert 2 + 2 == 4
print(2)
# assert 1 + 1 == 3
print(3)

print("_________________________ Test 2 _________________________")
temp = -10
# assert (temp >= 0), "Colder than absolute zero!"

print("_________________________ Test 3 _________________________")
def func(x):
    assert x > 0, "Error"
    print(x)

func(4)
func(-5)
