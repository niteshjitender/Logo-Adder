import os
import shutil

#This will rename the temp file generated to *.png
def rename():
    renamee = "./Data/temp_logo.nit"
    new_extension = ".png"
    pre, ext = os.path.splitext(renamee)
    os.rename(renamee, pre + new_extension)
    renamee = "./Data/temp_brush.nit"
    new_extension = ".png"
    pre, ext = os.path.splitext(renamee)
    os.rename(renamee, pre + new_extension)

#This will create simply copy of the file
def temp_copy():
    shutil.copyfile('./Data/brush.nit', './Data/temp_brush.nit')
    shutil.copyfile('./Data/logo.nit', './Data/temp_logo.nit')


# temp_copy()
# rename()

