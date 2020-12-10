import os

path = "/dev"

for root, dirs, files in os.walk(path):
    path = root.split(os.sep)
    print('\033[1m' + (len(path) - 1) * '-', os.path.basename(root) + '\033[0m')
    for file in files:
        print(len(path) * '--', file)
