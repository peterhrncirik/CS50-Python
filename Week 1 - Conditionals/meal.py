def main():
    time = input("What Time is it? ")
    
    # Convert time
    newTime = convert(time)
    
    # Check if it's time for breakfast, lunch, or dinner
    if newTime >= 7 and newTime <= 8:
        print("breakfast time")
    elif newTime >= 12 and newTime <= 13:
        print("lunch time")
    elif newTime >= 18 and newTime <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    timeChange = float(hours) + float(minutes) / 60
    return timeChange

main()
