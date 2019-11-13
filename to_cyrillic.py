from dictionaries import arabic_cyrillic_A, arabic_cyrillic_B
from tools import *


def readfile(filein):
    with open(filein, 'r', encoding="utf-8") as file:
        txt = file.readlines()
    return txt


def convert_to_Cyrillic(filein, fileout):
    # print('Enter/Paste your content. Ctrl-D to save it.')
    text = []
    try:
     with open(filein, 'r', encoding="utf-8") as file:
        for line in file:
            text.append(line.replace('\ufeff', ''))
    except IOError:
        print("文件错误或不存在!")
        return 0

    text.reverse()
    changers = ['ء', 'گ', 'ە', 'ك']
    output = ''
    while text.__len__() > 0:
        buffer = text.pop().split(' ')
        # print(buffer)
        convertedText = ''
        flag_for_upper = 1
        for word in buffer:
            flag_for_Jinhixke = False

            length = len(word)
            convertedWord = ''
            for letter in changers:
                if word.__contains__(letter):
                    flag_for_Jinhixke = True

            if flag_for_Jinhixke == True:
                for i in range(0, length):
                    if i == 0 and flag_for_upper == 1:
                        convertedWord += arabic_cyrillic_A.get(word[i], word[i]).upper()
                    else:
                        convertedWord += arabic_cyrillic_A.get(word[i], word[i])
                convertedText += convertedWord + ' '

            else:
                for i in range(0, length):
                    if i == 0 and flag_for_upper == 1:
                        convertedWord += arabic_cyrillic_B.get(word[i], word[i]).upper()
                    else:
                        convertedWord += arabic_cyrillic_B.get(word[i], word[i])
                convertedText += convertedWord + ' '

            for mark in ['.', '؟', '!']:
                if word.__contains__(mark):
                    flag_for_upper = 1
                    break
                else:
                    flag_for_upper = 0
        output += convertedText

    writefile(output, fileout)

# convert_to_Cyrillic()
