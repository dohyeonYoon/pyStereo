'''
Client Device
(Capture images from both camera lens and send to calculate server by ftp protocol)
'''

import cv2
import pyrpc
import os
from datetime import datetime

def capture_img():

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

    # Save captured images to archive folder.
    file_name = datetime.today().strftime("%Y_%m_%d_%H_%M_%S")
    left_image_path = os.path.join('./archive/stereoL/', f'{file_name}_L.png')
    right_image_path = os.path.join('./archive/stereoR/', f'{file_name}_R.png')
    cv2.imwrite(left_image_path, left_frame)
    cv2.imwrite(right_image_path, right_frame)

    return left_frame, right_frame

def calculate_depth(left_frame, right_frame):
    
    # Depth estimation with both images in calculate server.
    result = pyrpc.call("main", imgL=left_frame, imgR=right_frame)

if __name__ == "__main__":
    capture_img()
    calculate_depth()
    


