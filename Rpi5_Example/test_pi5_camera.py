import cv2
from picamera2 import Picamera2

# Picamera2 객체 생성 및 설정
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

while True:
    # 카메라에서 이미지 캡처
    im = picam2.capture_array()

    # 이미지를 OpenCV 윈도우에 표시
    cv2.imshow("Camera", im)

    # 'q' 키를 누르면 루프 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 프로그램 종료 시 카메라 객체 해제 및 OpenCV 윈도우 종료
picam2.stop()
cv2.destroyAllWindows()