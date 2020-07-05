num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (*, /, +, -): ")

if operator == "+":
    print(num2+num1)
elif operator == "-":
    print(num2-num1)
elif operator == "/":
    print(num2/num1)
elif operator == "*":
    print(num2*num1)
else:
    print("Invalid operator. Please use /, *, +, -")


# Dictionaries, allow us to store information in key value pairs.
monthConversions = {
    "Jan": "January",
    2: "February",
    "Mar": "March",
    4: "April",
    "May": "May",
    6: "June",
    "Jul": "July",
    8: "August",
    "Sep": "September ",
    10: "October",
    "Nov": "November",
    12: "December",
}
print(monthConversions["Nov"])
print(monthConversions.get(8))

# While loop
i = 1
while i <= 10:  # Condition: while loop/loop guard
    print(i)
    i += 1

print("Done with the loop")

# Building a guessing game
secretWord = "giraffe"
guess = ""
guessCount = 0
guessLimit = 2
outOfGuesses = False

while guess != secretWord and not outOfGuesses:
    if guessCount < guessLimit:
        guess = input("Enter your guess of what the secret word is: ")
        guessCount += 1
    else:
        outOfGuesses = True
if outOfGuesses:
    print("You are out of guesses. Sorry you suck!")
else:
    print("You are a winner, and you do not suck!")

# For loop
fish = ["Iwana", "Amago", "Yamame", "Golden Trout", "Cutthroat Trout", "Rainbow Trout", "Brown trout"]
len(fish)

for fish in fish:
    print(fish)

for index in range(3, 5):
    print(fish)

for index in range(len(fish)):
    print(fish[index])
