import ColorDescriptor

#Used for parsing command line arguments
import argparse
#Used for getting paths of our images
import glob
import cv2

#Create the argument parser to parse the arguments
ap = argparse.ArgumentParser()

#Switch for the path to our photos directory
#Thêm biến vào câu lệnh khởi chạy
ap.add_argument("-d","--dataset", required = True , help = "Path to directory that contains images")
ap.add_argument("-i","--index", required = True , help = "Path to where the index will be stored")
args = vars(ap.parse_args())


#Khởi tạo bộ trích xuất đặc trưng với các bin 8 bin trong kênh Hue , 12 bin kênh Saturation ,3 bin Value 
cd = ColorDescriptor.ColorDescriptor((8,12,3))

# open the output index file for writing
output = open(args["index"], "w")
# use glob to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
	# extract the image ID (i.e. the unique filename) from the image
	# path and load the image itself
	#Khởi tạo ID mà sau dùng để viết vào file index 
	imageID = imagePath[imagePath.rfind("\\") + 1:]
	# Đọc ảnh
	image = cv2.imread(imagePath)
	# Gọi đến hàm describe để trích xuất đặc trưng ảnh
	features = cd.describe(image)
	# Viết các đặc trưng vào file
	features = [str(f) for f in features]
	output.write("%s,%s\n" % (imageID, ",".join(features)))
# Đóng file index
output.close()

