def main():
    q = input()
    convert(q)

def convert(msg):
    print(msg.replace(':)', '🙂').replace(':(', '🙁'))

main()
