import os

# print(dir(os))
# print(len(dir(os)))

# get current working directory
print(os.getcwd())

# list out directory
print(os.listdir())

def readAllContentInADirectory(content, file_name):
    if content == file_name.lower():
        print(f'Found {file_name} file in directory')
        return True
    return False

def deleteFolder(path):
    os.rmdir(f'{os.getcwd()}/to_delete')
    print('directory deleted')



readAllContentInADirectory(os.getcwd(), 'data.py')
deleteFolder('C:\\Users\\ADMIN\\Documents\\PythonFiles')

current_path = os.getcwd()
# os.mkdir('to_delete1')
# print('directory created')
