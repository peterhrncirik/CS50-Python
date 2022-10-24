answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")

match answer.strip().replace('-', ' ').title():
    case "42" | "Forty Two" | "forty-two" :
        print("Yes")
    case _:
        print("No")
