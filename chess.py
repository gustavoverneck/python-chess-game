'''

    TERMINAL PYTHON CHESS GAME - by Gustavo Arruda Verneck, 2023.
                                    -> gustavoverneck@gmail.com
    
'''

'''
    TO-DO LIST: 
                - Verify if move is possible
                - Block impossible moves
                - Add turns for players
                - Smooth game's creashs: If input not valid, try again instead of breaking
                - Add Victory and Surrender
                - Add Castling

'''


class ChessGame:
    def __init__(self):
        print("\n --- Initializing chess game... ---\n")
        self.setupBoard()
        running = True
        self.rodada = 1
        while running:
            print("\n-------- Move {} --------\n".format(self.rodada))
            self.showBoard()
            self.playMove()


    def setupBoard(self):
        self.board = [[Piece("Empty", "Space") for i in range(8)] for j in range(8)]
        # Pawns
        for i in range(len(self.board[1])):
            self.board[1][i] = Piece("White", "Pawn")
        for i in range(len(self.board[6])):
            self.board[6][i] = Piece("Black", "Pawn")
        # Rooks
        self.board[0][0] = Piece("White", "Rook")
        self.board[0][7] = Piece ("White", "Rook")
        self.board[7][0] = Piece("Black", "Rook")
        self.board[7][7] = Piece("Black", "Rook")
        # Knights
        self.board[0][1] = Piece("White", "Knight")
        self.board[0][6] = Piece("White", "Knight")
        self.board[7][1] = Piece("Black", "Knight")
        self.board[7][6] = Piece("Black", "Knight")
        # Bishops
        self.board[0][2] = Piece("White", "Bishop")
        self.board[0][5] = Piece("White", "Bishop")
        self.board[7][2] = Piece("Black", "Bishop")
        self.board[7][5] = Piece("Black", "Bishop")
        # Queens
        self.board[0][3] = Piece("White", "Queen")
        self.board[7][4] = Piece("Black", "Queen")
        # Kings
        self.board[0][4] = Piece("White", "King")
        self.board[7][3] = Piece("Black", "King")

    def verifyMove(self, moveFrom, moveTo):
        if ( (moveFrom[0] >= 0) and (moveFrom[0] <= 7) and (moveFrom[1] >= 0) and (moveFrom[1] <= 7) and (moveTo[0] >= 0) and (moveTo[0] <= 7) and (moveTo[1] >= 0) and (moveTo[1] <= 7) ):
            return True
        else:
            return False
    
    def showBoard(self):
        print("  -  A B C D E F G H")
        str2 = ""
        for j in range(len(self.board)):
            for i in range(len(self.board)):
                match self.board[j][i].__str__(): # ♔ ♕ ♗ ♘ ♙ ♖ ♚ ♛ ♝ ♞ ♜ ♟ ▢
                    case "Empty Space":
                        str2 += " " + "▢"
                    case "White Pawn":
                        str2 += " " + "♟"
                    case "Black Pawn":
                        str2 += " " + "♙"
                    case "White King":
                        str2 += " " + "♚"
                    case "Black King":
                        str2 += " " + "♔"
                    case "White Queen":
                        str2 += " " + "♛"
                    case "Black Queen":
                        str2 += " " + "♕"
                    case "White Bishop":
                        str2 += " " + "♝"
                    case "Black Bishop":
                        str2 += " " + "♗"
                    case "White Rook":
                        str2 += " " + "♜"
                    case "Black Rook":
                        str2 += " " + "♖"
                    case "White Knight":
                        str2 += " " + "♞"
                    case "Black Knight":
                        str2 += " " + "♘"
                    case _:
                        raise Exception("Piece not found!")

                if ((i+1)%8 == 0):
                    print("{} - {}\n".format(j+1, str2))
                    str2 = ""

    def playMove(self):
        valid_move = False
        while not valid_move:
            moveFrom = input("Input the square to be moved: ")
            moveTo = input("Input where it should be moved to: ")
            moveFrom = self.moveToMatrix(moveFrom)
            moveTo = self.moveToMatrix(moveTo)
            if (self.verifyMove(moveFrom, moveTo)):
                valid_move = True
                self.rodada += 1
            if (valid_move == False):
                print("Invalid play! Please try again.")
        self.board[moveTo[1]][moveTo[0]] = self.board[moveFrom[1]][moveFrom[0]]
        self.board[moveFrom[1]][moveFrom[0]] = Piece("Empty", "Space")

    def moveToMatrix(self, move):
        match move[0]:
            case "A":
                return [0, int(move[1])-1]
            case "B":
                return [1, int(move[1])-1]
            case "C":
                return [2, int(move[1])-1]
            case "D":
                return [3, int(move[1])-1]
            case "E":
                return [4, int(move[1])-1]
            case "F":
                return [5, int(move[1])-1]
            case "G":
                return [6, int(move[1])-1]
            case "H":
                return [7, int(move[1])-1]
            case _:
                raise Exception("Error in play.")
    
    def __str__(self):  # To-do: Add game status
        return "Chess game"


class Piece:
    def __init__(self, color, specie):
        self.color = color
        self.specie = specie

    def verifyMove(self):
        pass
    
    def pop(self):
        self.color = "Empty"
        self.specie = "Space"
    
    def transform(self, color, specie):
        self.color = color
        self.specie = specie
    
    def __str__(self):
        return self.color + " " + self.specie


if __name__ == "__main__":
    chess = ChessGame()