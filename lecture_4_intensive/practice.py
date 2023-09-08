import import_this as race

winners: list = []

for key, value in race.RACE_DATA.items():
    winners.append(race.RACE_DATA.get(key).get('FinishedPlace'))

winners_names: list = []
winners_teams: list = []
winners_scores: list = []

for winner in winners[0:3]:
    winners_names.append(race.RACE_DATA.get(winner).get('RacerName'))
    winners_teams.append(race.RACE_DATA.get(winner).get('RacerTeam'))
    winners_scores.append(race.RACE_DATA.get(winner).get('FinishedTimeSeconds'))

print(f"Выиграл {winners_names[0]}!!!Поздравляем!")
print("_"*(len(f"Выиграл {winners_names[0]}!!!Поздравляем!")))

places_list = [1,2,3]
print()
print("Первые три места:")
print()

for place in places_list:
    print(f"Гонщик на {place} месте:")
    print(f"\tИмя: {winners_names[place-1]}")
    print(f"\tКоманда: {winners_teams[place-1]}")

    time: int = winners_scores[place-1]
    hours: int = time // 3600
    minutes: int = time % 3600 // 60
    seconds: int = time - hours * 3600 - minutes * 60
    print(f"\tВремя: {hours}:{minutes}:{seconds}")
    print()

# def find_winners (): #прописать аргументы
#     racerplace1: str = race.RACE_DATA.get(1).get('FinishedPlace')
#
#     for key, value in RACE_DATA.items():
#         print(RACE_DATA.keys)
