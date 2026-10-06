words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
frequency = {}

for word in words:
    if word in frequency.keys():
        frequency[word] += 1
    else:
        frequency[word] = 1

for word, count in frequency.items():
    print(f"{word}: {count}")
