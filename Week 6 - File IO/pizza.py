import sys
import csv
from tabulate import tabulate

# less or more than 1 argument - exit
if len(sys.argv) == 1:
    sys.exit('Too few command-line arguments.')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments.')
# if the file doesn't end with .csv - exit
elif not sys.argv[1].endswith('.csv'):
    sys.exit('Not a CSV file')

menu = []

try:

    with open(sys.argv[1]) as file:

        reader = csv.reader(file)

        # append file to a list
        for line in reader:
            menu.append(line)

    # set the table and print it
    table = menu[1:]
    headers = menu[0]
    print(tabulate(table, headers, tablefmt="grid"))

except FileNotFoundError:
    sys.exit('File does not exist')
