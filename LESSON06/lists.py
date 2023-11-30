users = ['Jackson', 'Kathleen', 'Jasson']

data = ['Jackson', 30, True]

emptylist = []

print("Jackson" in users)

print(users[0])
print(users[-1])  # to find last value in list

print(users.index('Kathleen'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(users))

users.append('Edgar')
print(users)

users += ['Roxy']
print(users)

users.extend(['Amira', 'Zara'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Miranda')
print(users)

users[2:2] = ['Eddie', 'Alex']
print(users)

users[1:3] = ['Sarah', 'Rahul']
print(users)

users.remove('Rahul')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ['jackson']
users.sort()
print(users)

# needs this key in order to sort lowercase with uppercase
users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()  # Flips the list/array
print(nums)

# nums.sort(reverse=True)  # sorts in descending order
# print(nums)

print(sorted(nums, reverse=True))  # This does not modify the original
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# Tuples
mytuple = tuple(('Jackson', 30, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Kathleen')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))
