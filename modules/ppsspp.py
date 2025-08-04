import ctypes
from ctypes import wintypes

user_memory_address = 0x8800000


def wm_get_base_pointer(l_param, win_id):
    send_message_w = ctypes.windll.user32.SendMessageW
    send_message_w.restype = wintypes.LPARAM
    hwnd = int(win_id)
    result = send_message_w(hwnd, 0xB118, 0, l_param)
    return result


def get_memory_base_address(win_id):
    reply0 = wm_get_base_pointer(0, win_id)
    reply1 = wm_get_base_pointer(1, win_id)

    if reply0 != "FAIL" and reply1 != "FAIL":
        return (reply1 << 32) + reply0
