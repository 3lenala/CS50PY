def main():
    file_name = input('File name: ')
    file_name = file_name.lower().strip()
    extensions = {'.gif':'image/gif','.jpg':'image/jpeg','.png':'image/png','.pdf':'application/pdf','.txt':'text/plain','.zip':'application/zip'}
    extension = file_name[-4:]
    if file_name[-5:] == '.jpeg':
        print('image/jpeg')
    elif extension in extensions:
        print(extensions[extension])
    else:
        print('application/octet-stream')

if __name__ == '__main__':
    main()
