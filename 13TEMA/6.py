def stop(a, b):
    count = 0
    while a > b:
        a -= (a * 8.4 / 100)
        count += 1
    return count


start_ampl = float(input('Введите начальную амплитуду: '))
stop_ampl = float(input('Введите амплитуду остановки: '))
while (start_ampl < 0) or (stop_ampl < 0) or (start_ampl <= stop_ampl):
    print('Начальная амплитуда и амплитуда остановки должны быть больше нуля.\nТак же начальная амплитуда должна быть больше амплитуды остановки.')
    start_ampl = float(input('Введите начальную амплитуду: '))
    stop_ampl = float(input('Введите амплитуду остановки: '))
print(f'Маятник считается остановившимся через {stop(start_ampl, stop_ampl)} колебаний.')