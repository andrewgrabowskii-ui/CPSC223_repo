new_list = ["I", "am", "the,", "very", "model", "of", "a", "modern", "general"]

for word in new_list:
    print(f"This word is: {word}")
    print(f"This word in upper is: {word.upper()}")
    print(f"This word in lower is: {word.lower()}")
    print(f"This word in title is: {word.title()}")
    print(f"The type of word is {type(word)}")

    new_string = "This is an example of a title"
    print(new_string.title())

num_list = list(range(1,100,2))
sum = 0
for n in num_list:
    print(f"The number is {n}")
    sum += n
    print(f"The current sum is {sum}")
print(f"The average value is {sum/ len(num_list)}")