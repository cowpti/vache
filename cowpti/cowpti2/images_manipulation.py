import glob
import os
import sys 
from wand.image import Image


def genererVersions(filepath):
    with Image(filename=filepath, resolution=200) as img:
        img.compression_quality = 55
        img.format = 'jpeg'
        img.transform(resize='900x360')
        img.save(filename=filepath.replace(' ', '')[:-4].upper()+'_big.jpg')
        img.sample(320,168)
        img.save(filename=filepath.replace(' ', '')[:-4].upper()+'_small.jpg')


filefolder = '/var/www/gclcimages/'
os.chdir(filefolder)
for file in glob.glob("*.jpg"):
    filepath = os.path.realpath(file) # script filename (usually with path)
    print(filepath)
    genererVersions(filepath)

