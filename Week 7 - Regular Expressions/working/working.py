import re

def main():
    print(convert(input('Hours: ')))

def convert(s):

    # group input into hours/minutes AM/PM
    pattern = '(^([0-9]{0,2}):?([0-9]?[0-9])? (AM|PM))( to )(([0-9]{0,2}):?([0-9]?[0-9]?) (AM|PM))'
    times = re.search(pattern, s)

    if not times:
        raise ValueError()


    # get part of the day for both times
    first_part = times.group(1)
    second_part = times.group(6)

    # Check first part if it's AM or PM and convert accordingly
    hours_first_part, minutes_first_part = convert_am_to_24(first_part) if 'AM' in first_part else convert_pm_to_24(first_part)

    # Check second part if it's AM or PM and convert accordingly
    hours_second_part, minutes_second_part = convert_am_to_24(second_part) if 'AM' in second_part else convert_pm_to_24(second_part)

    return f'{int(hours_first_part):02}:{int(minutes_first_part):02} to {int(hours_second_part):02}:{int(minutes_second_part):02}'

def convert_am_to_24(part):

    # Split into hours, minutes
    s = part.split(' ')
    hours = 0
    minutes = 0

    if ':' in s[0]:
        hours, minutes = s[0].split(':')
    else:
        hours = s[0]

    # Check hours correctness
    if not check_hours(hours):
        raise ValueError('Wrong Time (Hours)')

    # Check minutes correctness
    if not check_minutes(minutes):
        raise ValueError('Wrong Time (Minutes)')

    if int(hours) == 12:
        hours = 0

    return hours, minutes



def convert_pm_to_24(part):

    # Split into hours, minutes
    s = part.split(' ')
    hours = 0
    minutes = 0

    if ':' in s[0]:
        hours, minutes = s[0].split(':')
    else:
        hours = s[0]

    # Check hours correctness
    if not check_hours(hours):
        raise ValueError('Wrong Time (Hours)')

    # Check minutes correctness
    if not check_minutes(minutes):
        raise ValueError('Wrong Time (Minutes)')

    match int(hours):
        case 1:
            hours = 13
        case 2:
            hours = 14
        case 3:
            hours = 15
        case 4:
            hours = 16
        case 5:
            hours = 17
        case 6:
            hours = 18
        case 7:
            hours = 19
        case 8:
            hours = 20
        case 9:
            hours = 21
        case 10:
            hours = 22
        case 11:
            hours = 23
        case 12:
            hours = 12

    return hours, minutes

# Functions that check hours and minutes correctness
def check_hours(h):

    if int(h) <= 0 or int(h) > 12:
        return False

    return True

def check_minutes(m):

    # Make sure minutes are between 0-59
    if int(m) < 0 or int(m) > 59:
        return False

    return True


if __name__ == '__main__':
    main()
