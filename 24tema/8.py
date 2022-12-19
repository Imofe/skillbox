import random


class Deck:
    def __init__(self, cost_card, name_card):
        self.cost_card = cost_card
        self.name_card = name_card


class Player:
    def __init__(self, name, points=0):
        self.name = name
        self.points = points


class Game:
    sum_points = 0

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play_one_turn(self, card_1, card_2):
        if self.sum_points > 21:
            cards[12].cost_card = 1
            self.player_1.points += card_1.cost_card
            self.player_2.points += card_2.cost_card
            print(self.player_1.points, card_1.name_card)
        else:
            self.player_1.points += card_1.cost_card
            self.player_2.points += card_2.cost_card
            self.sum_points = (self.player_1.points + self.player_2.points)
            print(self.player_1.points, card_1.name_card)

    def get_winner(self):
        if self.player_1.points > 21 and self.player_2.points > 21:
            print('Ничья. У обоих перебор.')
            print(f'{self.player_1.__name}, набрал {self.player_1.points} очков. {self.player_2.__name} набрал {self.player_2.points} очков.')
        elif self.player_1.points > 21 or self.player_2.points > self.player_1.points:
            print(f'Победил {self.player_2.__name}, набрав {self.player_2.points} очков. У {self.player_1.__name} {self.player_1.points} очков.')
        elif self.player_2.points > 21 or self.player_1.points > self.player_2.points:
            print(f'Победил {self.player_1.__name}, набрав {self.player_1.points} очков. У {self.player_2.__name} {self.player_2.points} очков.')
        elif self.player_1.points == self.player_2.points:
            print(f'Ничья! У обоих игроков {self.player_1.points} очков.')
        else:
            print('Нет победителей.')


cards = [Deck(2, 'Двойка'), Deck(3, 'Тройка'), Deck(4, 'Четвёрка'), Deck(5, 'Пятёрка'),
         Deck(6, 'Шестёрка'), Deck(7, 'Семёрка'), Deck(8, 'Восьмёрка'), Deck(9, 'Девятка'),
         Deck(10, 'Десятка'), Deck(10, 'Валет'), Deck(10, 'Дама'), Deck(10, 'Король'),
         Deck(11, 'Туз')]

player = Player('Игрок')
dealer = Player('Диллер')
game = Game(player, dealer)

for _ in range(2):
    game.play_one_turn(cards[random.choice(range(0, 12))], cards[random.choice(range(0, 12))])

while True:
    request = int(input('1 - ещё, 2 - хватит: '))
    if request == 1:
        game.play_one_turn(cards[random.randint(0, 12)], cards[random.randint(0, 12)])
    else:
        break
    if player.points > 21 or dealer.points > 21:
        break

game.get_winner()