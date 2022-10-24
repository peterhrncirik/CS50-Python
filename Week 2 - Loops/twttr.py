tweet = input('Input: ')
twtt = []

for letter in tweet:
    
    match letter.lower():
        case 'a':
            continue
        case 'e':
            continue
        case 'i':
            continue
        case 'o':
            continue
        case 'u':
            continue

    twtt.append(letter)

print(f'{"".join(twtt)}')
