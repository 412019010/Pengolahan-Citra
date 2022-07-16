import cv2
import imutils
from re import search

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

file = 'video/lurus.mp4'

def detect(frame):
	frame = imutils.resize(frame, width=min(800, frame.shape[1]))
	
	frameg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	(regions, _) = hog.detectMultiScale(frameg,
										winStride=(4, 4),
										padding=(4, 4),
										scale=1.05)

	person = 0
	for (x, y, w, h) in regions:
		cv2.rectangle(frame, (x, y),
					(x + w, y + h),
					(0, 255, 0), 2)
		person += 1

	if person >= 4 :
		r = 255
		g = 0
		b = 0
		cv2.putText(frame, 'Lebih dari 3 orang terdeteksi', (40, 110), cv2.FONT_HERSHEY_DUPLEX, 0.8, (b, g, r), 2)
	else :
		r = 0
		g = 255
		b = 0

	cv2.putText(frame, 'Jumlah orang : {}'.format(person), (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (b,g,r), 2)
	
	cv2.imshow("Output", frame)

if search('.jpeg', file) or search('.jpg', file) or search('.png', file) :
	frame = cv2.imread(file)
	detect(frame)
	
	cv2.waitKey(0)

elif search('.mp4', file) or search('.avi', file) :
	cap = cv2.VideoCapture(file)

	while cap.isOpened():

		ret, frame = cap.read()
		if ret:
			detect(frame)
			if cv2.waitKey(1) & 0xFF == ord('\x1b'):
				break
		else:
			break
	cap.release()

cv2.destroyAllWindows()
