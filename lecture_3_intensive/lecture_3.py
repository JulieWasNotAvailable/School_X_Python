#строковые переменные

import string

'''
new_name: str = input ('type name: ')
greet_message: str = "hello bob"
greet_message = greet_message.replace(' bob ', f' {new_name} ' )
print(greet_message)


river: str = 'mmississippi'
print(
    'm'+ river.lstrip("m") #но если ввести misp, удалит всё слово, пока не найдёт сочетние полностью
)
#rstip, чтобы начинать справа

words: str = "<!---da da da---!>"

print(
    words.strip('<!>-').split()
)
'''


"""

#задача очистить уродливую стрингу "hel1lo 123 b012ob"
#импорты в начале, пустой строкой разделяются локальные файлы

numbers: str = string.digits

word: str = "hel1lo 123 b012ob"

#1 вариант решения
for number in numbers:
    word = word.replace(number,'')


#2 вариант решения
_word: str = ""
for ch in word:
    if ch in numbers:
        continue
    else:
        _word += ch
        
word = _word
del _word
        
print (word)
"""

#words: str = "Hello Bob, are you a bob? BOB!!"
#words = words.lower().replace('bob', 'gregory')

words: str = "Hello Bob, are you a bob? BOB!!"
#words = words.lower().replace('bob', 'gregory')

_word = ""
while True:
    bob_index = words.lower().find('bob')
    if bob_index == -1:
        break
    else:
        words = (
            words = words[:bob_index] + "Gregory" + word[bob_index+len('bob')]
            #сначала берёт строку от 1 до 6, потом вставляет грегори, и потом с девяти до конца продолжает строку
        )
print (
    words
)

#words.find("bob") найдёт индекс слова bob, но только первого, и сразу остановится
_list: list = list[1,2,3]

#если стр не изменяется, почему мы можем делать реплэйс?
#set для уникальных?
#откуда подчёркивание в задачке про боба что неправильно
#args kwargs как выглдятя
#как комментировать несколько строк одновременно?

# :q! чтобы выйти из вима
