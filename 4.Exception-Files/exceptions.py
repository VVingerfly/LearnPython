# Exceptions
# ImportError
# IndexError
# NameError
# SyntaxError
# TypeError
# ValueError

print("_________________________ Test 1 _________________________")
try:
    num1 = 7
    num2 = 0
    print(num1/num2)
    print("Done calculation!")
except ZeroDivisionError:
    print("An error occured")
    print("due to zero division")

print("_________________________ Test 2 _________________________")
try:
    var = 10
    print(var + "ghello")
    print(var / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occured")

print("_________________________ Test 3 _________________________")
try:
    word = "spam"
    print(word / 0)
except:
    print("An error occured")


print("_________________________ Test 4  _________________________")
# finally
try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("This code will run no matter what")

print("_________________________ Test 5  _________________________")
print(1)
# raise ValueError
print(2)


print("_________________________ Test 6  _________________________")
name = '123'
# raise NameError("Invalid name!")

print("_________________________ Test 7  _________________________")
try:
    num = 5 / 0
except:
    print("An error occurred")
    raise

