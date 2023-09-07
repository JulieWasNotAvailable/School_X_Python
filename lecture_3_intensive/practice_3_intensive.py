#ввод - любое целое число
#вывод - корень этого числа, если он целый
#если такого нет "трудно, не могу"

a = 0
def guess(num: int):
    for i in range (1,9):
        a = i*i
        if num == a:
            return(i)
        if i>(num//2):
            print("Не могу")
            break
        else:
            continue

print (guess(int(input("Квадрат какого числа хотите взять: "))))