import os

def func4():
    scripts_file = []
    for file in os.listdir():
        if file[-7:] == '.korpus':
            os.remove(file)
    exit()