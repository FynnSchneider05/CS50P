from prettytable import PrettyTable
import pyfiglet
from colorama import Fore, Back
import sys
import pickle
import re
import os
from custom_errors import MovementFailedError


#import all pieces
from pieces import Piece
from pawn import Pawn






#initiate Pieces
king_w: Piece = Piece("king",[7,5],"w")
king_b: Piece = Piece("king",[0,5],"b")

queen_w: Piece = Piece("queen",[7,4],"w")
queen_b: Piece = Piece("queen",[0,4],"b")

rook1_w: Piece = Piece("rook",[7,1],"w")
rook2_w: Piece = Piece("rook",[7,8],"w")

rook1_b: Piece = Piece("rook",[0,8],"b" )
rook2_b: Piece = Piece("rook",[0,1],"b")

bishop1_w: Piece = Piece("bishop",[7,3],"w")
bishop2_w: Piece = Piece("bishop",[7,6],"w")

bishop1_b: Piece = Piece("bishop",[0,3],"b")
bishop2_b: Piece = Piece("bishop",[0,6],"b")

knight1_w: Piece = Piece("knight",[7,2],"w")
knight2_w: Piece = Piece("knight",[7,7],"w")

knight1_b: Piece = Piece("knight",[0,2],"b")
knight2_b: Piece = Piece("knight",[0,7],"b")

pawn1_w: Pawn = Pawn([6,1], "w")
pawn2_w: Pawn = Pawn([6,2], "w")
pawn3_w: Pawn = Pawn([6,3], "w")
pawn4_w: Pawn = Pawn([6,4], "w")
pawn5_w: Pawn = Pawn([6,5], "w")
pawn6_w: Pawn = Pawn([6,6], "w")
pawn7_w: Pawn = Pawn([6,7], "w")
pawn8_w: Pawn = Pawn([6,8], "w")

pawn1_b: Pawn = Pawn([1,1], "b")
pawn2_b: Pawn = Pawn([1,2], "b")
pawn3_b: Pawn = Pawn([1,3], "b")
pawn4_b: Pawn = Pawn([1,4], "b")
pawn5_b: Pawn = Pawn([1,5], "b")
pawn6_b: Pawn = Pawn([1,6], "b")
pawn7_b: Pawn = Pawn([1,7], "b")
pawn8_b: Pawn = Pawn([1,8], "b")




#saves the current position
current_position =[
            ["8",rook1_b,knight1_b,bishop1_b,queen_b,king_b,bishop2_b,knight2_b,rook2_b],
            ["7",pawn1_b, pawn2_b, pawn3_b, pawn4_b, pawn5_b, pawn6_b, pawn7_b, pawn8_b],
            ["6","",      "",        "",       "",     "",    "",        "",         ""],
            ["5","",      "",        "",       "",     "",    "",        "",         ""],
            ["4","",      "",        "",       "",     "",    "",        "",         ""],
            ["3","",      "",        "",       "",     "",    "",        "",         ""],
            ["2",pawn1_w, pawn2_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w, pawn8_w],
            ["1",rook1_w,knight1_w,bishop1_w,queen_w,king_w,bishop2_w,knight2_w,rook2_w],
            ]


#dict to convert the user input to the correct indices for current_position
field_convertion_dict = {
    "a": 1, "b": 2, "c": 3, "d":4, "e":5, "f":6, "g":7, "h":8,
    "1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0,
                         }


#tracks whitch color is to move
color_to_move = "w"

#tracks a possible errormessage to print it after reprinting the board
error_message = ""


#main function to
def main():

    #prints start menu
    print_start_menu()

    #starts the game cycle of promting the user, validating the move and printing the new board or errors
    while True:
        make_a_move()


