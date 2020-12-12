import os.path
import json
import random
import string

def remove(x):
    ID = input('Insert ID: ')
    for i in range(len(x['movies'])):
        if x['movies'][i]['ID'] == ID:
            del x['movies'][i]
            print('Removed')
        else:
            print('')


def add(x):
    ID = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    title = input("Add movie title: ")
    release_date = input("Add release date: ")
    genre = input("Add genre: ")
    entry = {"ID": ID, "Title": title, "Release date": release_date, "Genre": genre}
    x['movies'].append(entry)


if __name__ == '__main__':
    if os.path.exists('movies.json'):
        with open('movies.json', 'r') as f:
            x = json.load(f)
    else:
        x = {'movies': []}

    while True:
        if len(x) == 0:
            print('No entries')
        else:
            for i in x['movies']:
                print(i)

        operation = int(input('Operation:\n'+'1.Add\n2.Remove\n3.Exit\n'))

        if operation == 1:
            add(x)
        elif operation == 2:
            remove(x)
        elif operation == 3:
            break
        else:
            print('Try again')

    with open('movies.json', 'w') as outfile:
        json.dump(x, outfile)
