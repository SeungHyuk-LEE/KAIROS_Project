import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout


class MyWindow(QWidget):

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

if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MyWindow()

    window.show()

    sys.exit(app.exec_())
#
"""
<Grid>
00 01 02 03
10 11 12 13
20 21 22 23
"""
#