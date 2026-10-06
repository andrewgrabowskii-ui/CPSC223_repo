# Name: Andrew Grabowski
# Student ID: 878218254
# Section: 07
# Assignment: Module 5 Assignment 3

triviabank_dict = {}
print("Welcome to the trivia builder 3000")
trivia_poll_active = True
while trivia_poll_active:
    invalid_answer = True
    while invalid_answer:
        question_str = input("Enter the next question: ")
        if question_str == "":
            print("You did not enter a question, let's try again.")
        else:
            invalid_answer = False
    if question_str == "Done":
        trivia_poll_active = False
        continue
    else:
        answer_str = input("Enter the correct answer for that question: ")
        triviabank_dict[question_str] = answer_str
        question_str = ""

print("We will stop entering questions now")
print("Here is the final trivia dictionary:")
for question, answer in triviabank_dict.items():
    print(f"The question is: {question}")
    print(f"And the answer is: {answer}")