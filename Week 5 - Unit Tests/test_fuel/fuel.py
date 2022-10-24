def main():

    while True:

        try:
            fr = input('Fraction: ')
            # numbers = fr.split('/')
            # x, y = numbers

            # if int(y) == 0 or int(x) > int(y):
            #     continue

            g = convert(fr)
            break

        except (ValueError):
            pass

    print(gauge(g))

def convert(fraction):


    numbers = fraction.split('/')
    x, y = numbers

    try:

        if int(y) == 0 or int(x) > int(y):
            raise ValueError()

        return round((int(x) / int(y)) * 100)
    except (ValueError, ZeroDivisionError):
        pass



def gauge(percentage):

    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'



if __name__ == '__main__':
    main()
