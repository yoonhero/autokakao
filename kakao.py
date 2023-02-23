import time
import applescript
from utils import copy_text

class KakaoAutomation():
    def __init__(self, is_mac=False):
        self.mac = is_mac

    def open_kakao(self):
        if not self.mac:
            raise NotImplemented("Please Waiting")

        start = time.time()
        print("Try Opening Kakao Application in Mac...")

        open_command = f"""\
        tell application "KakaoTalk"
            reopen -- unminimizes the first minimized window or makes a new default window
            activate (first window whose name is "카카오톡") -- makes the app frontmost
        end tell
        """
        _ = applescript.run_applescript(open_command)  

        end = time.time()
        print(f"⭐️ Finished in {(end-start)*1000:.4f}ms ⭐️")


    def open_chatroom(self, chatroom_name: str) -> None:
        if not self.mac:
            raise NotImplemented("Please Waiting")

        copy_text(chatroom_name, self.mac)
        time.sleep(0.4)

        start = time.time()
        print("Open Chatroom in Kakao App...")
        
        command = f"""\
        tell application "System Events" to key code 19 using command down -- activate main window
        delay 0.3
        tell application "System Events" to key code 3 using command down
        delay 0.3
        tell application "System Events" to key code 9 using command down
        delay 1.2
        tell application "System Events" to key code 125
        delay 0.7
        tell application "System Events" to key code 36
        """
        _ = applescript.run_applescript(command)

        time.sleep(0.4)

        end = time.time()
        print(f"⭐️ Finished in {(end-start)*1000:.4f}ms ⭐️")


    def write_message(self, message: str) -> None:
        if not self.mac:
            raise NotImplemented("Please Waiting")

        start = time.time()
        print("Writing Message...")

        # Copy Message and Paste it on the Chatroom Message Box.
        copy_text(message, self.mac)
        time.sleep(0.4)

        write_command = """\
            tell application "System Events" to tell application process "KakaoTalk"
                keystroke "v" using command down
                key code 36
            end tell
        """
        _ = applescript.run_applescript(write_command)

        end = time.time()
        print(f"⭐️ Finished in {(end-start)*1000:.4f}ms ⭐️")
