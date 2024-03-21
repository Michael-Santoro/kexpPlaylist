def openfile(file_path:str):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            print("File contents:")
            print(file_contents)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")
    
    return file_contents