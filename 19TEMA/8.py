max_numbers = int(input('Введите максимальное число: '))
numbers = set(range(1, max_numbers + 1))
while True:
    guess = input('Нужное число есть среди вот этих чисел: ')
    if guess == 'Помогите!':
        break
    if input('Ответ Артёма: ') == 'Да':
        numbers &= {int(x) for x in guess.split()}
    else:
        numbers -= {int(x) for x in guess.split()}

print(*numbers)