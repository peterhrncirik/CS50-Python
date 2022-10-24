list = {}

while True:
    try:
        item = input('')

        # Add first count for an item into the dict
        if item not in list:
            list[item] = 1
        # Increase count if already in the dict
        else:
            list[item] += 1

    except EOFError:
        print('')

        for item in sorted(list):
            print(f'{list[item]} {item.upper()}')

        break
