import sys
import re

def main():
    print(parse(input('HTML: ')))

def parse(s):

    # if it's not an iframe html tag, return None
    if not 'iframe' in s:
        return None

    # re pattern to search for
    pattern = r"(https?://(w{3}\.)?youtube\.com/embed/(\w*))"

    # look for the url
    find_url = re.search(pattern, s)

    # return the url (only the last group/part)
    if find_url:
        return f'https://youtu.be/{find_url.group(3)}'


if __name__ == '__main__':
    main()
