import re as re


sentence = "The Quick Brown Fox Jumps Over The Lazy Dog"
paragraph = """Once apon a
            time there lived
            3 bears and 1 girl 
            They all owed the bank $1000. 
            Ouch!"""
website = "www.medium.com"

special_characters = "[\^$.|?*+()"

# Split the paragraph at every white-space character:

white = paragraph.split(" ")
print(white)

# Using regex functions to do some things with the sentence, paragraph, website and special_characters given as variables above:


#Matching explicit charachters

pattern = "Quick"

match = re.findall(pattern, sentence)   
print(match)

#Note: This is case sensitive.

pattern = "quick"

match = re.findall(pattern, sentence)
print(match) #This will return an empty list because the pattern is not in the sentence.

#Ignoring case sensitivity

pattern = "quick"

match = re.findall(pattern, sentence, re.IGNORECASE)
print(match)

#We could also use the re.search() function to find the pattern in the sentence.
#This will return a match object if the pattern is found in the sentence. It will tell us where the pattern is found in the sentence.

pattern = "bears"

match = re.search(pattern, paragraph)
print(match)



