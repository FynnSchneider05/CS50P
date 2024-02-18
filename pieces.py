from custom_errors import MovementFailedError

#Piece Class as parent for all Pieces
class Piece:

    #the possible Fields the piec can be at
    possible_fields = [
        [0, 1],[0, 2],[0, 3],[0, 4],[0, 5],[0, 6],[0, 7],[0, 8],
        [1, 1],[1, 2],[1, 3],[1, 4],[1, 5],[1, 6],[1, 7],[1, 8],
        [2, 1],[2, 2],[2, 3],[2, 4],[2, 5],[2, 6],[2, 7],[2, 8],
        [3, 1],[3, 2],[3, 3],[3, 4],[3, 5],[3, 6],[3, 7],[3, 8],
        [4, 1],[4, 2],[4, 3],[4, 4],[4, 5],[4, 6],[4, 7],[4, 8],
        [5, 1],[5, 2],[5, 3],[5, 4],[5, 5],[5, 6],[5, 7],[5, 8],
        [6, 1],[6, 2],[6, 3],[6, 4],[6, 5],[6, 6],[6, 7],[6, 8],
        [7, 1],[7, 2],[7, 3],[7, 4],[7, 5],[7, 6],[7, 7],[7, 8],
    ]

    #move patterns of all the pieces
    move_pattern_dict = {
    "king": [[0,1], [1,0],[1,1],[1,-1]],
    "queen": [[0, 1], [1, 0], [1, 1], [-1, 1], [0, 2], [2, 0], [2, 2], [-2, 2], [0, 3], [3, 0], [3, 3], [-3, 3], [0, 4], [4, 0], [4, 4], [-4, 4], [0, 5], [5, 0], [5, 5], [-5, 5], [0, 6], [6, 0], [6, 6], [-6, 6], [0, 7], [7, 0], [7, 7], [-7, 7], [0, 8], [8, 0], [8, 8], [-8, 8]],
    "rook":[[1, 0], [0, 1], [2, 0], [0, 2], [3, 0], [0, 3], [4, 0], [0, 4], [5, 0], [0, 5], [6, 0], [0, 6], [7, 0], [0, 7], [8, 0], [0, 8]],
    "bishop":[[1, 1], [-1, 1], [2, 2], [-2, 2], [3, 3], [-3, 3], [4, 4], [-4, 4], [5, 5], [-5, 5], [6, 6], [-6, 6], [7, 7], [-7, 7], [8, 8], [-8, 8]],
    "knight": [[2,1],[2,-1],[1,2],[1,-2]],
    "pawn":[],
    }

    #icons of all the pieces
    icon_dict = {"kingW":"♚","kingB":"♔","queenW":"♛", "queenB":"♕","rookW":"♜","rookB":"♖", "knightW":"♞","knightB":"♘","bishopW":"♝","bishopB":"♗","pawnW":"♟︎","pawnB":"♙"}


#Properties

    #the current position the a piec
    @property
    def position(self):
        return self._position

    @property
    def crossed_fields_from_last_move(self):
        return self._crossed_fields_from_last_move

    #the icon of the piece
    @property
    def icon(self):
        return self._icon

    #the color of the piece
    @property
    def color(self):
        return self._color

    #the type of the piece (rook, knight etc.)
    @property
    def piece_type(self):
        return self._piece_type

    #the unique move pattern of the piece
    @property
    def move_pattern(self):
        return self._move_pattern



