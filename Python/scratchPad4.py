# Exponent functions
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(3, 2))

# 2D list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10]
]

print(number_grid[2][2])
print("It is time to move on to nested for loops!")

# Nested for loop
for row in number_grid:
    for element in row:
        print(element)


# A translator that dislikes vowels and prefers the letter "G"
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))
