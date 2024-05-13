import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

def buttonClicked(self):
    print('Button Clicked!')

app = QApplication(sys.argv)
window = QWidget()
# 창 위치와 크기 설정
window.setGeometry(100, 100, 300, 200)   
# 창 제목 설정 
window.setWindowTitle('PyQt5 Button Example')  
# 버튼 생성
btn = QPushButton('Click Me!', window)
btn.setGeometry(100, 50, 100, 30)  # 버튼 위치와 크기 설정
# 버튼 클릭 시 이벤트 핸들러 연결
btn.clicked.connect(buttonClicked)

window.show()
# 이벤트 루프 생성
sys.exit(app.exec_())