#Setter functions

    #checks, that piece_type can only be set once
    @piece_type.setter
    def piece_type(self, piece_type):
        try:
            self.piece_type
        except:
            self._piece_type = piece_type


    #makes it impossible to set crossed_fields_from_last_move manually
    @crossed_fields_from_last_move.setter
    def crossed_fields_from_last_move(self, crossed_fields_from_last_move):
        return


    #checks, that icon type can only be set once
    @icon.setter
    def icon(self, icon):
        try:
            self.icon
        except:
            self._icon = icon

    #checks, taht color can only be set once
    @color.setter
    def color(self, color):
        try:
            self.color
        except:
            self._color = color

    #validates so that a move pattern can only be set once
    @move_pattern.setter
    def move_pattern(self, move_pattern):
        try:
            if self.move_pattern:
                return
        except:
            self._move_pattern = move_pattern



    #validates if reaching the new_position is possible
    @position.setter
    def position(self, new_position):

        #checks if new_position is a possible_field
        if new_position not in self.possible_fields:
            raise MovementFailedError

        #checks, if position was already set once. Is needed to avoid errors when initializeing a new piece
        try:
            self.position

        #If position was not already set once, It means, that the piece gets initialized and we set the position property to new_position and return
        except:
            self._position = new_position
            return


        #If position was already set onece, it means we are currently trying to change the position
        #Checks if the specific peace can move to the new_position
        self.try_to_move_piece(new_position)




#Helper Methods for Properties

    #helper method for position.setter
    def try_to_move_piece(self, new_position):

        #checks if piece can move to the new_position from the current one with his move_pattern
        #adds for each move in move_pattern the current position and the move, to see if any valid move can reach the new_position
        #if so, the new positon gets set and we return
        for move in self.move_pattern:
            if [self.position[0] + move[0], self.position[1] + move[1]] == new_position:
                #makes a list with all the fields our piece has crossed during his move (start, end excluded)
                self.get_crossed_fields_from_last_move(new_position, move, 1)
                self._position = new_position
                self.move_count += 1
                return
            elif [self.position[0] - move[0], self.position[1] - move[1]] == new_position:
                #makes a list with all the fields our piece has crossed during his move (start, end excluded)
                self.get_crossed_fields_from_last_move(new_position, move , -1)
                self._position = new_position
                self.move_count += 1
                return
            else:
                continue

        raise MovementFailedError




    #helper method for try_to_make_move
    #sets _crossed_fields_from_last_move to a list with all fields that our piece has crossed while moving the the new position
    def get_crossed_fields_from_last_move(self, new_position, move, direction):
        start_position = self.position
        crossed_fields = []

        #sets crossed_fields_from_last_move to [] if the piece is a knight, because he jups over fields
        if self.piece_type == "knight":
            self._crossed_fields_from_last_move = crossed_fields
            return

        #looks if move_pattern is diagonal
        elif abs(move[0]) == abs(move[1]):
            #shortends the move, to only be one square at a time
            move_norm = [move[0] / abs(move[0]), move[1] / abs(move[1])]
        #looks if move_pattern is straight left or right
        elif move[0] == 0:
            #shortends the move, to only be one square at a time
            move_norm = [move[0], move[1]/move[1]]#
        #looks if move_pattern is straight up or down
        elif move[1] == 0:
            #shortends the move, to only be one square at a time
            move_norm = [move[0] / move[0], move[1]]


        #looks if we added or subtracted the move from the start position to get to the new position earlier
        #multiplies with -1 if we subtracted the move and with 1 if we added the move
        move_norm = [int(move_norm[0] * direction), int(move_norm[1] * direction)]

        #walks from the start position the the end position one field at a time and appends all the crossed fields to ohe crossed_fields list
        #sets _crossed_fields_from_last_move the list when the new position is reached before appending the last position
        while True:
            start_position = [int(start_position[0] + move_norm[0]), int(start_position[1] + move_norm[1])]

            if start_position == new_position:
                self._crossed_fields_from_last_move = crossed_fields
                return

            crossed_fields.append(start_position)







#Methods



    #init class sets piece_type, move_patter, position, icon and color
    def __init__(self,piece_type, position, color):
        self.move_count = 0
        self.piece_type = piece_type
        self.position = position
        self.color = color
        self.icon = self.icon_dict[f"{self.piece_type}{self.color.upper()}"]
        self.move_pattern = self.move_pattern_dict[self.piece_type]



    #returns piece icon if Object gets printed
    def __str__(self):
        return self.icon


    #Tries to set a new position(calls the position Setter) if piece_type is not pawn
    #Only to make it easier to cleaner to acess the position Property from another File
    def move_to(self, position):
        #Pawn movement is unique and gets handled in the Pawn class
        if self.piece_type == "pawn":
            return
        self.position = position

