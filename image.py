import os
from PIL import Image
import cv2
import mydecoder
import progressbar
from time import sleep
import sys


def main():
    print("A logo Adding utility \n")
    print("Welcome back JiLL")
    logo_file = './Data/temp_logo.png'
    brush_file = './Data/temp_brush.png'
    logo_file1 = './Data/temp_logo.nit'
    brush_file1 = './Data/temp_brush.nit'
    try:
       os.remove(logo_file)
       os.remove(brush_file)
    except OSError:
        pass
    try:
       os.remove(logo_file1)
       os.remove(brush_file1)
    except OSError:
        pass
    #Creating Copies
    mydecoder.temp_copy()
    mydecoder.rename()
    
    #For logo
    logoIm = Image.open(logo_file)
    logoWidth, logoHeight = logoIm.size
    #For Brush
    brushIm = Image.open(brush_file)
    brushWidth, brushHeight = logoIm.size
    
    #Checking the directory
    os.makedirs('withlogo', exist_ok = True)
    #Photo Folder
    photos_list = os.listdir('./Photos')
    number_of_photos = len(photos_list)
    print("Total "+str(number_of_photos) + " images found !!")
    count = 0 
    #For progress bar
    bar = progressbar.ProgressBar(maxval=20, \
         widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    for filename in photos_list:
        #For progress bar in one line
        sys.stdout.write('\r')
        if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == logo_file:
            continue

        #Manipulating the images
        im = Image.open(os.path.join('Photos', filename))
        width, height = im.size
        temp_logo = logoHeight
        logoHeight = (int)(height/11.7)
        perc_change_in_logo = temp_logo/logoHeight
        logoWidth = (int)(logoWidth/perc_change_in_logo)
        logoIm = logoIm.resize((logoWidth,logoHeight))

        temp_brush = brushHeight
        brushHeight = (int)(height/7.8)
        perc_change_in_brush = temp_brush/brushHeight
        brushWidth = (int)(brushWidth/perc_change_in_brush)
        brushIm = brushIm.resize((brushWidth,brushHeight))
        im.paste(brushIm, (width - brushWidth, height - brushHeight), brushIm)
        im.paste(logoIm, (width - logoWidth - (int)(0.03 * width), height - (int)(0.02 * height) -logoHeight), logoIm)
        im.save(os.path.join('withlogo', filename))

        #Updating progress bar
        count = count + 1
        bar.update(count)
        sys.stdout.flush()
    
    #Deleting the tempfiles
    os.remove(logo_file)
    os.remove(brush_file)
    bar.finish()
    temp = input('\nAll images are compiled successfuly\n\nPress any key to exit !!')

if __name__=="__main__":
    main()