from time import *
print("Welcome to OS4")
# Python3 code to demonstrate
# attributes of now()
# importing datetime module for now()
import datetime

# using now() to get current time
current_time = datetime.datetime.now()
print("Today's date: ")
print("Year :", current_time.year)

print("Month : ", current_time.month)

print("Day : ", current_time.day)

print("Hour : ", current_time.hour)

print("Minute : ", current_time.minute)

print("Second :", current_time.second)

print("Microsecond :", current_time.microsecond)
username = input("Enter your username that you want to display in your account: ")
email = input("Enter your email: ")
password = input("Enter your password: ")
while True:
    z = ["1 for contacts", "2 for calculator", "3 for settings", "4 for app store"]
    a = input("Type 1 for contacts, 2 for calculator, 3 for settings, and 4 App Store")
    if a == "1":
        while True:
            print("Welcome to Contacts!")
            b = input("Type 1 to add contacts, type 2 to view contacts, type 3 to edit contacts, and 4 to exit contacts: ")
            if b == "1":
                c1 = input("Type your new contacts name: ")
                d1 = input("Enter your contacts phone #: ")

            if b == "2":
                if b == 1:
                    print("The name of your first contact is " + c1 + "and the phone # of your first contact is " + d1)
                    sleep(5)
            if not b == "1":
                print("Sorry there are no contacts created yet.")
            if b == "4":
                break
                sleep(4)
                continue
    if a == "2":
        # Program make a simple calculator
        while True:
            # This function adds two numbers
            def add(x, y):
                return x + y

            # This function subtracts two numbers
            def subtract(x, y):
                return x - y

            # This function multiplies two numbers
            def multiply(x, y):
                return x * y

            # This function divides two numbers
            def divide(x, y):
                return x / y


            print("Select operation.")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")

            while True:
                # take input from the user
                choice = input("Enter choice(1/2/3/4): ")

                # check if choice is one of the four options
                if choice in ('1', '2', '3', '4'):
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if choice == '1':
                        print(num1, "+", num2, "=", add(num1, num2))

                    elif choice == '2':
                        print(num1, "-", num2, "=", subtract(num1, num2))

                    elif choice == '3':
                        print(num1, "*", num2, "=", multiply(num1, num2))

                    elif choice == '4':
                        print(num1, "/", num2, "=", divide(num1, num2))

                    # check if user wants another calculation
                    # break the while loop if answer is no
                    next_calculation = input("Let's do next calculation? (yes/no): ")
                    if next_calculation == "no":
                      break
                else:
                    print("Invalid Input")
    if a == "3":
        print("Welcome to settings")
        print("Your account username is: " + username)
        print("Your account email is: " + email)
        print("We will not say your password for security reasons.")
        print("Version 0.1")
        print("© All rights reserved")
        updates = input("Check for updates? ")
        if not updates:
            continue
        if updates == "Y" or "y" or "Yes" or "yes":
            print("Searching... Please wait...")
            sleep(10)
            print("No updates avalible now.")
    if a == "4":
        print("Welcome to the App Store")
        print("We have 0 Apps avalible on the App Store.")
        app = input("Would you like a list of apps, or search for apps? ")
        if app == "Search" or "Search for apps" or "search" or "search for apps":
            search_app = input("Search for the App you would like to install: ")
        if app == "list" or "list of apps" or "List" or "List of apps":
            print("You will see a list o apps...")
            print("1 Tic Tac Toe")
            number_of_apps = input("Please type the number on the left of the app")
            if number_of_apps == "1":
                print("Installing Tic Tac Toe...")
                sleep(4)
                print("Succesfuly installed Tic Tac Toe.")
                z.append("5 for Tic-Tac Toe")
                print("Opening Tic Tac Toe...")
                sleep(2)
                # Tic-Tac-Toe Program using
                # random number in Python

                # importing all necessary libraries
                import numpy as np
                import random
                from time import sleep

                # Creates an empty board


                def create_board():
                    return(np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]]))

                # Check for empty places on board


                def possibilities(board):
                    l = []

                    for i in range(len(board)):
                        for j in range(len(board)):

                            if board[i][j] == 0:
                                l.append((i, j))
                    return(l)

                # Select a random place for the player


                def random_place(board, player):
                    selection = possibilities(board)
                    current_loc = random.choice(selection)
                    board[current_loc] = player
                    return(board)

                # Checks whether the player has three
                # of their marks in a horizontal row


                def row_win(board, player):
                    for x in range(len(board)):
                        win = True

                        for y in range(len(board)):
                            if board[x, y] != player:
                                win = False
                                continue

                        if win == True:
                            return(win)
                    return(win)

                # Checks whether the player has three
                # of their marks in a vertical row


                def col_win(board, player):
                    for x in range(len(board)):
                        win = True

                        for y in range(len(board)):
                            if board[y][x] != player:
                                win = False
                                continue

                        if win == True:
                            return(win)
                    return(win)

                # Checks whether the player has three
                # of their marks in a diagonal row


                def diag_win(board, player):
                    win = True
                    y = 0
                    for x in range(len(board)):
                        if board[x, x] != player:
                            win = False
                    if win:
                        return win
                    win = True
                    if win:
                        for x in range(len(board)):
                            y = len(board) - 1 - x
                            if board[x, y] != player:
                                win = False
                    return win

                # Evaluates whether there is
                # a winner or a tie


                def evaluate(board):
                    winner = 0

                    for player in [1, 2]:
                        if (row_win(board, player) or
                                col_win(board, player) or
                                diag_win(board, player)):

                            winner = player

                    if np.all(board != 0) and winner == 0:
                        winner = -1
                    return winner

                # Main function to start the game


                def play_game():
                    board, winner, counter = create_board(), 0, 1
                    print(board)
                    sleep(2)

                    while winner == 0:
                        for player in [1, 2]:
                            board = random_place(board, player)
                            print("Board after " + str(counter) + " move")
                            print(board)
                            sleep(2)
                            counter += 1
                            winner = evaluate(board)
                            if winner != 0:
                                break
                    return(winner)


                # Driver Code
                print("Winner is: " + str(play_game()))
