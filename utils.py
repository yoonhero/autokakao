import pyperclip
import subprocess

def copy_text(text:str, is_mac:bool) -> None:
    if not is_mac:
        pyperclip.copy(text)
        return

    process = subprocess.Popen('pbcopy', env={'LANG': 'ko_KR.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(text.encode('utf-8'))

def get_copied_text(is_mac:bool) -> str:
    if not is_mac:
        x = pyperclip.paste()   
        return x

    return subprocess.check_output(
        'pbpaste', env={'LANG': 'ko_KR.UTF-8'}).decode('utf-8')

