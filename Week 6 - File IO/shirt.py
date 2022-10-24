import sys
from PIL import Image, ImageOps

def main():

    # Check command-line args
    if len(sys.argv) <= 2:
        sys.exit('Too few command line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command line arguments')
    elif not check_file(sys.argv[1]) or not check_file(sys.argv[2]):
        sys.exit('Invalid input')
    elif sys.argv[1].split('.')[1] != sys.argv[2].split('.')[1]:
        sys.exit('Input and output have different extensions')


    try:

        # Open images, resize, overlay and save
        shirt = Image.open('shirt.png')
        photo = Image.open(sys.argv[1])
        result = ImageOps.fit(photo, shirt.size)
        result.paste(shirt, shirt)
        result.save(sys.argv[2])


    except FileNotFoundError:
        sys.exit('File does not exist')


# Function to check correct file extension
def check_file(f):

    # split file and get extension
    extension = f.rsplit('.')[-1].lower().strip()

    match extension:
        case 'jpg' | 'jpeg' | 'png':
            return True

    return False

if __name__ == '__main__':
    main()
