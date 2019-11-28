import cv2
img_path = 'img/lena,png'
img = cv2.imread(img_path, cv2.IMREAD_COLOR)
img_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
cv2.waitKey(0) 
cv2.destroyAllWindows() 