responses = {}
polling_active = True
while polling_active:
    name = input(f"What is your name? ")
    if name == 'done':
        polling_active = False
    else:
        subject = input(f"What is your favorite subject? ")
    responses[name] = subject

print("\nPoll Results:")
for name, subject in responses.items():
    print(f"{name}: {subject}")