def openfile(file_path:str):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            print("File contents:")
            print(file_contents)
            return ' '.join(file_contents.split())
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")

data_load_map = {'hosts':'INSERT INTO hosts (id, uri, name,image_uri, thumbnail_uri,is_active) VALUES (%s, %s, %s, %s, %s)',
                 'plays':'INSERT INTO plays (name, age, email) VALUES (%s, %s, %s)',
                 }
    