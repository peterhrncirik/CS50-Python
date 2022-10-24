ext = input("File name: ")

# Print the file extension
match ext.rsplit('.')[-1].lower().strip():
    case 'gif':
        print('image/gif')
    case 'jpg' | 'jpeg':
        print('image/jpeg')
    case 'png':
        print('image/png')
    case 'pdf':
        print('application/pdf')
    case 'txt':
        print('text/plain')
    case 'zip':
        print('application/zip')
    case _:
        print("application/octet-stream")
