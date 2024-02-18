from pytest import MonkeyPatch
import pytest
import game
import project
from prettytable import PrettyTable
from colorama import Fore
from pieces import Piece
from pawn import Pawn


#import custom Error
from custom_errors import MovementFailedError


#!!!!!!!!!!!
#run tests with an empty 'saved_games' Folder
#!!!!!!!!!!!

#tests to load a game when there are no saved games
def test_show_saved_games(capsys):
    with pytest.raises(OSError):
        assert project.show_saved_games()

    stdout, stderr = capsys.readouterr()

    last_output = stdout.split("\n")[-3]

    assert last_output == "Sorry, there are currently no games saved"


def test_main(capsys):
    with pytest.raises(OSError):
        assert project.main()
    stdout, stderr = capsys.readouterr()

    last_output = stdout.split("\n")[-1]

    assert last_output ==  "action: "

#tests to start a new game ant to save it (a new file names 'test_file.pickle' should show up in saved_games)
def test_start_and_save_game(monkeypatch):

    inputs = iter(["p"," ", "e2","e4", "e7", "e5","b1","c3","s","test_file.pickle"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(SystemExit):
        assert project.main()


#tests if the saved games are shown in the selection meunu to load a game
def test_load_game_show_saved_games(capsys):
    with pytest.raises(OSError):
        assert project.load_game()

    stdout, stderr = capsys.readouterr()

    last_output = stdout.split("\n")[-2]

    assert last_output == f"{Fore.BLUE}1, test_file.pickle{Fore.WHITE}"


#tests to load the earlier saved game
def test_load_game(monkeypatch, capsys):
    inputs = iter(["test_file.pickle"," "])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(StopIteration):
        assert project.load_game()

    stdout, stderr = capsys.readouterr()

    last_output = stdout.split("\n")[-3]

    assert last_output == f"Black to move"


def test_delete_game(monkeypatch, capsys):
    inputs = iter(["test_file.pickle","y"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(StopIteration):
        assert project.delete_game()

    stdout, stderr = capsys.readouterr()

    last_output = stdout.split("\n")[-2]

    assert last_output == f"{Fore.GREEN}test_file.pickle was deleted!{Fore.WHITE}"




#tests if the program exits from the menu
def test_exit_from_menu(monkeypatch):
    inputs = iter(["e"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    with pytest.raises(SystemExit):
        assert project.main()

#tests if the programm exits from the game
def test_exit_from_game(monkeypatch):
    inputs = iter([" ","e"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    with pytest.raises(SystemExit):
        assert game.main()


def test_king_movement_invalid():
    king = Piece("king",[0,1], "w")
    with pytest.raises(MovementFailedError):
        assert king.move_to([-1,1])
        assert king.move_to([0,-1])
        assert king.move_to([-1,-1])
        assert king.move_to([2,1])
        assert king.move_to([0,3])
        assert king.move_to([2,3])

def test_king_movement_valid():
    king = Piece("king",[0,1], "w")
    king.move_to([1,1])
    assert king.position ==[1,1]
    king.move_to([2,2])
    assert king.position == [2,2]
    king.move_to([3,2])
    assert king.position == [3,2]

def test_queen_movement_invalid():
    queen = Piece("queen",[0,1], "w")
    with pytest.raises(MovementFailedError):
        assert queen.move_to([-1,1])
        assert queen.move_to([0,-1])
        assert queen.move_to([-1,-1])
        assert queen.move_to([2,2])
        assert queen.move_to([1,3])
        assert queen.move_to([1,6])
        assert queen.move_to([2,7])
        assert queen.move_to([4,2])
        assert queen.move_to([6,3])

def test_queen_movement_valid():
    queen = Piece("queen",[0,1], "w")
    queen.move_to([0,6])
    assert queen.position ==[0,6]
    queen.move_to([4,6])
    assert queen.position == [4,6]
    queen.move_to([4,2])
    assert queen.position == [4,2]
    queen.move_to([6,4])
    assert queen.position ==[6,4]
    queen.move_to([4,6])
    assert queen.position == [4,6]
    queen.move_to([4,2])
    assert queen.position == [4,2]
    queen.move_to([0,6])
    assert queen.position ==[0,6]


def test_rook_movement_invalid():
    rook = Piece("rook",[0,1], "w")
    with pytest.raises(MovementFailedError):
        assert rook.move_to([-1,1])
        assert rook.move_to([0,-1])
        assert rook.move_to([-1,-1])
        assert rook.move_to([2,2])
        assert rook.move_to([1,2])
        assert rook.move_to([2,6])
        assert rook.move_to([3,2])
        assert rook.move_to([4,2])
        assert rook.move_to([6,3])

def test_rook_movement_valid():
    rook = Piece("rook",[0,1], "w")
    rook.move_to([0,6])
    assert rook.position ==[0,6]
    rook.move_to([4,6])
    assert rook.position == [4,6]
    rook.move_to([4,2])
    assert rook.position == [4,2]
    rook.move_to([6,2])
    assert rook.position ==[6,2]
    rook.move_to([0,2])
    assert rook.position == [0,2]
    rook.move_to([0,7])
    assert rook.position == [0,7]
    rook.move_to([3,7])
    assert rook.position ==[3,7]



def test_bishop_movement_invalid():
    bishop = Piece("bishop",[0,1], "w")
    with pytest.raises(MovementFailedError):
        assert bishop.move_to([-1,2])
        assert bishop.move_to([1,-2])
        assert bishop.move_to([-1,-2])
        assert bishop.move_to([1,0])
        assert bishop.move_to([1,1])
        assert bishop.move_to([2,1])
        assert bishop.move_to([2,2])
        assert bishop.move_to([1,4])
        assert bishop.move_to([0,5])

def test_bishop_movement_valid():
    bishop = Piece("bishop",[0,1], "w")
    bishop.move_to([6,7])
    assert bishop.position ==[6,7]
    bishop.move_to([3,4])
    assert bishop.position == [3,4]
    bishop.move_to([2,5])
    assert bishop.position == [2,5]
    bishop.move_to([1,6])
    assert bishop.position ==[1,6]
    bishop.move_to([5,2])
    assert bishop.position == [5,2]
    bishop.move_to([6,3])
    assert bishop.position == [6,3]
    bishop.move_to([4,1])
    assert bishop.position ==[4,1]



def test_knight_movement_invalid():
    knight = Piece("knight",[0,1], "w")
    with pytest.raises(MovementFailedError):
        assert knight.move_to([-2,0])
        assert knight.move_to([-2,2])
        assert knight.move_to([1,-3])
        assert knight.move_to([-1,3])
        assert knight.move_to([1,2])
        assert knight.move_to([0,2])
        assert knight.move_to([2,1])
        assert knight.move_to([1,4])
        assert knight.move_to([3,2])

def test_knight_movement_valid():
    knight = Piece("knight",[0,1], "w")
    knight.move_to([1,3])
    assert knight.position == [1,3]
    knight.move_to([3,2])
    assert knight.position == [3,2]
    knight.move_to([1,1])
    assert knight.position == [1,1]
    knight.move_to([3,2])
    assert knight.position ==[3,2]
    knight.move_to([4,4])
    assert knight.position == [4,4]
    knight.move_to([2,3])
    assert knight.position == [2,3]
    knight.move_to([1,5])
    assert knight.position ==[1,5]




def test_pawn_movement_two_fields():
    pawn = Pawn([6,1], "w")

    current_position =[
            ["8","",      "",        "",       "",     "",    "",        "",         ""],
            ["7","",      "",        "",       "",     "",    "",        "",         ""],
            ["6","",      "",        "",       "",     "",    "",        "",         ""],
            ["5","",      "",        "",       "",     "",    "",        "",         ""],
            ["4","",      "",        "",       "",     "",    "",        "",         ""],
            ["3","",      "",        "",       "",     "",    "",        "",         ""],
            ["2",pawn,      "",        "",       "",     "",    "",        "",        ""],
            ["1","",      "",        "",       "",     "",    "",        "",         ""],
            ]

    #test moving forward
    assert pawn.try_to_move_pawn([6,1], [4,1], "", current_position) == ""
    assert pawn.position == [4,1]


    current_position =[
            ["8","",      "",        "",       "",     "",    "",        "",         ""],
            ["7","",      "",        "",       "",     "",    "",        "",         ""],
            ["6","",      "",        "",       "",     "",    "",        "",         ""],
            ["5","",      "",        "",       "",     "",    "",        "",         ""],
            ["4",pawn,      "",        "",       "",     "",    "",        "",         ""],
            ["3","",      "",        "",       "",     "",    "",        "",         ""],
            ["2","",      "",        "",       "",     "",    "",        "",        ""],
            ["1","",      "",        "",       "",     "",    "",        "",         ""],
            ]

    assert pawn.try_to_move_pawn([4,1],[2,1], "", current_position) == "Your selected piece can't move to this position"

def test_pawn_movement_invalid():
    pawn = Pawn([6,1], "w")

    current_position =[
            ["8","",      "",        "",       "",     "",    "",        "",         ""],
            ["7","",      "",        "",       "",     "",    "",        "",         ""],
            ["6","",      "",        "",       "",     "",    "",        "",         ""],
            ["5","",      "",        "",       "",     "",    "",        "",         ""],
            ["4","",      "",        "",       "",     "",    "",        "",         ""],
            ["3","",      "",        "",       "",     "",    "",        "",         ""],
            ["2",pawn,      "",        "",       "",     "",    "",        "",        ""],
            ["1","",      "",        "",       "",     "",    "",        "",         ""],
            ]

    assert pawn.try_to_move_pawn([6,1], [6,0], "", current_position) == "Your selected piece can't move to this position"
    assert pawn.try_to_move_pawn([6,1], [6,2], "", current_position) == "Your selected piece can't move to this position"
    assert pawn.try_to_move_pawn([6,1], [3,1], "", current_position) == "Your selected piece can't move to this position"
    assert pawn.try_to_move_pawn([6,1], [7,1], "", current_position) == "Your selected piece can't move to this position"
    assert pawn.try_to_move_pawn([6,1], [5,2], "", current_position) == "Pawn can only move diagonal if he takes a piece"
    assert pawn.try_to_move_pawn([6,1], [5,2], "", current_position) == "Pawn can only move diagonal if he takes a piece"

    current_position =[
            ["8","",      "",        "",       "",     "",    "",        "",         ""],
            ["7","",      "",        "",       "",     "",    "",        "",         ""],
            ["6","",      "",        "",     pawn,     "",    "",        "",         ""],
            ["5","",      "",        "",       "",     "",    "",        "",         ""],
            ["4","",      "",        "",       "",     "",    "",        "",         ""],
            ["3","",      "",        "",       "",     "",    "",        "",         ""],
            ["2","",      "",        "",       "",     "",    "",        "",        ""],
            ["1","",      "",        "",       "",     "",    "",        "",         ""],
            ]

    pawn = Pawn([2,4], "b")
    assert pawn.try_to_move_pawn([2,4], [1,4], "", current_position) == "Your selected piece can't move to this position"
    assert pawn.try_to_move_pawn([2,4], [5,4], "", current_position) == "Your selected piece can't move to this position"
    assert pawn.try_to_move_pawn([2,4], [2,3], "", current_position) == "Your selected piece can't move to this position"
    assert pawn.try_to_move_pawn([2,4], [3,3], "", current_position) == "Pawn can only move diagonal if he takes a piece"
    assert pawn.try_to_move_pawn([2,4], [3,5], "", current_position) == "Pawn can only move diagonal if he takes a piece"



def test_pawn_movement_one_field():
    pawn = Pawn([2,4], "b")

    current_position =[
            ["8","",      "",        "",       "",     "",    "",        "",         ""],
            ["7","",      "",        "",       "",     "",    "",        "",         ""],
            ["6","",      "",        "",       pawn,     "",    "",        "",         ""],
            ["5","",      "",        "",       "",     "",    "",        "",         ""],
            ["4","",      "",        "",       "",     "",    "",        "",         ""],
            ["3","",      "",        "",       "",     "",    "",        "",         ""],
            ["2","",      "",        "",       "",     "",    "",        "",        ""],
            ["1","",      "",        "",       "",     "",    "",        "",         ""],
            ]

    #test moving forward
    assert pawn.try_to_move_pawn([2,4], [3,4], "", current_position) == ""
    assert pawn.position == [3,4]


def test_pawn_movement_colliding():
    pawn1 = Pawn([6,1], "w")
    pawn2 = Pawn([3,1], "b")
    pawn3 = Pawn([3,2], "b")

    current_position =[
            ["8","",      "",        "",       "",     "",    "",        "",         ""],
            ["7","",      "",        "",       "",     "",    "",        "",         ""],
            ["6","",      "",        "",       "",     "",    "",        "",         ""],
            ["5", pawn2,  pawn3,       "",       "",     "",    "",        "",        ""],
            ["4", pawn1,    "",        "",       "",     "",    "",        "",         ""],
            ["3","",      ""         "",       "",     "",    "",        "",         ""],
            ["2","",      "",        "",       "",     "",    "",        "",         ""],
            ["1","",      "",        "",       "",     "",    "",        "",         ""],
            ]

    assert pawn1.try_to_move_pawn([4,1],[3,1],pawn2, current_position) == "Pawn can't take a pice while moving straight forward"
    assert pawn2.try_to_move_pawn([3,1],[4,1],pawn1, current_position) == "Pawn can't take a pice while moving straight forward"
    assert pawn3.try_to_move_pawn([3,2], [4,1], pawn1, current_position) == ""
    assert pawn3.position == [4,1]



def test_pawn_promotion(monkeypatch):
    pawn = Pawn([0,1], "w")

    inputs = iter(["Q"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    piece = pawn.check_for_promotion()
    assert piece.piece_type == "queen"

    inputs = iter(["r"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    piece = pawn.check_for_promotion()
    assert piece.piece_type == "rook"

    inputs = iter(["B"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    piece = pawn.check_for_promotion()
    assert piece.piece_type == "bishop"


    inputs = iter(["k"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    piece = pawn.check_for_promotion()
    assert piece.piece_type == "knight"



    pawn = Pawn([7,1], "b")

    inputs = iter(["Q"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    piece = pawn.check_for_promotion()
    assert piece.piece_type == "queen"

    inputs = iter(["R"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    piece = pawn.check_for_promotion()
    assert piece.piece_type == "rook"

    inputs = iter(["B"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    piece = pawn.check_for_promotion()
    assert piece.piece_type == "bishop"


    inputs = iter(["K"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    piece = pawn.check_for_promotion()
    assert piece.piece_type == "knight"


#def get_crossed_fields_from_last_move(self, new_position, move, direction):
def test_crossed_fields_from_last_move():
    knight = Piece("knight",[4,4], "w")
    knight.get_crossed_fields_from_last_move([6,5],[2,1], 1)
    assert knight.crossed_fields_from_last_move == []
    rook = Piece("rook",[1,1], "w")
    rook.get_crossed_fields_from_last_move([1,6],[0,5], 1)
    assert rook.crossed_fields_from_last_move == [[1,2],[1,3],[1,4],[1,5]]
    bishop = Piece("bishop",[4,4], "w")
    bishop.get_crossed_fields_from_last_move([2,2],[2,2], -1)
    assert bishop.crossed_fields_from_last_move == [[3,3]]

    queen = Piece("queen",[4,4], "w")
    queen.get_crossed_fields_from_last_move([4,8],[0,4], 1)
    assert queen.crossed_fields_from_last_move == [[4,5], [4,6], [4,7]]
    queen.get_crossed_fields_from_last_move([1,1],[3,3], -1)
    assert queen.crossed_fields_from_last_move  == [[3,3], [2,2]]
