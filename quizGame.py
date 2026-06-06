# list of questions
# store the answers
# randomly pick questions
# ask questions
# see if they are correct
# keep track of the score
# tell the user score


import random

# The trivia database: A list of dictionaries
trivia_bank = [
    {"question": "What is the correct file extension for Python files?", "answer": ".py"},
    {"question": "Which keyword is used to create a function in Python?", "answer": "def"},
    {"question": "What data type is the result of: 10 > 9?", "answer": "bool"},
    {"question": "Which method removes whitespace from the beginning and end of a string?", "answer": "strip"},
    {"question": "How do you start a single-line comment in Python?", "answer": "#"},
    {"question": "What is the output of print(type([]))?", "answer": "list"},
    {"question": "Which built-in function returns the number of items in an object?", "answer": "len"},
    {"question": "What keyword do you use to loop through a set of items?", "answer": "for"},
    {"question": "Which collection is ordered, changeable, and allows duplicate members?", "answer": "list"},
    {"question": "What is the name of Python's default package manager?", "answer": "pip"}
]


random.shuffle(trivia_bank)
correct = 0
for item in trivia_bank:
    print(item["question"])
    guess = input("Your answer: ")

    if guess.lower() == item["answer"].lower():
        print("Correct!")
        correct += 1
    else:
        print(f"Wrong! The answer is {item['answer']}")

    
    print(f"You have answerred correcty {correct} questions")