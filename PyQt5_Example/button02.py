import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('PyQt5 Multiple Buttons Example')  # 창 제목 설정


        layout = QVBoxLayout()  # 수직 레이아웃 생성


        # 첫 번째 버튼 생성

        btn1 = QPushButton('Button 1', self)

        btn1.clicked.connect(lambda: self.buttonClicked(1))  # 버튼 클릭 시 이벤트 핸들러 연결

        layout.addWidget(btn1)  # 레이아웃에 버튼 추가


        # 두 번째 버튼 생성

        btn2 = QPushButton('Button 2', self)

        btn2.clicked.connect(lambda: self.buttonClicked(2))  # 버튼 클릭 시 이벤트 핸들러 연결

        layout.addWidget(btn2)  # 레이아웃에 버튼 추가


        self.setLayout(layout)  # 레이아웃 설정


    def buttonClicked(self, index):

        print('Button', index, 'Clicked!')


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MyWindow()

    window.show()

    sys.exit(app.exec_())
