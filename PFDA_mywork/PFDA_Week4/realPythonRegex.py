# Regular expressions are a powerful tool for various kinds of string manipulation.
# They are a domain specific language (DSL) that is present as a library in most modern programming languages, not just Python.
# They are useful for two main tasks:
# verifying that strings match a pattern (for instance, that a string has the format of an email address),
# performing substitutions in a string (such as changing all American spellings to British ones).
# In Python, regular expressions are supported by the re module.

# The re module in Python provides with functions that can be used to work with Regular Expressions.
# In Python a regular expression search is typically written as:
# match = re.search(pat, str)
# The re.search() method takes a regular expression pattern and a string and searches for that pattern within the string.

# If the search is successful, search() returns a match object or None otherwise.
# Therefore, the search is usually immediately followed by an if-statement to test if the search succeeded.
# The re.match() method returns a match object if the text matches the pattern. Otherwise, it returns None.
# The re.findall() method returns a list of strings containing all matches.
# The re.split() method splits the string where there is a match and returns a list of strings where the splits have occurred.
# The re.sub() method replaces the matches with a string of your choice.

# The following are some of the most commonly used methods provided by re module:
# re.match() - Determine if the RE matches at the beginning of the string.
# re.search() - Scan through a string, looking for any location where this RE matches.
# re.findall() - Find all substrings where the RE matches, and returns them as a list.
# re.split() - Split the string into a list, splitting it wherever the RE matches.
# re.sub() - Find all substrings where the RE matches, and replace them with a different string.
# re.compile() - Compile a RE into a regular expression object.
# re.finditer() - Find all substrings where the RE matches, and returns them as an iterator.
# re.fullmatch() - Determine if the RE matches the whole string.
# re.escape() - Return string with all non-alphanumerics backslashed.

# The regular expression language is relatively small and restricted, so not all possible string processing tasks can be done using regular expressions.
# There are also tasks that can be done with regular expressions, but the expressions turn out to be very complicated.
# In these cases, you may be better off writing Python code to do the processing; while Python code will be slower than an elaborate regular expression, it will also probably be more understandable.

#Author: Michael Curley
#The examples below are from the realpython website: https://realpython.com/regex-python/

# Import the re module:
import re as re

