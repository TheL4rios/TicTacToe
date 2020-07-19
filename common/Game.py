import random


class Game:
    def __init__(self, player_1, player_2):
        self.turns = 0
        self.win = False
        self.player_1 = player_1
        self.player_2 = player_2
        self.turn = None
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def start(self):
        self.turn = self.get_turn()
        while not self.win:
            self.turns += 1
            self.show_table()
            print("Turno de: ", self.turn.name, " - ", self.turn.symbol)
            position = self.get_position()

            self.board[position] = self.turn.symbol

            if self.analyze_table(self.turn):
                self.win = True
                self.show_winner()
            else:
                if self.turns == 9:
                    self.win = True
                    print("Empate :/")
                else:
                    self.turn = self.get_turn()

    def show_winner(self):
        self.show_table()
        print("Ganó: ", self.turn.name, " :D")

    def analyze_table(self, player):
        symbol = player.symbol
        if self.board[0] == symbol and self.board[1] == symbol and self.board[2] == symbol or \
                self.board[3] == symbol and self.board[4] == symbol and self.board[5] == symbol or \
                self.board[6] == symbol and self.board[7] == symbol and self.board[8] == symbol or \
                self.board[0] == symbol and self.board[3] == symbol and self.board[6] == symbol or \
                self.board[1] == symbol and self.board[4] == symbol and self.board[7] == symbol or \
                self.board[2] == symbol and self.board[5] == symbol and self.board[8] == symbol or \
                self.board[0] == symbol and self.board[4] == symbol and self.board[8] == symbol or \
                self.board[2] == symbol and self.board[4] == symbol and self.board[6] == symbol:
            return True
        else:
            return False

    def get_position(self):
        try:
            position = int(input('''
Inserte el número de la posición:\n
            1 | 2 | 3
            4 | 5 | 6
            7 | 8 | 9\n
            '''))

            if 1 <= position <= 9:
                if self.board[position - 1] == ' ':
                    return position - 1
                else:
                    print("Escoge otro lugar, ese ya ha sido seleccionado")
                    return self.get_position()
            else:
                print("la fila debe de estar dentro del valor 0 y 2")
                return self.get_position()
        except ValueError:
            print("Debe de insertar un número")
            return self.get_position()

    def get_turn(self):
        if self.turn is None:
            rnd = random.randint(0, 1)

            if rnd == 0:
                return self.player_1
            else:
                return self.player_2
        else:
            if self.turn.name == self.player_1.name:
                return self.player_2
            else:
                return self.player_1

    def show_table(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("----------")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("----------")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])
