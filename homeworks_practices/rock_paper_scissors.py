def rock_paper_scissors():
    player_1, player_2 = input('Ввод: ').split(' ')
    if (player_1 or player_2) != ("камень" or "ножницы" or "бумага"):
        print("такого знака нет в игре, давай другой")
    elif player_1 == player_2:
        print("ничья")
    elif ((player_1 == "камень" and player_2 == "ножницы")
          or (player_1 == "ножницы" and player_2 == "бумага")
          or (player_1 == "бумага" and player_2 == "камень")):
        print("игрок 1 выиграл")
    else:
        print("игрок 2 выиграл")


rock_paper_scissors()

