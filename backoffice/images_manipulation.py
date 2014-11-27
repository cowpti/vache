#!/usr/bin/env python

import sys
import getopt
from wand.image import Image

def genererVersions(filepath):
    with Image(filename=filepath, resolution=200) as img:
        img.compression_quality = 99
        img.format = 'jpg'
        with open(filepath, 'wb') as f:
            
            s = filepath
            resizeImg(img, s[0,len(s)-6] + "_big.jpg" ,900,360) 
            resizeImg(img, s[0,len(s)-6] + "_big.jpg" ,320,128) 
    
       



def resizeImg(sourceFile, destFile, width, height):                                                                                                                                                                                                                                       
  with Image(width=width, height=height) as outerImg:                                                                                                                                                                                                                                     
    with Image(filename=sourceFile) as img:                                                                                                                                                                                                                                               
      img.transform(resize="%dx%d>" % (width, height))                                                                                                                                                                                                                                    
      outerImg.format = img.format.lower()                                                                                                                                                                                                                                                
      outerImg.composite(img, left=(width - img.width) / 2, top=(height - img.height) / 2)                                                                                                                                                                                                
      outerImg.save(filename=destFile)




def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
    # process arguments
    for arg in args:
        genererVersions(arg) # process() is defined elsewhere

if __name__ == "__main__":
    sys.exit(main())


