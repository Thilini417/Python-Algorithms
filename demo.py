# Input the three letters
first = input('1st letter: ')
second = input('2nd letter: ')
third = input('3rd letter: ')

# Convert letters to uppercase for case-insensitive comparison
letters = [first.lower(), second.lower(), third.lower()]

# Sort the list
letters.sort()

# The middle letter is the second element in the sorted list
middle = letters[1]

# Print the result
print(f"The letter in the middle is {middle}")