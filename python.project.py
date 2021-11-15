import cv2
img_location="C:\\Users\\ASISH VARDHAN SINGH\\Pictures\\Camera Roll\\big_thumb.jpg"
img=cv2.imread(img_location)
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
inverted_img=255-gray_image
blurred_img=cv2.GaussianBlur(inverted_img,(21,21),0)
inverted_blurred_img=255-blurred_img
sketch_img=cv2.divide(gray_image,inverted_blurred_img,scale=256.0)
cv2.imshow('original image',img)
cv2.imshow('new image',sketch_img)
cv2.waitKey(0)
