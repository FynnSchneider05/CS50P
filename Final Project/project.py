from prettytable import PrettyTable
import game as game
import pickle
import os
from colorama import Fore
import sys
import pyfiglet

def main():
    print_menu()
    action = input("action: ").lower().strip()

    if action == "p":
        game.main()

    elif action == "l":
        load_game()

    elif action == "d":
        delete_game()

    elif action == "e":
        sys.exit()

    else:
        main()

#delete saved game
def delete_game():
    show_saved_games()

    while True:
        #prompts the user for a file he wants to delete
        print(f"{Fore.BLUE}press 'e' to exit{Fore.WHITE}")
        file_name = input(f"{Fore.GREEN}Please Select a File name you want to delete: {Fore.WHITE}")
        if file_name == "e":
            main()
        #promts the user if he really wants to delete the file
        print(f"Are you sure you want to remove {file_name}?")
        answer = input("to continue enter 'y': ")
        #deletes the file if answer is y
        if answer == "y":
            os.remove(f"saved_games/{file_name}")
            print(f"{Fore.GREEN}{file_name} was deleted!{Fore.WHITE}")
            input("press enter to continue")
            continue
        else:
            main()

#load an saved game
def load_game():
    show_saved_games()

    while True:
        #prompts the user for a file he wants to load
        file_name = input(f"{Fore.GREEN}Please Select a File name you want to load: {Fore.WHITE}")
        #tries to open a loaded File and to extract the game data
        try:
            with open(f"saved_games/{file_name}", "rb") as file:
                data = pickle.load(file)
                color_to_move = data["color_to_move"]
                current_position = data["current_position"]
                break

        #catches error if fail cant be opend or read
        except:
            continue
    #loads the game if opening data was successfull
    game.load_game(current_position, color_to_move)



def show_saved_games():
    #list of all saved games
    saved_games = os.listdir("saved_games")
    #prints error if there are no saved games
    if len(saved_games) == 0:
        print("Sorry, there are currently no games saved")
        input("Press enter to continue\n")
        #shows menu again
        main()

    #lists all saved games
    for i, saved_game in enumerate(saved_games):
        print(f"{Fore.BLUE}{i + 1}, {saved_game}{Fore.WHITE}")


def print_menu():
    #clears the terminal
    print(chr(27) + "[2J")

    #prints title
    print(f"{Fore.GREEN}{pyfiglet.figlet_format('Terminal Chess', font='5lineoblique')}{Fore.WHITE}\n\n")
    #prints Menu table with all options
    table = PrettyTable()
    table.field_names = [f"{Fore.GREEN}Press", f"Action{Fore.WHITE}"]
    table.add_row([f"{Fore.GREEN}p{Fore.WHITE}", f"{Fore.GREEN}Play a new Game{Fore.WHITE}"], divider=True)
    table.add_row([f"{Fore.GREEN}l{Fore.WHITE}", f"{Fore.GREEN}Load a saved Game{Fore.WHITE}"], divider=True)
    table.add_row([f"{Fore.GREEN}d{Fore.WHITE}", f"{Fore.GREEN}Delete a saved Game{Fore.WHITE}"], divider=True)
    table.add_row([f"{Fore.GREEN}e{Fore.WHITE}", f"{Fore.GREEN}Exit{Fore.WHITE}"], divider=True)
    print(table)



if __name__ == "__main__":
    main()
