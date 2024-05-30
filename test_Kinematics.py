#기구학/역기구학 라이브러리
import cv2
import numpy as np
import time

from pymycobot.mycobot import MyCobot

# import move_gripper as mg
# import detect_obj as do


def sync_send_coords(self, coords, speed, mode=0, timeout=15):
    """
    동기화 상태로 좌표를 보내고 대상 지점에 도달할 때까지 기다립니다.

    Args:
        coords: 좌표 값의 리스트(List[float]).
        speed: 이동 속도를 나타내는 정수, 0에서 100 사이의 값을 가집니다.
        mode: 이동 모드를 나타내는 정수:
              0 - 각도(기본값),
              1 - 선형.
        timeout: 타임아웃 기간(초), 기본값은 15초입니다.

    Returns:
        self: 현재 객체의 인스턴스.
    """
    t = time.time()  # 현재 시간 기록.
    self.send_coords(coords, speed, mode)  # 좌표를 장치에 보냄.

    # 대상 지점에 도달하거나 타임아웃이 발생할 때까지 계속 반복.
    while time.time() - t < timeout:
        if self.is_in_position(coords, 1) == 1:  # 대상 지점에 도달했는지 확인.
            break  # 도달하면 루프를 종료.
        time.sleep(0.1)  # 다시 확인하기 전에 잠시 대기.

    return self  # 현재 객체의 인스턴스를 반환.


# 예제 코드
mc = MyCobot('COM3',115200)
#                [5, -15, -15, -35, 90, 90],
#                [20, -22, -34, -23, 87, 105],
#                [5, -15, -15, -35, 90, 90],
#                [0, 0, 0, 0, 0, 0],

# #mc.send_angles([34.45, -35.59, 2.37, -60.55, 95.51, 125.15], 20)
mc.send_angles([0, 0, 0, 0, 0, 0], 20)
# # #mc.send_angles([-90, -15, -15, -15, 90, -90], 35)
# # #mc.send_angles([5, -15, -15, -35, 90, 90], 35)
time.sleep(3)
coords = mc.get_coords()
angles = mc.get_angles()
time.sleep(0.1)
print("angles:",angles)
print("coords:",coords)


#coords = [-2.9, -153.3, 523.8, -90.0, 1.31, -179.73] # 원점 좌표
#coords = [-220, -110, 250, -170, 0, 95]
# coords= [-86.6, -288.1, 268.5, -179.81, -2.54, -90.0]  #50 70[-202, -159, 280, -170, 0, 95]
# mc.sync_send_coords(coords, 15, 0, 1)
# time.sleep(1)
# coords = mc.get_coords()
# angles = mc.get_angles()
# time.sleep(0.1)
# print("coords:",coords)
# print("angles:",angles)

        # t.lx, t.ly, t.lz, t.ax, t.ay, t.az = [-85.6, -288.5, 268.1, 179.91, -2.46, -89.73]
        # mc.sync_send_coords([t.lx, t.ly, t.lz, t.ax, t.ay, t.az], 50, 0, 1)
        # time.sleep(4)
        # t.lx, t.ly, t.lz, t.ax, t.ay, t.az = [0.7, -153.2, 523.8, -90.0, 0.35, -179.73]

#
"""
mc.get_coords() : 현재 엔드 이펙터의 좌표를 구해주는 함수
mc.send_coords() : 좌표를 입력하면 그 위치로 엔드 이펙터를 이동시킴
mc.sync_send_coords(coords, speed, timeout)  # 좌표(coords)로 엔드 이펙터를 이동시키나 타임아웃 기능이 있음(위 함수 참고.)

다른 코드에서 참조할 때는 from Kinematics import * ㄱㄱ

"""