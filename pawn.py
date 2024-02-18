from pieces import Piece

class Pawn(Piece):
    def __init__(self, position, color):
        super().__init__("pawn",position, color)



    #moves the pawn to a new position
    def pawn_move(self, position, pawn):
        if pawn == self:
            self._position = position
            self.move_count += 1



    def try_to_move_pawn(self, start, end, selected_piece_end, current_position):
        #if pawn color is white:
        if self.color == "w":
            #looks if end is infront of start, if yes, looks if there is a piece, if no, moves forward, if yes, returns error
            if [start[0] - 1, start[1]] == end:
                if selected_piece_end == "":
                    self.pawn_move(end, self)
                    return ""
                else:
                    error_massage = "Pawn can't take a pice while moving straight forward"
                    return error_massage

            #checks if pawn can move two fields (first move) and if so moves the pawn
            elif [start[0] - 2, start[1]] == end and self.move_count == 0 and current_position[start[0]-1][start[1]] == "":
                self.pawn_move(end, self)
                return ""

            #looks if end is diagonal from start, if yes, looks if there is a piece, if yes, takes it, if no, error
            elif [start[0] - 1, start[1] - 1] == end or [start[0] - 1, start[1] + 1] == end:
                if selected_piece_end != "":
                    self.pawn_move(end, self)
                    return ""
                else:
                    error_massage = "Pawn can only move diagonal if he takes a piece"
                    return error_massage

            error_massage = "Your selected piece can't move to this position"
            return error_massage



        #if pawn color is black:
        else:
            #looks if end is infront of start, if yes, looks if there is a piece, if no, moves forward, if yes, error
            if [start[0] + 1, start[1]] == end:
                if selected_piece_end == "":
                    self.pawn_move(end, self)
                    return ""
                else:
                    error_massage = "Pawn can't take a pice while moving straight forward"
                    return error_massage

            #checks if pawn can move two fields (first move) and if so moves the pawn
            if [start[0] + 2, start[1]] == end and self.move_count == 0 and current_position[start[0]+1][start[1]] == "":
                self.pawn_move(end, self)
                return ''

            #looks if end is diagonal from start, if yes, looks if there is a piece, if yes, takes it, if no, error
            if [start[0] + 1, start[1] + 1] == end or [start[0] + 1, start[1] - 1] == end:
                if selected_piece_end != "":
                    self.pawn_move(end, self)
                    return ""
                else:
                    error_massage = "Pawn can only move diagonal if he takes a piece"
                    return error_massage

            error_massage = "Your selected piece can't move to this position"
            return error_massage

    #checks for promotion
    def check_for_promotion(self):
        #checks if on back rank
        if self.color == "w" and not self.position[0] == 0:
            return self
        #checks if on back rank
        if self.color == "b" and not self.position[0] == 7:
            return self

        #if pawn can promote, promts the user for the piece he wants to promote to
        while True:
            print("Queen = q, Rook = r, Knigkt = k, Bishop = b")
            answer = input("Select the piec you want to promote to: ").strip().lower()
            match answer:
                case "q":
                    piece = Piece("queen",self.position, self.color)
                    break
                case "r":
                    piece = Piece("rook",self.position, self.color)
                    break
                case "k":
                    piece = Piece("knight",self.position, self.color)
                    break
                case "b":
                    piece = Piece("bishop",self.position, self.color)
                    break
                case _:
                    continue
        #returns the new piece with position and color set to the promoted pawns position and color
        return piece

