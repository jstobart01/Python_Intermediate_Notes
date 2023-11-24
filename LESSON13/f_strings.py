person = "Dave"
coins = 3

# basic method
print("\n" + person + " has " + str(coins) + " coins left.")

# %s method
# inserts person and coins in order of %s's
message = "\n%s has %s coins left." % (person, coins)
print(message)

# format method
# This uses the standard index order
message = "\n{} has {} coins left.".format(person, coins)
print(message)
# This flips the position values
message = "\n{1} has {0} coins left.".format(person, coins)
print(message)
# Must use assignment to get this next one to work
message = "\n{person} has {coins} coins left.".format(person=person, coins=coins)
print(message)

player = {'person': 'Dave', 'coins': 3}

message = "\n{person} has {coins} coins left.".format(**player)
print(message)

#################
# f-strings

message = f"\n{person} has {coins} coins left."
print(message)
# Can pass equations
message = f"\n{person} has {2 * 5} coins left."
print(message)
# Can pass methods
message = f"\n{person.lower()} has {2 * 5} coins left."
print(message)
# must wrap string in " " if you plan on using ' ' inside
message = f"\n{player['person']} has {2 * 5} coins left."
print(message)

#####################
# You can pass formatting options
num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 11):
    print(f"\n2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"\n{num} divided by 4.52 is {num / 4.52:.2%}")