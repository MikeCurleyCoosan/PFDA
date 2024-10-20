import re

regex = ".*"
FILENAME = "./data/quiz.txt"

with open(FILENAME, "r") as Quizfile:
    for line in Quizfile:
        match = re.search(regex, line)
        if (match):
            matchline = line
            print(matchline, end="")

regex = "Hello"
with open(FILENAME, "r") as Quizfile:
    for line in Quizfile:
        match = re.search(regex, line)
        if (match):
            matchline = line
            print(matchline, end="")