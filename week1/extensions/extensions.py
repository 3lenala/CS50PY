# This programs aims to output a file's media type given the file's name
# Mime types are declared outside any function so it is only 
MIME_TYPES = {
    '.gif':'image/gif',
    '.jpg':'image/jpeg',
    '.png':'image/png',
    '.pdf':'application/pdf',
    '.txt':'text/plain',
    '.zip':'application/zip',
    '.jpeg':'image/jpeg'
}

# Extract the sufix from the file's name
def get_suffix(file_name: str) -> str:
    # .rsplit(sperator, maxsplit) splits a string into a list starting from the right 
    # maxsplit specifies how many splits to do (optional)
    parts = file_name.strip().lower().rsplit('.', 1)
    if len(parts) == 1:
        return ''
    
    return '.' + str(parts[1])


def main():
    file_name = input('File name: ')
    file_name = file_name.lower().strip()
    sufix = get_suffix(file_name)
    
    if sufix in MIME_TYPES:
        print(MIME_TYPES[sufix])
    else:
        print('application/octet-stream')

if __name__ == '__main__':
    main()
