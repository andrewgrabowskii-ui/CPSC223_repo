student1_dict = {
    'name': 'Jim Bob',
    'id': 123456,
    'schedule': ['CPSC223p', 'ENG1', 'MATH2']
    }

for myclass in student1_dict.get('schedule'):
    print(f"The class is {myclass}")