# 그리퍼를 gripper_open_angle, gripper_open_speed로 여는 함수

from pymycobot.mycobot import MyCobot
import time

port = 'com3'
gripper_open_angle = 30
gripper_open_speed = 30
mc = MyCobot(port, 115200)

def gripper_open(angle, speed):
    mc.set_gripper_mode(0)
    mc.init_eletric_gripper()
    time.sleep(0.1)
    mc.set_eletric_gripper(1)
    mc.set_gripper_value(angle, speed)
    time.sleep(2)
    print("그리퍼가",angle,"도 만큼 열렸습니다.")



gripper_open(30, gripper_open_speed)

gripper_open(70, gripper_open_speed)

# gripper_open(30, gripper_open_speed)

# gripper_open(70, gripper_open_speed)

# gripper_open(10, gripper_open_speed)



 