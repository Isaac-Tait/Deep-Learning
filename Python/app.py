print("Hello World!")

print("     ^ ")
print("    /|\\")#Double \\ is needed, a single one returns an error
print("   / | \\")
print("  /  |  \\")
print(" /   |   \\")
print("/____|____\\")

character_name = "Petunia"
character_location = "Splenda"

print("There was once a beautiful woman named " + character_name + ", ")
print("she was a princess in the land of " + character_location + ". ")
print(character_name + " did not like living in " + character_location + ", ")#Notice there is no leading + sign on this line
print("but she did like her name " + character_name + ".")

print(len(character_name))
print(character_location[5])
print(character_name.index("e"))
print(character_location.replace("Splenda", "Cane"))

my_num = 360
print(my_num % 7)
print(str(my_num % 7.3) + " is my favorite number")#If you do not use str() to append a number to a string Python will return an error