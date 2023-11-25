name = "Dave"
count = 1

def another():
    color = "blue"
    # must use global keyword to allow modification of original count
    global count 
    count += 1
    print(count)

    def greeting(name):
        nonlocal color # tells our greeting function that it will use color from parent function
        color = "red"
        print(color)
        print(name)
    
    greeting("Dave")

another()