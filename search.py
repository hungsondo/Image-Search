# import the necessary packages
from ColorDescriptor import ColorDescriptor
from searcher import Searcher
import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())
#Khởi tạo bộ trích xuất đặc trưng với các bin 8 bin Hue , 12 bin Saturation ,3 bin Value 
cd = ColorDescriptor((8, 12, 3))
# Đọc ảnh đầu vào 
query = cv2.imread(args["query"])
# Trích xuất đặc trưng ra vector features
features = cd.describe(query)
# perform the search
#khởi tạo searcher với path ở sau args[index]
searcher = Searcher(args["index"])
#Thực hiện search và trả về mảng 10 kết quả , kết quả có cấu trúc ('điểm', 'id ảnh')
results = searcher.search(features)
print(results)
# Hiển thị ảnh đầu vào
cv2.imshow("Query", query)
#Hiển thị kết quả
# loop over the results
for (score, resultID) in results:
	# Đọc ảnh kết quả và hiển thị
	result = cv2.imread(args["result_path"] + "/" + resultID)
	cv2.imshow("Result", result)
	cv2.waitKey(0)