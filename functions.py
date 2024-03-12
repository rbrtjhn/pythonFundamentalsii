# functions
# - consists of function name, parameters
# - start "def" keyword.
# - Optimizes and make a block of reuseable.

# void function
def averageOfThreeNumbers(num1, num2, num3):
    #codes...
    average = (num1 + num2 + num3) / 3
    print("Average: ", average)

# SHORTCUT FOR COPYING HIGHLIGTED/SINGLE LINE: alt + shift + arrow down/up
# SHORCUT FOR REPOSITIONING HIGHLIGTED/SINGLE LINE:

# averageOfThreeNumbers(89, 76, 81)
# averageOfThreeNumbers(89, 76, 81)
# averageOfThreeNumbers(89, 76, 81)

# return function
title = "Ang Alamat ni Berto"
title2 = ": Bagsakan Era"

def stringToTitle(title):
    return title.title()

def stringToUppercase(message):
    return message.upper()

def stringToLowercase(message):
    return message.lower()

def joinString(message, message2):
    return message.join(message2)

def countLetters(message):
    return len(message)

print(stringToTitle(title))
print(stringToUppercase(title))
print(stringToLowercase(title))
#print(joinString(title, title2))
print(countLetters(title))