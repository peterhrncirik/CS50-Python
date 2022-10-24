import sys
import re

def main():
    print(validate(input('IPv4 Adress: ')))

def validate(ip):

    # Check IP Address pattern
    pattern = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"

    if re.search(pattern, ip):
        return True

    return False

if __name__ == '__main__':
    main()
