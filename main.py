from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_words():
    words = bot.find_element_by_id('words').text
    return words


url = 'https://monkeytype.com/'

bot = webdriver.Chrome(
    executable_path='chromedriver.exe')

bot.get(url)
bot.implicitly_wait(5)

inputBox = bot.find_element_by_id('wordsInput')

para = get_words().split('\n')
for word in para:
    inputBox.send_keys(word+' ')


def find_init_idx_p1(word, para, n):
    return len(para)-1 - [i for i, n in enumerate(para[::-1]) if n == word][n]


def find_end_idx_p2(word, para, n):
    return [i for i, n in enumerate(para) if n == word][n]


while True:
    para2 = get_words().split('\n')
    print('Para1 : {}\n\nPara2: {}\n'.format(para, para2))

    init_idx_p1 = find_init_idx_p1(para2[0], para, 0)
    end_idx_p1 = len(para)-1
    init_idx_p2 = 0
    end_idx_p2 = find_end_idx_p2(para[end_idx_p1], para2, 0)

    size1 = end_idx_p1 - init_idx_p1
    size2 = end_idx_p2 - init_idx_p2

    while(size1 != size2):
        print('entered while loop')

        occurence = 1

        if (size1 < size2):
            init_idx_p1 = find_init_idx_p1(para2[0], para, occurence)
        else:
            end_idx_p2 = find_end_idx_p2(para[end_idx_p1], para2, occurence)

        size1 = end_idx_p1 - init_idx_p1
        size2 = end_idx_p2 - init_idx_p2

        occurence += 1

    para2 = para2[(size1+1):]
    print('Edited para2 : {}\n\n'.format(para2))

    for word in para2:
        inputBox.send_keys(word+' ')

    para = para2
