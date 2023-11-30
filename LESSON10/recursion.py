

def add_one(num):

    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)


mynewtotal = add_one(0)
print(mynewtotal)

# Same thing but with a loop instead

# def add_one_new(num):

#     while num < 9:
#         num += 1
#         print(num)
#     else:
#         return num + 1


# mynewtotal = add_one_new(0)
# print(mynewtotal)
