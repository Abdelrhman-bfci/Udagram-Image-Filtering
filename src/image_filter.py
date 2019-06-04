import sys
import cv2
import os

inputDirectory = '/input/'
outputDirectory = '/output/'
fileName = 'test.jpg'
failed = False

def process(fileName, inputDirectory, outputDirectory):
    # We need an absolute path
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Load the image from disk
    img = cv2.imread(dir_path+inputDirectory+fileName,0)
    if img is None:
        return False, "Image Failed to Load"

    # Apply the Canny edge detection filter
    filtered = cv2.Canny(img, 50, 50)
    if filtered is None:
        return False, "Image Failed To Filter"


    # Write the image back to disk
    out = cv2.imwrite(dir_path+outputDirectory+fileName, filtered)
    if out == False:
        return False, "Image Failed To Write"

    return True, "Success"

isSuccess, message = process(fileName, inputDirectory, outputDirectory)
print(isSuccess)
print(message)
sys.stdout.flush()