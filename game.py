from random import randint, choice
from player import Player
from time import sleep


class Game:
    messages = ['Хотите сыграть? Y|N > ', 'Хотите сыграть ещё раз? Y|N > ', 'Добро пожаловать!', 'Я вас не понимаю...',
                'На какое число хотите поставить? > ', 'Такого слота нет...', 'Какой суммой рискнёте? > ',
                'Ставка принята!', 'К сожалению, у вас не хватает средств...', 'Ставка должнабыть больше 0...',
                'Крутим рулетку...', 'Вы выйграли ', 'Не повезло...']
    yes = ['Y', 'y']
    no = ['N', 'n']
    wait_time = 0.02
    count_of_symbols = 100
    symbol = '♪♫'

    def __init__(self, slots, multiply):
        self.__slots = slots
        self.__multiply = multiply
        self.__rules = f'Поставьте любую сумму на число от 1 до {self.__slots}, если вы отгадали - ' \
                       f'ваша выйгрыш умножается на {self.__multiply}, ' \
                       f'в случае пройгрыша вы потеряете сумму вашей ставки.'

    def __is_win(self, number: int):
        if number == randint(1, self.__slots + 1):
            return True
        else:
            return False

    def play(self, player: Player):
        print(Game.messages[2])
        while True:
            print(
                '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Рулетка $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
                '$$$$$$$$$')
            print(player)
            if player.games == 0:
                answer = input(Game.messages[0])
            else:
                answer = input(Game.messages[1])
            if answer in Game.yes:
                self.__main_game(player)
            elif answer in Game.no:
                player.end()
                exit(0)
            else:
                print(Game.messages[3])

    def __main_game(self, player: Player):
        print(self.__rules)
        number = input(Game.messages[4])
        if self.__check_number(number):
            bid = input(Game.messages[6])
            if bid.isdigit():
                bid = int(bid)
                if player.is_bid_correct(bid):
                    if bid != 0:
                        print(Game.messages[7])
                        Game.__wait(Game.wait_time, Game.count_of_symbols, Game.symbol)
                        if self.__is_win(int(number)):
                            player.win(bid * self.__multiply)
                            print(Game.messages[11], end='')
                            print(bid * self.__multiply)
                        else:
                            player.loss(bid)
                            print(Game.messages[12])
                    else:
                        print(Game.messages[9])
                else:
                    print(Game.messages[8])
            else:
                print(Game.messages[3])
        else:
            print(Game.messages[5])

    def __check_number(self, number):
        if not number.isdigit():
            return False
        elif int(number) < 1 or int(number) > self.__slots:
            return False
        else:
            return True

    @staticmethod
    def __wait(wait_time, count, symbol):
        print(Game.messages[10])
        for i in range(count):
            print(choice(symbol), end='')
            sleep(wait_time)
        print('')