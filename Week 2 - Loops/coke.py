amount = 50

# Start the loop
while True:

    coins = int(input('Insert Coin: '))
    
    # Calculate amount based on input - exit loop when amount reaches 0
    if coins == 5 or coins == 10 or coins == 25:
        amount -= coins

    if amount > 0:
        print(f'Amount due: {amount}')

    if amount == 0:
        print(f'Change owed: {amount}')
        break
    if amount < 0:
        print(f'Change owed: {amount * -1}')
        break
