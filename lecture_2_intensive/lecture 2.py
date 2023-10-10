#что такое парсинг?

#хранить в списках только переменные
#в Питоне множества не упорядоченные, называются сетами

#_set1: set = {a, b, c, d}
#print (_set1)

#set1.intersection(set2)
#может быть полезно, если

"""
abc = list ("abc")
print (abc)
numbers: list = [1, 2, 3, 4, 5, 6, 7]
"""

#вы двигаетесь по списку пока он не закончится
'''
for n in numbers:
    if n%2 == 0:
        print (f"Число - {n} четное"
           )
    else:
        print (f"Число - {n} нечетное")
'''
'''
for n in numbers:
    if n % 3 == 0 and n % 5 == 0:
        print(f"Число - {n} четное"
          )
    elif n % 3 == 0:
        print()
    elif n % 5 == 0:
        print ()
        
    else:
        print(f"Число - {n} нечетное")
        '''
#от более сложного условия идём к более простому
'''
word: str = input("Введите слово: ")
vowel: str = "aeiouy"
vowel_count: int = 0
for char in word: #цикл будет итерироваться по строке 
    if char in vowel:
        vowel_count += 1
    print (char)
'''
# range это не список, а генератор. он не возвращает список, он возвращает генератор, который выдаёт числа при просьбе
n: int = int(input("N: "))

"""
array: list = list(range(n))
i = 0
while True:
    if array[i] % 123 == 0:
        print (array[i], "делится")
        break
    i += 1         #i = 1 +1 для более сложных итераций 
"""

"""n: int = int(input("N: "))
while n>0:
    print (n)
    n=n-1
"""