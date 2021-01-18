import cv2

def make_cartoon(file_path):
	img = cv2.imread(file_path)
	
	#get edges
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = cv2.medianBlur(gray, 5)
	edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
	# color
	color = cv2.bilateralFilter(img, 9, 300, 300)
	# cartoon
	cartoon = cv2.bitwise_and(color, color, mask=edges)
	return cartoon
	
