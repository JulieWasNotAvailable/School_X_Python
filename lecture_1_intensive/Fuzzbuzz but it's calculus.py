a = int(input("До скольки считать? Введите число: "))
t: int = a//3
f: int = a//5
ft: int = a//15
threes = ((2*3+3*(t-1))/2)*t
fives = ((2*5+5*(f-1))/2)*f
fifteens = ((2*15+15*(ft-1))/2)*ft
print(threes, " ", fives, " ", fifteens, " ")
sum = threes + fives - fifteens
print(sum)
