num_list = list(range(0,100))

print(num_list)

print(num_list[2:9])
print(num_list[2:])
print(num_list[:9])
new_list = num_list[:]
new_list[0] *= 2
new_list[1] *= 2
new_list[2] *= 2

print(f"The original list is:")
print(num_list)
print(f"The new list is:")
print(new_list)

print(num_list[5:-2])