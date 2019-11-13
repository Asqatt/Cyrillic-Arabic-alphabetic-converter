from to_cyrillic import *
from to_Arabic import *
from tools import *

heading()
while True:
    instruction = input()
    if instruction.upper() == 'A':
        Cyrillic_Arabic()
        while True:
            ins = input().split(" ")
            if ins[0].upper() == 'R':
                heading()
                break
            elif ins.__len__() == 2:
                convert_to_Arabic(ins[0], ins[1])
            else:
                print("指令有误！")
    elif instruction.upper() == 'C':
        Arabic_Cyrillic()
        while True:
            ins = input().split(" ")
            if ins[0].upper() == 'R':
                heading()
                break
            elif ins.__len__() == 2:
                convert_to_Cyrillic(ins[0], ins[1])
            else:
                print("指令有误！")
    elif instruction.upper() == 'H':
        pass
    elif instruction.upper() == 'Q':
        break
    else:
        print("  指令有误！ ")
