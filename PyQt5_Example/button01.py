# 버튼 생성 예제

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MyWindow(QWidget):  # QWidget 상속을 받음

    def __init__(self):

        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(100, 100, 300, 200)  # 창 위치와 크기 설정

        self.setWindowTitle('PyQt5 Button Example')  # 창 제목 설정


        # 버튼 생성

        btn = QPushButton('Click Me!', self)

        btn.setGeometry(100, 50, 100, 30)  # 버튼 위치와 크기 설정


        # 버튼 클릭 시 이벤트 핸들러 연결

        btn.clicked.connect(self.buttonClicked)



    def buttonClicked(self):

        print('Button Clicked!')


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MyWindow()

    window.show()

    sys.exit(app.exec_())
