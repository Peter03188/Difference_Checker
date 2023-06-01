import numpy as np
from PIL import Image


def combined_images(image_path_1, image_path_2, image_path_3, output_path):

    # Load the images and convert them to RGB format
    img1 = Image.open(image_path_1).convert("RGB")
    img2 = Image.open(image_path_2).convert("RGB")
    img3 = Image.open(image_path_3).convert("RGB")

    # Get the width and height of the first image and resize all images to the same size
    width, height = img1.size
    img1 = img1.resize((width, height))
    img2 = img2.resize((width, height))
    img3 = img3.resize((width, height))

    # Create a white border to separate the images
    padding = 10
    white = (0, 0, 0)
    border = Image.new('RGB', (padding, height), white)

    # Concatenate the images horizontally into a grid
    grid = np.hstack((img1, border, img2, border, img3))

    # Save the result as a new image
    result_img = Image.fromarray(grid)
    result_img.save(output_path)

