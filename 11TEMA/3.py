size = float(input('Укажите размер файла для скачивания: '))
speed = float(input('Какова скорость вашего соединения? '))

time_download = round(size / speed)
download = 0
percent = 0

for time in range(1, time_download + 1):
    download += speed
    percent = round(download / size * 100)
    if time == time_download:
        download = size
        percent = 100
    print(f'Прошло {time} сек. Скачано {round(download)} из {round(size)} Мб ({str(percent)}%)')