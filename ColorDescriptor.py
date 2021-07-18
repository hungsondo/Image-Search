import numpy as np
import cv2
import imutils


# Bộ trích xuất đặc trưng ảnh
class ColorDescriptor:
    def __init__(self, bins):
        #Storing number of bins for histogram
        self.bins = bins
        
    # Trích xuất đặc trưng của ảnh, trả về là vector đặc trưng của ảnh
    def describe(self, image):
        #Convert the image into hsv and initialize the features to quantify the image
        image = image.astype('uint8')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        features = []
        
        #Lấy chiều dài, rộng của ảnh 
        (h, w) = image.shape[:2]      
        #Tính tọa độ tâm của elip    
        (cX, cY) = (int(w * 0.5), int(h * 0.5))
        
        #Bán trục lớn, nhỏ của hình elip với chiều cao  là 0.75 ảnh gốc , chiều rộng 0.6 ảnh gốc
        (axesX, axesY) = (int(w * 0.75) // 2, int(h * 0.6) // 2)
        #Khởi tạo mặt nạ elip
        ellipMask = np.zeros(image.shape[:2], dtype = "uint8")
        cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 90, 0, 360, 255, -1)
            
        #Extract a color histogram from the elliptical region and update the feature vector
        #Trích xuất đặc trưng của mặt nạ elip
        hist = self.histogram(image, ellipMask)
        #Thêm đặc trưng đó vào vector features
        features.extend(hist)
        #Return the feature vector
        return features
    
    # Tính histogram của 1 vùng trên ảnh, trả về là vector đặc trưng 1 chiều của vùng ảnh
    def histogram(self,image,mask):
        
        #Extract a 3-D color histogram from the masked region of the image, using the number of bins supplied
        hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins, [0, 180, 0, 256, 0, 256])
        
        #Chuẩn hóa histogram
        hist = cv2.normalize(hist,hist)
        # Chuyển ma trận nhiều chiều thành vecto 1 chiều
        hist = hist.flatten()
        #Returning histogram
        return hist
