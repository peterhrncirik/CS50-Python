greeting = input("Greeting: ")

# hello/Hello = 0$
if greeting.strip().startswith("hello") or greeting.strip().startswith("Hello"):
    print("$0")
# word starts with h = 20$
elif greeting.strip().lower()[0] == "h":
    print("$20")
# anything else = 100$
else:
    print("$100")
