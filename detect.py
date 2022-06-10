import cv2
import imutils

# Initializing the HOG person
# detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture('pejalan3.mp4')

while cap.isOpened():
	person = 0

	# Reading the video stream
	ret, image = cap.read()
	if ret:
		image = imutils.resize(image,
							width=min(800, image.shape[1]))

		# Detecting all the regions
		# in the Image that has a
		# pedestrians inside it
		(regions, _) = hog.detectMultiScale(image,
											winStride=(4, 4),
											padding=(4, 4),
											scale=1.05)

		# Drawing the regions in the
		# Image
		for (x, y, w, h) in regions:
			cv2.rectangle(image, (x, y),
						(x + w, y + h),
						(0, 255, 0), 2)
			person += 1

		if person >= 4 :
			r = 255
			g = 0
			b = 0
		else :
			r = 0
			g = 255
			b = 0

		cv2.putText(image, 'Jumlah orang : {}'.format(person), (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (b,g,r), 2)
		if r>0 :
			cv2.putText(image, 'lebiih dari 4 orang terdeteksi', (40, 120), cv2.FONT_HERSHEY_DUPLEX, 0.8, (b, g, r), 2)

		# Showing the output Image
		cv2.imshow("Image", image)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
	else:
		break