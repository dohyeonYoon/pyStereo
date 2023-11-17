'''
Client Device working code
(Capture images from both camera lens and send to cloud server by rpc method)
'''

import cv2
import pyrpc
import asyncio
import os
import datetime

def capture_img():
    ''' 양쪽 카메라 렌즈에서 이미지를 캡처하고 저장하는 코드'''
    # Open the left and right cameras.
    left_cam = cv2.VideoCapture(1)
    right_cam = cv2.VideoCapture(0)

    # Set the resolution for each camera.
    left_cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    left_cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    right_cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    right_cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    # Capture images from both cameras.
    ret_left, left_frame = left_cam.read()
    ret_right, right_frame = right_cam.read()
    return left_frame, right_frame


async def calculate_depth(left_frame, right_frame, serial_num):
    '''클라우드 서버에서 스테레오 깊이추정 함수를 원격호출'''
    # Depth estimation with both images in cloud server.
    with pyrpc.Client('localhost', 5000) as client:
        await client.call_async('main', serial_num, left_frame, right_frame)


async def main():
    # Set camera serial number.
    serial_num = '0001'
    while True:
        current_time = datetime.datetime.now()
        # Calculate next o'clock.
        next_hour = (current_time + datetime.timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
        # Wait until o'clock.
        await asyncio.sleep((next_hour - current_time).total_seconds())
        # Run every o'clock.
        left_frame, right_frame = await capture_img()
        await calculate_depth(left_frame, right_frame, serial_num)

if __name__ == "__main__":
    asyncio.run(main())


