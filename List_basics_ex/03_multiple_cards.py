cards = input().split()
team_A = 11
team_B = 11
my_list = []
for card in cards:
    if card not in my_list:
        my_list.append(card)
        if card[0] == "A":
            team_A -= 1
        elif card[0] == "B":
            team_B -= 1
    if team_A<7 or team_B<7:
        print(f"Team A - {team_A}; Team B - {team_B}")
        print(f"Game was terminated")
        break
else:
    print(f"Team A - {team_A}; Team B - {team_B}")