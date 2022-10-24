import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
all_fonts = figlet.getFonts()

if len(sys.argv) == 2:
    sys.exit('Invalid usage')
elif (len(sys.argv) == 3) and not(sys.argv[1] == '-f' or sys.argv[1] == '--font') or (sys.argv[2] not in all_fonts):
    sys.exit('Invalid usage')


i = input('Input: ')


if len(sys.argv) == 1:
    figlet.setFont(font=all_fonts[random.randint(0, len(all_fonts) - 1)])
    print(figlet.renderText(i))
else:
    f = sys.argv[2]
    figlet.setFont(font=f)
    print(figlet.renderText(i))
