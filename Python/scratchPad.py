name = input("Enter your name: ") #Store the users input in a variable named "name"
print("Hello " + name + "!") #Print the completed variable with a string

#A very basic calculator
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + float(num2) #int will convert whole numbers only, it will throw an error with a decimal number. float will work with decimal numbers
print(result)

list = ["Tenkara rod", "Water bottle", "Sleeping bag", "Bug spray", "Baseball hat", "Wading shoes"]
numbers  = [2, 4, 5, 7, 88, 112, 223]

print(list[2:5])#Returns the value in the above list from 2-4
list[5] = "Kebari & tippet"
print(list)

list.extend(numbers)
list.append("Onigiri")#adds the item to the end of the list
list.insert(3, "Fly box")#adds the item to the 3rd spot in the list
list.remove("Water bottle")
#clear() wipes the entire list
#pop()#removes the last item in the list
#sort() prints the list in alphabeticaly or numerically
#reverse() reverses the list order
#copy() copies the list to a new variable

print(list)