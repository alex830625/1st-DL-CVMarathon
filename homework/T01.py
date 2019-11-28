#先把opencv 讀進來
import cv2

#定義img是甚麼東西， 接著讀圖片，前面是視窗名稱，後面是檔名
img = cv2.imread('img/lena.png')

#把圖片做影像處理，這邊把圖片轉成灰階
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#把圖片轉成線條
canny_img = cv2.Canny(gray_img,100,200)

#把圖片show出來
cv2.imshow('lena',img)
cv2.imshow('lena2',gray_img)
cv2.imshow('lena3',canny_img)
#下面兩行為任意視窗關閉圖片
cv2.waitKey(0) 
cv2.destroyAllWindows() 