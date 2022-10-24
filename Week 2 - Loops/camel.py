import re

camel_case = input('camelCase: ')

# find upper case letters
words_list = re.findall('[a-zA-Z][^A-Z]*', camel_case)

# lower upper case letters
words = [letter.lower() for letter in words_list]

# join with underscore to create snake_case
snake_case = '_'.join(words)

print(f'snake_case: {snake_case}')
