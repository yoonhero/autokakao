import pyautogui
import pyperclip
import argparse
from kakao import KakaoAutomation

# importing the required packages
import pyautogui
import cv2
import numpy as np


while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    img.save("test.png")
    break


# # Predict Answer
# # Write an answer to chat 

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Process platform options.')
#     parser.add_argument('--mac', action='store_true', help='Set platform to macOS')
#     args = parser.parse_args()
    
#     kakao = KakaoAutomation(is_mac=args.mac)

#     kakao.open_kakao()
#     kakao.open_chatroom("윤승현")
#     kakao.write_message("안녕!!")

