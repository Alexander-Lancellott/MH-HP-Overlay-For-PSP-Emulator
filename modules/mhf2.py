import re
from time import time
from math import ceil
from ahk import AHK
import pymem

from modules.utils import read_int, max_monsters, current_game
from modules.ppsspp import user_memory_address, get_memory_base_address
from modules.monsters_mhfu import MonstersMHFU

initial_pointer = {
    "ULES00851": 0x127AD70,
    "ULUS10266": 0x12799F0,
    "ULJM05156": 0x1278E70,
}


def get_mhf2_data(pid, base_address, game_id, show_small_monsters=True):
    large_monster_results = []
    small_monster_results = []

    address = base_address + user_memory_address + initial_pointer[game_id]

    large_monsters = MonstersMHFU.large_monsters
    small_monsters = MonstersMHFU.small_monsters if show_small_monsters else {}

    process_handle = pymem.process.open(pid)

    for i in range(0, max_monsters):
        offset = 0x4 * i
        p0 = read_int(process_handle, address + offset, 4)
        if p0 != 0:
            p1 = p0 + base_address
            abnormal_status = {}

            def add_abnormal_status(status_name: str, values: list):
                if values[1] != 0xFFFF:
                    abnormal_status.update({
                        status_name: values,
                    })

            name = read_int(process_handle, p1 + 0x1E8, 1)
            hp = read_int(process_handle, p1 + 0x2E2)
            max_hp = read_int(process_handle, p1 + 0x41E)
            if large_monsters.get(name):
                size = read_int(process_handle, p1 + 0x274)
                add_abnormal_status("Poison", [
                    read_int(process_handle, p1 + 0x388, 2),
                    read_int(process_handle, p1 + 0x450, 2)
                ])
                add_abnormal_status("Sleep", [
                    read_int(process_handle, p1 + 0x446, 2),
                    read_int(process_handle, p1 + 0x444, 2)
                ])
                add_abnormal_status("Paralysis", [
                    read_int(process_handle, p1 + 0x458, 2),
                    read_int(process_handle, p1 + 0x456, 2)
                ])
                add_abnormal_status("Dizzy", [
                    read_int(process_handle, p1 + 0x440, 2),
                    read_int(process_handle, p1 + 0x55E, 2)
                ])
                abnormal_status.update({
                    "Rage": int(ceil(
                        read_int(process_handle, p1 + 0x564, 2) / 60
                    ))
                })
                large_monster_results.append([name, hp, max_hp, size, abnormal_status, hex(p1), hex(address)])
            elif small_monsters.get(name) and show_small_monsters:
                small_monster_results.append([name, hp, max_hp, hex(p1), hex(address)])

    return {
        "monsters": large_monster_results + small_monster_results,
        "total": [len(large_monster_results), len(small_monster_results)]
    }


if __name__ == "__main__":
    class Test:
        start = time()
        ahk = AHK(version="v2")
        keys_regex = "|".join(map(re.escape, initial_pointer.keys()))
        target_window_title = fr"(?i)^PPSSPP v([\d.a-zA-Z]+) - ({keys_regex})\s*:"
        not_responding_title = r" \([\w\s]+\)$"
        win = None
        not_responding = ahk.find_window(
            title=target_window_title + not_responding_title, title_match_mode="RegEx"
        )
        if not not_responding:
            win = ahk.find_window(
                title=target_window_title, title_match_mode="RegEx"
            )
        if win:
            game = current_game(win.title)
            base_address = get_memory_base_address(win.id)

            print("base_address:", hex(base_address))
            print("base_address + user_memory_address:", hex(base_address + user_memory_address))

            data = get_mhf2_data(win.pid, base_address, game["id"])
            monsters = data["monsters"]
            for monster in monsters:
                if monster[2] > 5:
                    large_monster = MonstersMHFU.large_monsters.get(monster[0])
                    small_monster_name = MonstersMHFU.small_monsters.get(monster[0])
                    if large_monster:
                        print([large_monster["name"], *monster[1::], monster[0]])
                    if small_monster_name:
                        print([small_monster_name, *monster[1::], monster[0]])
        end = time()
        print(end - start)
    Test()
