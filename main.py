#
#██████╗░██╗░░██╗░█████╗░████████╗░█████╗░██████╗░██╗░░░██╗
#██╔══██╗██║░░██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚██╗░██╔╝
#██████╔╝███████║██║░░██║░░░██║░░░██║░░██║██████╔╝░╚████╔╝░
#██╔═══╝░██╔══██║██║░░██║░░░██║░░░██║░░██║██╔═══╝░░░╚██╔╝░░
#██║░░░░░██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░░░░░░░██║░░░
#╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░░░░░░░╚═╝░░░
#
# © MrBogdanYT. All rights reserved.

import cv2
import imutils
import numpy as np

filter = 'none'
type = 0 #Type 1 = .png | Type 2 = .jpg

print("██████╗░██╗░░██╗░█████╗░████████╗░█████╗░██████╗░██╗░░░██╗")
print("██╔══██╗██║░░██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚██╗░██╔╝")
print("██████╔╝███████║██║░░██║░░░██║░░░██║░░██║██████╔╝░╚████╔╝░")
print("██╔═══╝░██╔══██║██║░░██║░░░██║░░░██║░░██║██╔═══╝░░░╚██╔╝░░")
print("██║░░░░░██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░░░░░░░██║░░░")
print("╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░░░░░░░╚═╝░░░")
print('')
print('Hello, Welcome to PhotoPY.')
print("To Start, Please put your photo into the directory of the file.")
print("After that, rename the photo to image.")
print("NOTE: We only support .png and .jpg")
print('')
print('')
print('Now, Please select the type of your file. Type the number specified under.')
print('1 -> .png')
print('2 -> .jpg')

type = input("File Type:")
type = int(type)

# Verify what file type.
if type == 1:
    print("")
    print("PNG type was sellected.")
    print("")
elif type == 2:
    print("")
    print("JPG type was sellected.")
    print("")
else:
    print('')
    print('Unsupported type.')
    print('')
print('')
print('Now, Please select the filter you want to be applied to your image.')
print('1. - GaussianBlur')
print('2. - Gray and White')
print('3. - Erosion')
print('4. - Dilation')
print('5. - Lighter')
print('6. - Darker')
print('7. - Resize')
print('8. - Rotate (With Cropping)')
print('9. - Rotate (Without Cropping)')

filter = input("Filter:")
filter = int(filter)



if type == 1:
  image = cv2.imread("image.png")
  if filter == 1:
    blurred = cv2.GaussianBlur(image , (17 , 17) , 0)
    cv2.imshow("PhotoPY Output" , blurred)
    cv2.waitKey(0)
  if filter == 2:
    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    cv2.imshow("PhotoPY Output" , gray)
    cv2.waitKey(0)
  if filter == 3:
      for i in range(0,3):
         eroded = cv2.erode(image.copy() , None , iterations = i + 1)
         cv2.imshow("Eroded {} times [PRESS ANY KEY TO CLOSE]".format(i+ 1) , eroded)
         cv2.waitKey(0)
  if filter == 4:
     for i in range(0,3):
       dilated = cv2.dilate(image.copy() , None , iterations = i + 1)
       cv2.imshow("Dilated {} times [PRESS ANY KEY TO CLOSE]".format(i+ 1) , dilated)
       cv2.waitKey(0)
  if filter == 5:
    M = np.ones(image.shape , dtype = "uint8") * 100
    added = cv2.add(image , M)
    cv2.imshow("PhotoPY Output" , added)
    cv2.waitKey(0)
  if filter == 6:
    M = np.ones(image.shape , dtype = "uint8") * 100
    subtract = cv2.subtract(image, M)
    cv2.imshow("PhotoPY Output" , subtract)
    cv2.waitKey(0)
  if filter == 7:
    number_resize = input("What size should the output be?")
    number_resize = int(number_resize)
    resized = imutils.resize(image , width=number_resize)
    cv2.imshow("PhotoPY Output" , resized)
    cv2.waitKey(0)
  if filter == 8:
    number_rotate = input("How much should the output be rotated?")
    number_rotate = int(number_rotate)
    rotated = imutils.rotate(image , number_rotate)
    cv2.imshow("PhotoPY Output" , rotated)
    cv2.waitKey(0)
  if filter == 9:
    number_rotate = input("How much should the output be rotated?")
    number_rotate = int(number_rotate)
    rotated = imutils.rotate_bound(image , number_rotate)
    cv2.imshow("PhotoPY Output" , rotated)
    cv2.waitKey(0)


if type == 2:
  image = cv2.imread("image.jpg")
  if filter == 1:
    blurred = cv2.GaussianBlur(image , (17 , 17) , 0)
    cv2.imshow("PhotoPY Output" , blurred)
    cv2.waitKey(0)
  if filter == 2:
    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    cv2.imshow("PhotoPY Output" , gray)
    cv2.waitKey(0)
  if filter == 3:
      for i in range(0,3):
         eroded = cv2.erode(image.copy() , None , iterations = i + 1)
         cv2.imshow("Eroded {} times [PRESS ANY KEY TO CLOSE]".format(i+ 1) , eroded)
         cv2.waitKey(0)
  if filter == 4:
     for i in range(0,3):
       dilated = cv2.dilate(image.copy() , None , iterations = i + 1)
       cv2.imshow("Dilated {} times [PRESS ANY KEY TO CLOSE]".format(i+ 1) , dilated)
       cv2.waitKey(0)
  if filter == 5:
    M = np.ones(image.shape , dtype = "uint8") * 100
    added = cv2.add(image , M)
    cv2.imshow("PhotoPY Output" , added)
    cv2.waitKey(0)
  if filter == 6:
    M = np.ones(image.shape , dtype = "uint8") * 100
    subtract = cv2.subtract(image, M)
    cv2.imshow("PhotoPY Output" , subtract)
    cv2.waitKey(0)
  if filter == 7:
    number_resize = input("What size should the output be?")
    number_resize = int(number_resize)
    resized = imutils.resize(image , width=number_resize)
    cv2.imshow("PhotoPY Output" , resized)
    cv2.waitKey(0)
  if filter == 8:
    number_rotate = input("How much should the output be rotated?")
    number_rotate = int(number_rotate)
    rotated = imutils.rotate(image , number_rotate)
    cv2.imshow("PhotoPY Output" , rotated)
    cv2.waitKey(0)
  if filter == 9:
    number_rotate = input("How much should the output be rotated?")
    number_rotate = int(number_rotate)
    rotated = imutils.rotate_bound(image , number_rotate)
    cv2.imshow("PhotoPY Output" , rotated)
    cv2.waitKey(0)
