import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox
#GridLayout : 화면구성 레이아웃

from pymycobot.mycobot import MyCobot
import time
# from ultralytics import YOLO
import cv2

# Cobot의 position
class twist:
    def __init__(self,lx,ly,lz,ax,ay,az,speed):
        self.lx=lx
        self.ly=ly
        self.lz=lz
        self.ax=ax
        self.ay=ay
        self.az=az
        self.speed=speed

#인스턴스 생성
#mc=MyCobot('COM4',115200)
mc=MyCobot('COM7',115200)

mc.send_angles([0,0,0,0,0,0],30)
time.sleep(3)

t=twist(-220,-50,280,-170,0,70,20)
mc.send_coords([t.lx,t.ly,t.lz,t.ax,t.ay,t.az],t.speed,0)
time.sleep(3)


class MyWindow(QWidget):
    global t

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle('PyQt5 Grid of Buttons Example')  # 창 제목 설정

        layout = QGridLayout()  # 그리드 레이아웃 생성

        # 버튼을 생성하고 그리드에 추가

        for i in range(3):

            for j in range(3):

                button = QPushButton(str(i * 3 + j + 1), self)  # 버튼 생성 및 텍스트 설정

                button.clicked.connect(lambda checked, idx=i*3+j+1: self.buttonClicked(idx))  # 버튼 클릭 시 이벤트 핸들러 연결

                layout.addWidget(button, i, j)  # 그리드에 버튼 추가

        self.setLayout(layout)  # 레이아웃 설정

    def buttonClicked(self, index):

        print('Button', index, 'Clicked!')
        print(t.lx,t.ly,t.lz,t.ax,t.ay,t.az)
        print(t.speed)
        
        if index == 9:
            self.quit_application()
            
        elif index == 1:
            mc.send_angles([0,0,0,0,0,0],30)
            mc.power_on()
            
        elif index == 2:
            t.lx+=10
            if t.lx>-50:
                t.lx=-50
            mc.send_coords([t.lx,t.ly,t.lz,t.ax,t.ay,t.az],t.speed,0)
            
        elif index == 3:
            t.lx-=10
            if t.lx<-320:
                t.lx=-320
            mc.send_coords([t.lx,t.ly,t.lz,t.ax,t.ay,t.az],t.speed,0)
            
        elif index == 4:
            t.ly+=10
            if t.ly>140:
                t.ly=140
            mc.send_coords([t.lx,t.ly,t.lz,t.ax,t.ay,t.az],t.speed,0)
            
        elif index == 5:
            t.ly-=10
            if t.ly<-140:
                t.ly=-140
            mc.send_coords([t.lx,t.ly,t.lz,t.ax,t.ay,t.az],t.speed,0)
            
        elif index == 6:
            t.lz+=10
            if t.lz>290:
                t.lz=290
            mc.send_coords([t.lx,t.ly,t.lz,t.ax,t.ay,t.az],t.speed,0)
            
        elif index == 7:
            t.lz-=10
            if t.lz<50:
                t.lz=50
            mc.send_coords([t.lx,t.ly,t.lz,t.ax,t.ay,t.az],t.speed,0)
            
        elif index == 8:
            pass
                                                                                          
    def quit_application(self):
        # 강제 종료 다이얼로그 표시 / 팝업창
        reply = QMessageBox.question(self, '강제 종료', '프로그램을 강제로 종료하시겠습니까?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            # 사용자가 예를 선택하면 프로그램 종료
            QApplication.quit()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MyWindow()

    window.show()

    sys.exit(app.exec_())
