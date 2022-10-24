import sys
import csv

# Check command-line args
if len(sys.argv) <= 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

# create new variable for input
names = []

try:

    with open(sys.argv[1]) as file:

        reader = csv.DictReader(file)

        for row in reader:

            # split the name into first, last and append to new list
            last, first = row['name'].split(',')
            names.append({'first': first.lstrip(), 'last': last, 'house': row['house']})

except FileNotFoundError:
    sys.exit(f'Could not read {sys.argv[1]}')

# open new file and write into it
with open(sys.argv[2], "w") as file:

    writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
    writer.writeheader()

    # insert into file data - first,last,house
    for line in names:
        writer.writerow({'first': line['first'], 'last': line['last'], 'house': line['house']})
