#Working with regular expressions in Python
#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#RegEx can be used to check if a string contains the specified search pattern.
#Python has a built-in package called re, which can be used to work with Regular Expressions.
#Import the re module:
#Author: Michael Curley 
#The examples below are from the W3Schools website: https://www.w3schools.com/python/python_regex.asp

import re as re

# Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("YES! We have a match!")
else:
    print("No match")

# Return a list containing every occurrence of "ai":

x = re.findall("ai", txt)

print(x)

# Check if "Portugal" is in the string:

x = re.findall("Portugal", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# Split the string at every white-space character:

x = re.split("\s", txt)
print(x)

# Split the string at the first white-space character:	

x = re.split("\s", txt, 1)
print(x)

# Replace all white-space characters with the digit "9":

x = re.sub("\s", "9", txt)
print(x)

# Replace the first two occurrences of a white-space character with the digit 9:

x = re.sub("\s", "9", txt, 2)
print(x)

# Search for an upper case "S" character in the beginning of a word, and print its position:

x = re.search(r"\bS\w+", txt)
print(x.span())

# Search for an upper case "S" character in the beginning of a word, and print the word:

x = re.search(r"\bS\w+", txt)
print(x.group())

# Search for an upper case "S" character in the beginning of a word, and print the word:

x = re.search(r"\bS\w+", txt)
print(x.string)

# Search for an upper case "S" character in the beginning of a word, and print the word:
