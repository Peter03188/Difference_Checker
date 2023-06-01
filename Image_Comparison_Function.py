import cv2
import numpy as np
from Ignore_size import ignore_size
from Combine_Image_Function import combined_images


def comparison(image1_path, image2_path, output_path, device_type):
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Ensure the images are the same size
    if image1.shape != image2.shape:
        print("The images have different sizes.")
        return
    # Define the region to ignore
    x, y, w, h = ignore_size[device_type]

    mask = np.ones_like(image1) * 255
    mask[y:y + h, x:x + w] = 0

    # Apply the mask to both images
    masked_image1 = cv2.bitwise_and(image1, mask)
    masked_image2 = cv2.bitwise_and(image2, mask)

    # Compute the absolute difference between the images
    diff = cv2.absdiff(masked_image1, masked_image2)

    # Apply a threshold to create a binary difference image
    _, thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY)

    # Convert the threshold image to a single-channel image
    gray_thresh = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)

    # Dilate the single-channel threshold image to make differences more visible
    kernel = np.ones((20, 20), np.uint8)
    dilated = cv2.dilate(gray_thresh, kernel, iterations=1)

    # Find contours of the differences
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on the original image in red
    highlighted = image1.copy()
    cv2.drawContours(highlighted, contours, -1, (0, 0, 255), 2)

    # Save the highlighted image if there are any pixel differences
    has_difference = np.any(diff > 100)
    if has_difference:
        cv2.imwrite(output_path, highlighted)
        combined_images(image1_path, image2_path, output_path, output_path)

