# Boolean Operation - True, False, if, elif, else, &(and), |(or), ~(not)

# True, False

# if, elif, else

# if True:
#     print("It's true")

# if False:
#     print("It's false")


num = 5
print("Num is ", num)
if num == 0:
    print("It's 0!")
elif num == 1:
    print("It's 1!")
else: 
    print("I don't know.")

# and
if False and False:
    print("It's False.")

# or
if True or False: 
    print("It's definitely something.")
else:
    print("It's false.")

# not
if not False:
    print("It's true!")
if not True:
    print("It's False!")

# comparision == !=

# operators += -= *= /= %= //= **=

# switch (match) statements

color = "blue"

if color == "red" or color == "pink":
    print("It's reddish")
else:
    print("It's not reddish")