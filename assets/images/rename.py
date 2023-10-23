import os


files = os.listdir('.')

files = sorted([file if len(file) == 6 else '0' + file for file in files if file.endswith('.png') and file[0].isdigit()])

print(files)
i = 0

for i, file in enumerate(files):
    prefix = '0' if i+1 < 10 else ''
    file = file[1:] if file[0] == '0' else file
    os.rename(file, prefix + str(i+1) + '.png')
    #print(file, '->', prefix + str(i+1) + '.png')
