def squared(num): return num * num
# lambda num : num * num
 
print(squared(2))

addTwo = lambda num : num + 2

print(addTwo(12))

sum = lambda a, b : a + b

print(sum(2, 8))

#####################

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

#######################

lambda num : num * num

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))

####################

odd_nums = filter(lambda num : num % 2 != 0, numbers)

print(list(odd_nums))