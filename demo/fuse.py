import cv2
import numpy as np
import os 
import random

def read_images_from_directory(directory_path):
    # Get a list of all files in the directory
    file_list = os.listdir(directory_path)
    
    # Filter out non-image files (optional)
    image_files = [file for file in file_list if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
    
    # Read each image and store them in a list
    images = []
    for image_file in image_files:
        image_path = os.path.join(directory_path, image_file)
        image = cv2.imread(image_path)
        if image is not None:
            images.append(image)
    
    return images

def fuser(idx, styles):
    # Read the images and mask
    random_integer = random.randint(0, 3)
    image1 = cv2.imread(f'/tmp2/kent/harm/Diff-Harmonization/demo/composite/0{idx}.jpg')
    mask = cv2.imread(f'/tmp2/kent/harm/Diff-Harmonization/demo/mask/0{idx}_mask.jpg', cv2.IMREAD_GRAYSCALE)  # Ensure the mask is read as grayscale
    image2 = styles[random_integer]

    # Resize image2 to the shape of image1
    image2_resized = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    # Crop image1 by mask
    # Create a mask where the masked area is white (255) and the rest is black (0)
    cropped_image1 = cv2.bitwise_and(image1, image1, mask=mask)

    # Find the bounding box of the mask
    x, y, w, h = cv2.boundingRect(mask)

    # Crop the region from image1
    cropped_region = cropped_image1[y:y+h, x:x+w]

    # Create an inverse mask to paste the cropped part onto image2
    mask_inv = cv2.bitwise_not(mask)

    # Create a region of interest on image2
    roi = image2_resized[y:y+h, x:x+w]

    # Black-out the area of cropped_region in ROI
    roi_bg = cv2.bitwise_and(roi, roi, mask=mask_inv[y:y+h, x:x+w])

    # Add the cropped_region to the roi_bg
    result = cv2.add(roi_bg, cropped_region)

    # Place the result back onto image2_resized
    image2_resized[y:y+h, x:x+w] = result

    # Save or display the result
    cv2.imwrite(os.path.join('/tmp2/kent/harm/Diff-Harmonization/demo/style_composite', f'0{idx}.jpg'), image2_resized)
    # cv2.imshow('Result', image2_resized)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()



styles = read_images_from_directory('/tmp2/kent/harm/Diff-Harmonization/demo/style')


for i in range(15, 21):
    fuser(f"{i:02}", styles)