#lets the player Make a move
def make_a_move():
    global current_position
    global color_to_move
    global error_message

    while True:
        #reprints the board, because the position has changed and prints info/error massages
        print_board()

        #promts the user to select a start field
        start = input("Move from: ").strip().lower()

        #checks for special commands (leave or save)
        if start == "e":
            sys.exit()
        if start == "s":
            save_game()

        #Promts the user for a end field
        end = input("Move to: ").strip().lower()

        if not re.match(r"^[a-z][1-8]$" ,start) or not re.match(r"^[a-z][1-8]$", end):
            error_message = "Invalid Input please try again"
            continue

        #converts the input (a1, b4 ...) to the correct list index (a1 = 8,1; b1 = 8,2; d5 = 4,4)
        try:
            start_parts = [_ for _ in start]
            start= [field_convertion_dict[start_parts[1]], field_convertion_dict[start_parts[0]]]
            end_parts = [_ for _ in end]
            end = [field_convertion_dict[end_parts[1]], field_convertion_dict[end_parts[0]]]

        #catches all formating erros
        except Exception:
            continue


        #takes the pieces which are currently located at the selected fields if there is one
        selected_piece_start = current_position[start[0]][start[1]]
        selected_piece_end = current_position[end[0]][end[1]]


        #checks if there is a piece on the start field
        if selected_piece_start == "":
            error_message = "No piece selected"
            continue

        #checks if the selected piece has the right color to move in this move
        if selected_piece_start.color != color_to_move:
            error_message = "The other color has to move"
            continue

        #checks if you want to move to a field where one of your own pieces is
        if selected_piece_end != "" and selected_piece_start.color == selected_piece_end.color:
            error_message = "you can't take your own pieces"
            continue


        #executes special function for pawn movement if piece_type is pawn
        if selected_piece_start.piece_type == "pawn":
            #returns Error message if movement fails and returns "" if pawn can be moved
            message = selected_piece_start.try_to_move_pawn(start, end, selected_piece_end, current_position)
            if message == "":
                #checks if pawn can promote and returs promoted piece. If not returns the original pawn
                selected_piece_start = selected_piece_start.check_for_promotion()
                #break while loop if pawn can be moved
                break
            else:
                error_message = message
                continue


        #everything from here only if piece_type is not pawn

        #tries to move the selected pieces to the selected end field
        try:
            selected_piece_start.move_to(end)
        except MovementFailedError:
            error_message = "Your selected piece can't move to this position"
            continue

        #checks if there are any pieces in the way from start to end
        try:
            for field in selected_piece_start.crossed_fields_from_last_move:
                if current_position[field[0]][field[1]] != "":
                    error_message = "There are pieces in your way, you can't move to this position"
                    raise MovementFailedError
        except MovementFailedError:
            #resets the pieces position to the start field if it can't move to the end field
            selected_piece_start.position = start
            continue

        #breaks while loop if piece can be moved
        break

    #updates the current_position board with the new positions
    commit_the_move(start, selected_piece_start)



# saves the Game as pickle file
def save_game():
    while True:
        #promts the user for a file name to save the game to
        file_name = input("Please enter a File name to save your game (.pickle): ")
        #vaildates the files format
        if not re.match(r"^.+\.pickle$", file_name):
            print(f"{Fore.RED}Ups, something went wrong, make sure you enter a correct file type{Fore.WHITE}")
            continue

        #checks if file name already exists
        saved_files = os.listdir("saved_games")
        if file_name in saved_files:
            print(f"{Fore.RED}!!! A file named {file_name} already exists, if you continue the old file will be deleted!{Fore.WHITE}")
            #asks the user if he wants to replace the old file with the new one if the file already exists
            answer = input("Type 'y' to continue? ")
            if answer != "y":
                continue
            else:
                break
        else:
            break

    #creates dictionary with current_position and color_to_move
    data = {"current_position": current_position, "color_to_move": color_to_move}
    #saves the data as pickle file
    with open(f"saved_games/{file_name}", 'wb') as file:
        pickle.dump(data, file)

    #prints that the file was saved and exits the programm
    print(f"{Fore.GREEN}Game Saved in {file_name}")
    print(f"{Fore.GREEN}! Dont Forgett the name of your File{Fore.WHITE}")
    sys.exit()


#loads an old game
def load_game(position, c_to_move):
    global current_position
    global color_to_move
    #sets current_position and color_to_move to the saved value
    current_position = position
    color_to_move = c_to_move
    #continues the game from the saved point
    main()


#updates current position after moving pieces
def commit_the_move(start, selected_piece_start):
    global error_message
    global current_position
    global color_to_move
    #places a "" on the old position of the moved piec
    current_position[start[0]][start[1]] = ""
    #places selected_pice on the selected_position
    current_position[selected_piece_start.position[0]][selected_piece_start.position[1]] = selected_piece_start
    #sets the other color to color_to_move
    if color_to_move == "w":
        color_to_move = "b"
    else:
        color_to_move = "w"

    #there is no error massage when we can sucessfully move a piece so error_message gets set to ""
    error_message = ""










#prints the current_position to the console
def print_board():

    #clears the terminal
    print(chr(27) + "[2J")

    #prints the boad
    #creates a table with PrettyTable
    table = PrettyTable()
    #sets the header
    table.field_names = ["/","a","b","c","d","e","f","g","h"]
    #adds all roaws from current_position
    for row in current_position:
        table.add_row(row, divider=True)

    #prints the table (board)
    print(table)

    #prints Info/Error
    print(f"{Fore.BLUE}Press 'e' to exit or  's' to save{Fore.WHITE}")
    print(f"{Fore.RED}{error_message}{Fore.WHITE}")

    if color_to_move == "w":
        print("White to move\n")
    else:
        print("Black to move\n")


#prints start menu
def print_start_menu():
    #clears the terminal
    print(chr(27) + "[2J")
    #shows title
    print(f"{Fore.GREEN}{pyfiglet.figlet_format('Terminal Chess', font='5lineoblique')}{Fore.WHITE}\n\n")
    #waits for the user to start the game
    input("Press Enter to start the Game \n\n")



if __name__ == "__main__":
    main()
