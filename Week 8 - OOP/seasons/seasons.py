import sys
import re
from datetime import date
import inflect


def main():

    p = inflect.engine()

    # get input and make sure it's correct
    d = check_input(input('Date of Birth: '))

    # Convert minutes into words and print
    words = p.number_to_words(convert(d), andword="")
    print(f'{words.capitalize()} minutes')

def convert(user_date):

    today = date.today()

    # subtract user's input from today's date, convert difference into minutes and return it
    diff = today - user_date
    diff_in_minutes = diff.days * 24 * 60
    return diff_in_minutes


def check_input(d):

    # Check with regex pattern correct date format and group (YYYY)-(MM)-(DD)
    date_format = re.search('^([0-9]{4})-([0-9]{2})-([0-9]{2})$', d)

    if not date_format:
        sys.exit('Invalid date')

    # input is correct, change into a date object
    d_obj = date(int(date_format.group(1)), int(date_format.group(2)), int(date_format.group(3)))

    return d_obj



if __name__ == '__main__':
    main()
