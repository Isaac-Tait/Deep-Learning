# Tuples - a structure for storing multiple pieces of information.
# Tuples are immutable = cannot be modified ever.
# A list is denoted by [] However, a tuple is denoted with ().

coordinates = (4, 6, 8, 99, 11, 33, 44)
print(coordinates[3])

# Functions
# Why does Python expect two empty lines?

def say_hi(verse, date):
    print("Hello user your favorite verse is " + verse + " and was bookmarked on " + date)


say_hi("Psalms 150:9", "9/2/2020")


# Python return statement will return the function to the user (get information back from a function).
def cube(num):
    return num*num*num


print(cube(32))


# If Statements:
# I wake up, if I am hungry I eat breakfast. I leave my house.
# If it is cloudy I bring an umbrella - otherwise I bring sunglasses.

is_vegan = False
is_hungry = False

if is_vegan and is_hungry: # Or/And operators
    print("Do not eat honey buttermilk pancakes, but you can eat the veggie tofu")  # Will print if is_vegan is true
elif is_hungry and not is_vegan:
    print("You should be a vegan")
elif is_vegan and not is_hungry:
    print("What did you eat today?")
else:
    print("When you get hungry you should seriously consider your life choices in not being a vegan!")

# Comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(5, 6, 8))
