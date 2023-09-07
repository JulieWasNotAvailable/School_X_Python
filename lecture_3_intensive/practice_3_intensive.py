#ввод - любое целое число
#вывод - корень этого числа, если он целый
#если такого нет "трудно, не могу"

a = 0
def guess(num: int):
    for i in range (1,num+1):
        a = i*i
        if num == a:
            return(i)
        elif i>num/2:
            return "Не могу"

print (guess(int(input("Квадрат какого числа хотите взять: "))))