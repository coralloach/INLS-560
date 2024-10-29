import re

animals = ['monkey', 'dog', 'raccoon', 'cat']

pattern = r'o'

for animal in animals:
    if re.search(pattern, animal):
        print(f'{animal.upper()} contains the pattern {pattern}')
    else:
        print(f'The pattern "{pattern}" is not in item {(animals.index(animal))}.')