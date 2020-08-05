import os
renamee = "./Logo/logo.png"
new_extension = ".nit"
pre, ext = os.path.splitext(renamee)
os.rename(renamee, pre + new_extension)
renamee = "./Data/brush.png"
new_extension = ".nit"
pre, ext = os.path.splitext(renamee)
os.rename(renamee, pre + new_extension)