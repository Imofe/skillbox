violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

time_summ = 0
count = int(input('Введите количество песен: '))
for i in range(count):
    songs_name = input(f'Название {i+1}-й песни: ')
    for songs in range(len(violator_songs)):
        if violator_songs[songs][0] == songs_name:
            time_summ += violator_songs[songs][1]

print()
print(f'Общее время звучания песен: {time_summ}')