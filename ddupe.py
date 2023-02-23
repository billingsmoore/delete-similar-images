import os
from skimage import io, metrics

# Define a function to compare two images using their hash values
def compare_images(image_path_1, image_path_2):
    """
    Compares two images and returns their structural similarity index (SSIM).

    Parameters:
        image_path_1 (str): Path to the first image file.
        image_path_2 (str): Path to the second image file.

    Returns:
        float: SSIM value between 0 and 1, where 1 indicates the images are identical.
    """
    image_1 = io.imread(image_path_1)
    image_2 = io.imread(image_path_2)
    ssim = metrics.structural_similarity(image_1, image_2, multichannel=True)
    return ssim

# Define the folder path to search for images
folder_path = input("Input folder path: ")
threshold = float(input('Input image similarity threshold: '))

# Create a list of image files in the folder
image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

# Compare each image to every other image in the folder
done = False
while done == False:
    done = True
    for i in range(len(image_files)):
        for j in range(i + 1, len(image_files)):
            try:
                if compare_images(image_files[i], image_files[j]) >= threshold:
                    done = False
                # If the two images are similar, delete one of them
                    print(f'deleting {image_files[i]}')
                    os.remove(image_files[i])
                    break
            except:
                pass