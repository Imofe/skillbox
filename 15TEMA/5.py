films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов','Мементо', 'Отступники', 'Деревня']
favorite_films = []
films_number = int(input('Сколько фильмов хотите добавить? '))

for i in range(1, films_number + 1):
    movie = input('Введите название фильма: ')
    while movie not in films:
        print(f'Ошибка: фильма {movie} у нас нет!')
        movie = input('Введите название фильма: ')
    else:
        favorite_films.append(movie)
        
print('\nВаш список любимых фильмов: ')
print(favorite_films)
