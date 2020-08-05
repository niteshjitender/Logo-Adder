import os
from PIL import Image
import cv2

def main():
    print("Hello World")
    # sq_fit_size = 300
    logo_file = './Logo/Jill-Perla-Art-Logo.png'
    logoIm = Image.open(logo_file)
    logoWidth, logoHeight = logoIm.size

    brush_file = 'brush.png'
    brushIm = Image.open(brush_file)
    brushWidth, brushHeight = logoIm.size

    os.makedirs('withlogo', exist_ok = True)
    for filename in os.listdir('./Photos'):
        if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == logo_file:
            continue
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
        # if width > sq_fit_size and height > sq_fit_size:
        #     if width > height:
        #         height = int((sq_fit_size / width) * height)
        #         width = sq_fit_size
        #     else:
        #         width = int((sq_fit_size / height) * width)
        #         height = sq_fit_size
        #     print('Resizing %s'% (filename)) 
        #     im = im.resize((width, height))

        im.paste(brushIm, (width - brushWidth, height - brushHeight), brushIm)
        im.paste(logoIm, (width - logoWidth - (int)(0.03 * width), height - (int)(0.02 * height) -logoHeight), logoIm)
        im.save(os.path.join('withlogo', filename))

if __name__=="__main__":
    main()