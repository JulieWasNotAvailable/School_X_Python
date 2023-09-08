def divergent_seeker():
    ind_list = []
    index = 0
    str_values = input("gimme some numbers with commas and spaces pls (NO SPACES AT THE END!!!): ")
    num_list = list(map(int, str_values.split(' ')))
    print(num_list)
    for num in num_list:
        if num_list[index + 1] - num_list[index] != 1:
            ind_list.append(index+1)
        elif num_list[index + 1] - num == 1:
            continue
        index = index + 1
    return ind_list


print("here are indexes of divergent numbers: ", divergent_seeker())
