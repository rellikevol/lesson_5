class Player:

    def __init__(self, money):
        self.__start_money = money
        self.__money = money
        self.__winnings = 0
        self.__games = 0
        self.__wins = 0
        self.__losses = 0

    @property
    def games(self):
        return self.__games

    def win(self, bid):
        self.__games += 1
        self.__wins += 1
        self.__winnings += bid
        self.__money += bid

    def loss(self, bid):
        self.__games += 1
        self.__losses += 1
        self.__winnings -= bid
        self.__money -= bid

    def is_bid_correct(self, bid):
        if bid <= self.__money:
            return True
        else:
            return False

    def end(self):
        print(f'Вы сыграли {self.__games} раз, {self.__wins} раз выйграли и '
              f'{self.__losses} раз проиграли, заработав {self.__winnings}.\n'
              f'Вы начали с суммы в {self.__start_money}, '
              f'а теперь ваш счёт составляет {self.__money}.\nЗаходите ещё!')

    def __str__(self):
        return f'Ваш счёт: {self.__money}, Выйгрыш: {self.__winnings},' \
               f' Игр: {self.__games}, Выйгрышей: {self.__wins}, Пройгрышей: {self.__losses}'