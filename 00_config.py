import os
from pathlib import Path

run_in_cloud = False
dl_images_folder = "product_images"
database_name = "default"
collection_name = "prod_ann5"
FTS_collection_name = "product_text_ann2"

home_directory = Path.home()
local_temp_dir = os.path.join(home_directory, "temp")


def local_img_path(image_file_name, product_id): #input is (1, "imagefile.jpg")
    image_index = image_file_name[0]    # get index from tuple position 0
    basename = os.path.basename(image_file_name[1]) # get "imagefile" from "/path/to/imagefile"
    try:
        [image_file,image_extension] = basename.split('.') #get image file name "imagefile" and extension "jpg"
    except ValueError as e:
        print(f"Error splitting filename {basename}: {e}")
        return f"{dl_images_folder}/dummy.jpg"

    destination = f"{product_id}_{image_file}_{image_index+1}.{image_extension}".replace('%','_') # create a filename like "12345_imagefile_1.jpg" and replace % with _
    return f"{dl_images_folder}/" + os.path.basename(destination) # return "product_images/imagefile.jpg"