from common.Player import Player
from common.Game import Game


class UserInteraction:
    def __init__(self):
        self.main_menu = "--- Escoja una opción ---\n" + \
                         "1.- Jugar\n" + \
                         "2.- Salir\n"

        self.player_1 = None
        self.player_2 = None

    def start(self):
        try:
            option = int(input(self.main_menu))

            if option == 1:
                self.play()
            elif option == 2:
                exit()
            else:
                print("Debe escojer una opción dentro del rango preestablecido")
                self.start()
        except ValueError:
            print("Debe de introducir un número")
            self.start()

    def play(self):
        self.assign_data()
        game = Game(self.player_1, self.player_2)
        game.start()
        self.start()

    def assign_data(self):
        self.player_1 = Player(input("Ingrese un apodo para el jugador 1:\n"))
        self.player_1.symbol = 'X'
        self.player_2 = Player(input("Ingrese un apodo para el jugador 2:\n"))
        self.player_2.symbol = 'O'

        if self.player_1.name == "" or self.player_2.name == "":
            print("Los apodos no pueden quedar vacios, por favor vuelva a ingresarlos")
            self.assign_data()
