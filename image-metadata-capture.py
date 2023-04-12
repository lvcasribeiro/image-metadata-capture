# Libraries imports:
import shutil as pysh
import pandas as pypd
import PIL
import os

from exif import Image
from PIL.ExifTags import TAGS

print('- All libraries were imported.');

# Aux variables:
image_time = [];
image_date = [];
image_latitude = [];
image_longitude = [];
path_to_image = [];

dataset_path = 'C:\\Users\\lucas\\Downloads\\';

def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1]/60 + coords[2]/3600;

    if ref == 'S' or ref == 'W':
        decimal_degrees = -decimal_degrees;
        
    return decimal_degrees
    
def image_coordinates(image_path):
    # Reading image file:
    with open(image_path, 'rb') as source:
        image = Image(source);

    if image.has_exif:
        try:
            image.gps_longitude;
            coords = (decimal_coords(image.gps_latitude, image.gps_latitude_ref), decimal_coords(image.gps_longitude, image.gps_longitude_ref));

            # Appending info:
            image_time.append(image.datetime_original[11:19]);
            image_date.append(image.datetime_original[:10]);
            image_latitude.append(coords[0]);
            image_longitude.append(coords[1]);
            path_to_image.append(image_path.split('dataset')[1][1::]);

        except AttributeError:
            print('- No coordinates.');
    else:
        print(f'- {image_path} has no EXIF information.');

    print(f"- {image_path} was taken at {image.datetime_original[11:19]} on {image.datetime_original[:10]}, and has latitude: {coords[0]} and longitude {coords[1]}");

# Directory measurement variable:
dataset_existente = os.path.exists(dataset_path + 'dataset');

# Creation of the 'dataset' directory, if it does not exist:
if not dataset_existente:
    os.system('mkdir dataset');
    print('- Dataset folder created. Populate it with images!');
    
    populated = input('Is the dataset directory already populated? [y/n]: ');
else:
    # Dataset directory benchmarking:
    dataset_diretorio = os.listdir(dataset_path + 'dataset');

    if len(dataset_diretorio) == 0:
        print('- Dataset folder already exists, necessary to populate the dataset directory with images.');
        populated = input('Is the dataset directory already populated? [y/n]: ');
    else:
        print('- Dataset folder already exists.');

# Reading each image [in array format] manually:
dataset_directory = dataset_path + 'dataset';
dataset_array = [];

dataset = os.listdir(dataset_directory);

for aux in range(len(dataset)):
    # Captures only files with .jpg or .png extensions and increments them in the dataset_array list:
    if (dataset[aux].split('.')[1] == 'JPG' or dataset[aux].split('.')[1] == 'jpg' or dataset[aux].split('.')[1] == 'PNG' or dataset[aux].split('.')[1] == 'png'):
        dataset_array.append(dataset[aux]);

print('- Dataset list created.');

# Checking the amount of images obtained:
print(f'- {len(dataset_array)} images were read.');

for aux in range(len(dataset_array)):
    path = f'{dataset_path}dataset\\{dataset_array[aux]}';

    print(f'{aux + 1} ', end = '');

    image_coordinates(path);

# Calling dataframe constructor after zipping:
images_info_dataframe = pypd.DataFrame(list(zip(path_to_image, image_time, image_date, image_latitude, image_longitude)), columns =['Image', 'Time', 'Date','Latitude', 'Longitude']);

print(images_info_dataframe.head());

# Writing a .xlsl file:
images_info_dataframe.to_excel(f'{dataset_path}images-info-lat-long.xlsx');