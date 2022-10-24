months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:

    try:
        user_input = input('Date: ')

        if '/' in user_input:
            date_list = user_input.strip().split('/')
            month = int(date_list[0])
            day = int(date_list[1])

            if (month >= 1 and month <= 12) and (day >=1 and day <= 31):
                print(f'{date_list[2]}-{month:02}-{day:02}')
                break
            else:
                continue
        elif ',' in user_input:
            date_list = user_input.strip().split(' ')
            day = int(date_list[1].replace(',', ''))

            if (date_list[0] in months) and (day >= 1 and day <= 31):
                month = months.index(date_list[0]) + 1
            else:
                continue

            print(f'{date_list[2]}-{month:02}-{day:02}')
            break

    except ValueError:
        pass

    except EOFError:
        print('')
        break
