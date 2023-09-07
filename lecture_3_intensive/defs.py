"""
def my_personal_sum(

        x: int | float,
        y: int | float,
) -> int | float
    answer = x + y
    return answer
"""

def my_personal_sum(
        num_list: list

) -> int | float
    for num in num_list:
        answer += num
    return answer

def my_personal_sum(*args, **krawgs) -> int | float:
    for num in num_list:
        answer += num
    return answer

#* - распаковка, разворачиваает элемент
#**kwargs - dictionary, *args
#позиционные указываются в начале

print (my_personal_sum(3, 5))
print (sum([3, 5])) #sum по списку работает