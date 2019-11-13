from dictionaries import *
from tools import *
from dictionaries import Cyrillic_Arabic


def convert_to_Arabic(filein, fileout):
    text = []
    try:
        with open(filein, 'r', encoding="utf-8") as file:
            for line in file:
                text.append(line.replace('\ufeff', ''))
    except IOError:
        print("文件错误或不存在!")
        return 0

    text.reverse()
    output = []
    while text.__len__() > 0:
        buffer = text.pop().split(' ')
        convertedText = ''
        convertedWord = ''
        blockCounter = 0
        for word in buffer:
            length = len(word)
            flag_jingixke = False
            flag_drop_mark = False
            for j in range(0, 10):
                if word.__contains__(Jingixke_Cyrillic[j]):
                    flag_jingixke = True

            for i in range(0, 7):
                if word.__contains__(drop_mark[i]):
                    flag_drop_mark = True
                    break

            # print( word.lower().__contains__('ия'))
            if word.lower().__contains__('ия'):
                newWord = ''
                for i in range(0, length - 1):
                    if word[i] == 'и' and word[i + 1] == 'я':
                        newWord = word[0:i] + word[i + 1:length]
                        word = newWord
                        length = length - 1

            if flag_jingixke:
                if flag_drop_mark:
                    convertedWord = ''
                else:
                    convertedWord = 'ء'
                for i in range(0, length):
                    if Jingixke_Cyrillic.__contains__(word[i]):
                        convertedWord += Jingixke.get(word[i])
                        continue
                    else:
                        convertedWord += Cyrillic_Arabic.get(word[i], word[i])
                convertedWord += ' '

            else:
                convertedWord = ''
                for i in range(0, length):
                    convertedWord += Cyrillic_Arabic.get(word[i], word[i])
                convertedWord += ' '
            if convertedWord == ' ':
                blockCounter += 1
            else:
                blockCounter = 0
            if blockCounter <= 10:
                convertedText += convertedWord
        output.append(convertedText)
    writefile(output, fileout)

# convert_to_Arabic()
