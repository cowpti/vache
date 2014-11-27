#!/usr/bin/env python

import sys
import getopt
from wand.image import Image

def genererVersions(filepath):
    with Image(filename=filepath, resolution=200) as img:
        img.compression_quality = 99
        img.format = 'jpeg'
        with open(filepath, 'wb') as f:
            img.transform(resize='900x360>')
            img.save(filename=filepath[0,len(filepath)-6] + "_big.jpg")
            img.resize(320,168)
            img.save(filename=filepath[0,len(filepath)-6] + "_big.jpg" )


  





def main():
  
    path = '/var/www/images'
    dirs = os.listdir(path)
    for file in dirs:
     print(filepath)