## Image Metadata Capture

This code aims to capture images in a given directory for reading their metadata, capturing latitude, longitute, altitude, date and time of the moment the photo was taken.

##

### Basic information about the usage of the script

###### 1. Usage operation flow:

1. Create a folder named `dataset`;
2. Upload the desired images to the folder;
3. Run the notebook cells in order or just run the **.py** file in the same path of your `dataset`, as shown below:

```bash
.
├── dataset
│   ├── image-0.jpg
│   ├── image-1.jpg
│   ├── image-2.jpg
│   └── image-3.jpg
└── image-metadata-capture.py
```

<br>

###### 2. Script changes needed:
Create and configure your path to fit it on your files on line 19. Keep in mind that it is necessary to put a path above the dataset directory:
```python
# For example:
dataset_path = 'C:\\Users\\lucas\\Downloads\\';
```

##

### Remider

In some cases, it may be that a certain image does not have metadata attached, in this case, I recommend using the jupyter notebook so that it is possible to debug the code at runtime.
