def writefile(txt, fileout):
    with open(fileout, 'w', encoding="utf-8") as file:
        for line in txt:
            file.writelines(line)
    print(f"已成功写入为:{fileout} ！")


def heading():
    print("*" * 70)
    cstr = '西里尔字母-阿拉伯字母转换器'
    print(cstr.center(58, ' '))
    guide()
    print("*" * 70)


def Arabic_Cyrillic():
    print("*" * 70)
    cstr = 'Arabic--->Cyrillic    : 指令格式：输入文件名.txt 输出文件名.txt'
    print(cstr.center(58, ' '))
    print(" " * 20 + ' 返回上一层按R' + " " * 10)
    print("*" * 70)


def Cyrillic_Arabic():
    print("*" * 70)
    cstr = 'Cyrillic--->Arabic    : 指令格式：输入.txt 输出文件名.txt'
    print(cstr.center(58, ' '))
    print(" " * 20 + ' 返回上一层按R' + " " * 10)
    print("*" * 70)


def guide():
    print(" " * 18 + ' 西里尔字母--->阿拉伯字母 ：按 A或a' + " " * 10)
    print(" " * 18 + ' 阿拉伯字母--->西里尔字母 ：按 C或c' + " " * 10)
    print(" " * 18 + '          退出          ：按 C或c' + " " * 10)


