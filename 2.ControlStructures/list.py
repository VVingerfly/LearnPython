__author__ = 'Wei Li'
# -*- coding:utf-8 -*-

# a list is created using square brackets with commas seperating items
words = ["hello", "worlds", "!"]
print("words list : ", words)

empty_list = []
print("empty list ：", empty_list)

number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[2])

# string can be indexed like a list
str = "Hello World."
print("6th char in str : ", str[6])

## List operations
nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)
print(2 in nums)
print(4 in nums)

print("is 4 in ", nums, " ? ", not 4 in nums)
print("is 4 in ", nums, " ? ", 4 not in nums)
print("is 3 in ", nums, " ? ", not 3 in nums)
print("is 3 in ", nums, " ? ", 3 not in nums)

## List functions
# append
nums.append(4)
print(nums)
words = ["hello"]
words.append("world")
print(words[1])
print(words)
# len
print(len(nums))
print(len(words))
# insert
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)
# index: find the first occurrence of a list item and return its index
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
# max / min 
# count: return a count of how many time a item occurs in a list
# remove: remove an object from a list
# reverse: reverses objects in a list


# range
numbers = list(range(10))  
# range function creats a range object,
# this must be converted to a list if you want to use it as one
print(numbers)
numbers = list(range(3, 8))  
print(numbers)
numbers = list(range(5, 20, 2))  
print(numbers)
