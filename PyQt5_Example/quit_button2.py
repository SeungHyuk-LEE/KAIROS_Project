# 버튼 2개의 예제
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout ,QMessageBox

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

        btn2.clicked.connect(self.quit_application)  # 버튼 클릭 시 이벤트 핸들러 연결

        layout.addWidget(btn2)  # 레이아웃에 버튼 추가


        self.setLayout(layout)  # 레이아웃 설정


    def buttonClicked(self, index):

        print('Button', index, 'Clicked!')

    def quit_application(self):
        # 강제 종료 다이얼로그 표시
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
