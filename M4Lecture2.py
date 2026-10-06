cities_list = ['los angeles', 'long beach', 'sacramento']
pop_list = [7000000, 500000, 600000]

for index, city in enumerate(cities_list):
    print(f"The city of {city} has a population of {pop_list[index]}")

citties_dict = {
    'los angeles': 7000000, 'long beach': 500000, 'sacramento': 600000
}
print("\n")
      
for city in citties_dict:
    print(f"The city of {city} has a population of {citties_dict[city]}")
for values in citties_dict.values():
    print(f"{values}")

citties_dict['los angeles'] = 7500000
citties_dict['san francisco'] = 6250000

for city, pop in citties_dict.items():
    print(f"The city of {city} has a population of {pop}")

if 'fullerton' in citties_dict:
    print(f"The population of {'fullterton'} is {citties_dict.get('fullteron')}")
else:
    print("fullerton not found")