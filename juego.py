import random


class Game:
    def __init__(self):
        self.size = None
        self.board = None

    def SelectSizeGame(self, size):
        if type(size) != int or size < 3:
            raise ValueError("No es int o el tamaño es menor a 3")
        self.size = size
        self.board = [[random.randint(0, 1) for _ in range(self.size)] for _ in range(self.size)]
        
    def CheckWin(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] == 1:
                    return 0
        return 1
            
    def get_board(self):
        return self.board

    def change_pos(self, x, y):
        cambio = 0
        if self.board[x][y] == 0:
            cambio = 1
        
        self.board[x][y] = cambio
        
    def set_ady(self, x, y):
        if x >= self.size or x < 0 or y >= self.size or y < 0:
            raise ValueError("Estás intentando insertar un valor por fuera de la matriz")
        previus = None
        later = None
        superior = None
        inferior = None
        if self.board is None:
            raise ValueError("El tablero no ha sido inicializado. Llama a SelectSizeGame primero.")
        if x >= self.size - 1:
            previus = x - 1
            self.change_pos(previus, y)
        if x <= 0:
            later = x + 1
            self.change_pos(later, y)
        if y <= 0:
            inferior = y + 1
            self.change_pos(x, inferior)
        if y >= self.size - 1:
            superior = y - 1
            self.change_pos(x, superior)
        if 0 < x < self.size - 1:
            later = x + 1
            previus = x - 1
            self.change_pos(later, y)
            self.change_pos(previus, y)
        if 0 < y < self.size - 1:
            inferior = y + 1
            superior = y - 1
            self.change_pos(x, inferior)
            self.change_pos(x, superior)
        self.change_pos(x, y)
        
        
    def get_pos(self, x, y):
        return self.board[x][y]