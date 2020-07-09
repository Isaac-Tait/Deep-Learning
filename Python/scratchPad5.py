# Try except
try:
    value = 10/0
    number = int(input("Enter a number"))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Incorrect input douchebag")

# Opening files
learning_path = open("scratchPad2.py", "r")  # r = read w = write a = append r+ = read/write

print(learning_path.read())  # .readable will show boolean if the file is readable or not
print(learning_path.readline())  # Reads the first line in the file
print(learning_path.readlines())  # Reads all the lines in the file but puts them inside a list/array

learning_path.close()
