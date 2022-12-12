def get_winners(players, min_score):
    winners = []
    current_number = 0
    for player in players:
        player_data = player.split()
        if player_data[2] > min_score:
            current_number += 1
            winners.append(player_data)
    winners.sort(key=lambda x: x[2], reverse=True)
    return winners


def get_second_tour(winners):
    answer = str(len(winners)) + '\n'
    for winner in winners:
        answer += f'{len(winners)}) {winner[1][0]}. {winner[0]} {winner[2]}\n'
    passed = open('22tema/second_tour.txt', 'w', encoding='utf8')
    passed.write(answer)
    passed.close()


results = open('22tema/first_tour.txt', 'r', encoding='utf8')
lines = list(results.readlines())
results.close()

min_score = lines[0][:-1]
players = []

for line in lines[1:]:
    players.append(line[:-1])

get_second_tour(get_winners(players, min_score))