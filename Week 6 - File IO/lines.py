import sys

# less or more than 1 argument - exit
if len(sys.argv) == 1:
    sys.exit('Too few command-line arguments.')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments.')
# if the file doesn't end with .py - exit
elif not sys.argv[1].endswith('.py'):
    sys.exit('Not a Python file')

data = []

try:
    with open(f'{sys.argv[1]}') as file:

        for line in file:

            # Ignore comments end empty lines
            if line.startswith('#') or line.lstrip().startswith('#') or line.isspace():
                continue

            data.append(line)

except FileNotFoundError:
    sys.exit('File does not exist')


print(len(data))
