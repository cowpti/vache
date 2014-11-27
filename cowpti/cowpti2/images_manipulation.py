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




def resizeImage(img,hMax,lMax) : 
    
    with Image as img: 
    
        var maxWidth = lMax; ##Max width for the image
        var maxHeight =hMax;    ##Max height for the image
        var ratio = 0;  ## Used for aspect ratio
        var width = img.width();    ##Current image width
        var height = img.height();  ## Current image height

        // Check if the current width is larger than the max
        if(width > maxWidth){
            ratio = maxWidth / width;   // get ratio for scaling image
            $(this).css("width", maxWidth); // Set new width
            $(this).css("height", height * ratio);  // Scale height based on ratio
            height = height * ratio;    // Reset height to match scaled image
            width = width * ratio;    // Reset width to match scaled image
        }

        // Check if current height is larger than max
        if(height > maxHeight){
            ratio = maxHeight / height; // get ratio for scaling image
            $(this).css("height", maxHeight);   // Set new height
            $(this).css("width", width * ratio);    // Scale width based on ratio
            width = width * ratio;    // Reset width to match scaled image
            height = height * ratio;    // Reset height to match scaled image




filefolder = '/var/www/gclcimages/'
os.chdir(filefolder)
for file in glob.glob("*.jpg"):
    filepath = os.path.realpath(file) # script filename (usually with path)
    print(filepath)
    genererVersions(filepath)