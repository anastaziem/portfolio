import os


FOLDER_OF_IMAGES = '/home/ondin/Developer/portfolio/portfolio-muckova-web-resources/image/'


files = os.listdir(FOLDER_OF_IMAGES)

# files = sorted([file if len(file) == 6 else '0' + file for file in files if file.endswith('.png') and file[0].isdigit()])

files = sorted([file for file in files if file.endswith('.png')])
print(files)
i = 0

for i, file in enumerate(files):
    prefix = '0' if i+1 < 10 else ''
    file = file[1:] if file[0] == '0' else file
    fpath = FOLDER_OF_IMAGES + file
    outfpath = FOLDER_OF_IMAGES + prefix + str(i+1) + '.png'
    os.rename(fpath, outfpath)
    #print(file, '->', prefix + str(i+1) + '.png')
