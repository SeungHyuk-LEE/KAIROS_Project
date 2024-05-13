from PyQt5.QtWidgets import *
import sys
import threading
				
from PyQt5 import QtWidgets
import cv2
from PyQt5 import QtGui


flag = 0


def camMain() :
	global flag
	cap=cv2.VideoCapture(0)

	width = 320
	height = 240
	label.resize(width, height)

	while True:	
		ret,frame=cap.read()

		h,w,c = frame.shape
		qImg = QtGui.QImage(frame.data, w, h, w*c, \
		QtGui.QImage.Format_BGR888)#
		pixmap = QtGui.QPixmap.fromImage(qImg)
		label.setPixmap(pixmap)

		print(flag)
		if flag == 1:
			print('flag << 1')
			#cap.release()
			break

	cap.release()
	cv2.destroyAllWindows()
	QApplication.quit()
	

# Create main application window
app = QApplication([])
app.setStyle(QStyleFactory.create("Cleanlooks"))
mw = QMainWindow()
mw.setWindowTitle('RC Car Joystick')
mw.setGeometry(100, 100, 300, 200)

# Create and set widget layout
# Main widget container
cw = QWidget()
ml = QGridLayout()
cw.setLayout(ml)
mw.setCentralWidget(cw)

# Create Screen
label = QtWidgets.QLabel()       # 텍스트나 이미지를 표시하기 위한 QLabel 위젯을 생성
ml.addWidget(label,0,0)

def close():
    global flag
    # 프로그램 종료 시 웹 카메라 해제
    print('flag = 1')
    flag = 1
    #cap.release()

# Create joystick
# 종료 버튼 생성
#exit_button = QPushButton('Exit', self)
exit_button = QPushButton('Exit')
exit_button.clicked.connect(close)           # 버튼 클릭 시 종료
ml.addWidget(exit_button)                     # 레이아웃에 버튼 추가

camThread = threading.Thread(target=camMain)
camThread.start()

mw.show()

# Start Qt event loop 
sys.exit(app.exec_())