def main():
  
    # Get input and convert it to float
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    
    # Multiply and print formatted
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(price):
    updt = price.strip("$")
    return float(updt)

def percent_to_float(perc):
    updt = perc.strip("%")
    return float(updt) / 100

main()
