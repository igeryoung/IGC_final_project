import os
import cv2
import numpy as np
# print(os.listdir('/tmp2/kent/harm/Diff-Harmonization/Data/out'))

im = cv2.imread("/tmp2/kent/harm/Diff-Harmonization/Data/out/25/mask.png")
print(type(im))
print(np.max(im))