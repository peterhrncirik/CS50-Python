import random

def main():

    lvl = get_level()

    # Game state controllers
    round_number = 1
    correct_answers = 0
    tries = 0
    still_incorrect = 0

    # Start the game
    while round_number <= 10:

        # Get random numbers (x and y) for the exercise
        x, y = generate_integer(lvl)
        test = x + y

        # Get answer
        answer = input(f'{x} + {y} = ')

        if answer.isnumeric() and int(answer) == test:
            round_number += 1
            correct_answers += 1
        else:
            print('EEE')
            round_number += 1
            still_incorrect = 1
            tries += 1

            # Answer incorrect, start loop to ask again until 3 times or correct answer
            while still_incorrect == 1:

                answer = input(f'{x} + {y} = ')

                if answer.isnumeric() and int(answer) == test:
                    still_incorrect = 0
                    tries = 0

                tries += 1
                print('EEE')

                if tries == 3:
                    print(f'{x} + {y} = {test}')
                    tries = 0
                    still_incorrect = 0


    print('Score:', correct_answers)



def get_level():

    while True:

        try:
            n = input('Level: ')

            if not n.isnumeric() or int(n) <= 0 or int(n) > 3:
                continue

        except ValueError:
            pass

        return int(n)


def generate_integer(lvl):

    if lvl == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif lvl == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif lvl == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y


if __name__ == '__main__':
    main()
