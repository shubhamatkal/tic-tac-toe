from art import welcome_art
import time


horizontal_line = "-----------"


def greet_users():
    print("Please wait...")
    time.sleep(2)
    print(welcome_art)
    time.sleep(1)
    print("Welcome to tic-tac-toe game , pls note that there must be two players")
greet_users()
USER_X_NAME = str(input("What is the name of user X ? ")).title()
USER_O_NAME = str(input("What is the name of user O ?")).title()
print("processing, pls wait ")
time.sleep(1)
print(f"USER X : {USER_X_NAME}")
print(f"USER O : {USER_O_NAME}")
is_x_ready = str(input(f"Is {USER_X_NAME} ready to start the game ? Type X , if not ready type EXIT").title())
if is_x_ready == "X":
    global is_o_ready
    is_o_ready = str(input(f"Is {USER_X_NAME} ready to start the game ? Type O , if not ready type EXIT").title())
    if is_o_ready == "O":
        print("Ok so both of you are ready to play the game lets start")
    else:
        print(
            f"user {USER_O_NAME} is not ready to play the game is aborted, {USER_X_NAME} pls tell your friend to be ready if you want to play the game , or find any other friend ;)")
else:
    print(f"user {USER_X_NAME} is not ready to play the game is aborted, {USER_O_NAME} pls tell your friend to be ready if you want to play the game , or find any other friend ;)")


if is_o_ready == "O" and is_x_ready == "X":
    game_is_on = True

if game_is_on:
    print("playground")
    print(horizontal_line)
    print("playground")
    print(horizontal_line)
    print("playground")
