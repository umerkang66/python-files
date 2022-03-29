import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if folder exist, otherwise create it
if not os.path.exists(output_folder):
    # create the folder with the "output_folder" name, if this folder doesn't exit
    os.makedirs(output_folder)

# loop over entire first folder, and convert all the jpeg images to png
for filename in os.listdir(image_folder):
    # listdir() will return items in the provided folder
    img = Image.open(f"{image_folder}{filename}")
    # remove .jgp from the input files, split the filename into two elements of tuple
    clean_name = os.path.splitext(filename)
    # save them to second folder
    img.save(f"{output_folder}{clean_name[0]}.png", "png")
    print("All done")
