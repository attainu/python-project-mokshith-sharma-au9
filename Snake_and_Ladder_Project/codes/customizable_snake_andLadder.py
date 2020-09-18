import time
import random
import sys
import ast 

msg = """
        Welcome to Snake and Ladder Terminal Game.
        Features Added:
        1. Increase the Board Size
        2. Adjust the Number of players that can play
        3. Update the snake and Ladder position according to your choice

        Rules:
        1. Initally all the players are at starting position 0. 
            Take turns according to the order to roll the dice. 
            Move forward the number of spaces shown on the dice.
        2. If you reach the bottom of a ladder at a position, move up to the head of the ladder and continue
        3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
        4. The first player to get to reach 100 Wins
        5. Hit enter to roll the dice.

        Avoid:
        1. Press enter and wait for minimum of 0.5 milli sec for the game to exceute
        2. Avoid entering number as player names
        3. Make sure to enter input when starting a game

        """
print(msg)

a="This is a Customizable Game"
SLEEP_BETWEEN_ACTIONS = 0.1
MAX_VAL = int(input("Enter the board value:"))
DICE_FACE = int(input("Enter the dice value if 1 dice then 6 and if 2 dice then 12"))


# snake takes you down from 'key' to 'value'
# snakes = {18: 1,26: 10,39: 5,51: 6,54: 36,56: 1,60: 23,75: 28,83: 45,85: 59,90: 48,92: 25}

input_dict_snakes = input("Enter the snake_position") 
snakes = ast.literal_eval(input_dict_snakes) 

# ladder takes you up from 'key' to 'value'
# ladders = {3: 20,6: 14,11: 28,15: 34,17: 74,22: 37,38: 59,49: 67,57: 76,61: 78,73: 86,81: 98,88: 91}

input_dict_ladders = input("Enter the ladders_position") 
ladders = ast.literal_eval(input_dict_ladders)

n=int(input("Enter number of players playing the game:"))

if n==2:
    def get_player_names():
        player1_name = None
        while not player1_name:
            player1_name = input("Please enter a valid name for first player: ").strip()

        player2_name = None
        while not player2_name:
            player2_name = input("Please enter a valid name for second player: ").strip()

    


        print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
        return player1_name, player2_name


    def get_dice_value():
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        dice_value = random.randint(1, DICE_FACE)
        print("Its a " + str(dice_value))
        return dice_value


    def snake_bite(old_value, current_value, player_name):
        print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))


    def ladder_climb(old_value, current_value, player_name):
        print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


    def snake_ladder(player_name, current_value, dice_value):
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        old_value = current_value
        current_value = current_value + dice_value

        if current_value > MAX_VAL:
            print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
            return old_value

        print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
        if current_value in snakes:
            final_value = snakes.get(current_value)
            snake_bite(current_value, final_value, player_name)

        elif current_value in ladders:
            final_value = ladders.get(current_value)
            ladder_climb(current_value, final_value, player_name)

        else:
            final_value = current_value

        return final_value


    def check_win(player_name, position):
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        if MAX_VAL == position:
            print("\n\n\nThats it.\n\n" + player_name + " won the game.")
            print("Congratulations " + player_name)
            sys.exit(1)
            

    def start():
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        player1_name, player2_name = get_player_names()
        time.sleep(SLEEP_BETWEEN_ACTIONS)

        player1_current_position = 0
        player2_current_position = 0

        while True:
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            input_1 = input("\n" + player1_name + ": " + " Hit the enter to roll dice: ")
            print("\nRolling dice...")
            dice_value = get_dice_value()
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(player1_name + " moving....")
            player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)

            check_win(player1_name, player1_current_position)

            input_2 = input("\n" + player2_name + ": " + " Hit the enter to roll dice: ")
            print("\nRolling dice...")
            dice_value = get_dice_value()
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(player2_name + " moving....")
            player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)

            check_win(player2_name, player2_current_position)



elif n==3:
    def get_player_names():
        player1_name = None
        while not player1_name:
            player1_name = input("Please enter a valid name for first player: ").strip()

        player2_name = None
        while not player2_name:
            player2_name = input("Please enter a valid name for second player: ").strip()
        
        player3_name = None
        while not player3_name:
            player3_name = input("Please enter a valid name for third player: ").strip()
        


        print("\nMatch will be played between '" + player1_name + "' and '" + player2_name +"' and '"+ player3_name + "'\n")
        return player1_name, player2_name,player3_name


    def get_dice_value():
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        dice_value = random.randint(1, DICE_FACE)
        print("Its a " + str(dice_value))
        return dice_value


    def snake_bite(old_value, current_value, player_name):
        print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))


    def ladder_climb(old_value, current_value, player_name):
        print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


    def snake_ladder(player_name, current_value, dice_value):
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        old_value = current_value
        current_value = current_value + dice_value

        if current_value > MAX_VAL:
            print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
            return old_value

        print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
        if current_value in snakes:
            final_value = snakes.get(current_value)
            snake_bite(current_value, final_value, player_name)

        elif current_value in ladders:
            final_value = ladders.get(current_value)
            ladder_climb(current_value, final_value, player_name)

        else:
            final_value = current_value

        return final_value


    def check_win(player_name, position):
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        if MAX_VAL == position:
            print("\n\n\nThats it.\n\n" + player_name + " won the game.")
            print("Congratulations " + player_name)
            sys.exit(1)
            

    def start():
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        player1_name, player2_name,player3_name = get_player_names()
        time.sleep(SLEEP_BETWEEN_ACTIONS)

        player1_current_position = 0
        player2_current_position = 0
        player3_current_position = 0

        while True:
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            input_1 = input("\n" + player1_name + ": " + " Hit the enter to roll dice: ")
            print("\nRolling dice...")
            dice_value = get_dice_value()
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(player1_name + " moving....")
            player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)

            check_win(player1_name, player1_current_position)

            input_2 = input("\n" + player2_name + ": " + " Hit the enter to roll dice: ")
            print("\nRolling dice...")
            dice_value = get_dice_value()
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(player2_name + " moving....")
            player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)

            check_win(player2_name, player2_current_position)

            input_3 = input("\n" + player3_name + ": " + " Hit the enter to roll dice: ")
            print("\nRolling dice...")
            dice_value = get_dice_value()
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(player3_name + " moving....")
            player3_current_position = snake_ladder(player3_name, player3_current_position, dice_value)

            check_win(player3_name, player3_current_position)
elif n==4:
    def get_player_names():
        player1_name = None
        while not player1_name:
            player1_name = input("Please enter a valid name for first player: ").strip()

        player2_name = None
        while not player2_name:
            player2_name = input("Please enter a valid name for second player: ").strip()
        
        player3_name = None
        while not player3_name:
            player3_name = input("Please enter a valid name for third player: ").strip()
        
        player4_name = None
        while not player4_name:
            player4_name = input("Please enter a valid name for fourth player: ").strip()
        


        print("\nMatch will be played between '" + player1_name + "' and '" + player2_name +"' and '"+ player3_name + "' and '" + player4_name + "'\n")
        return player1_name, player2_name,player3_name,player4_name


    def get_dice_value():
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        dice_value = random.randint(1, DICE_FACE)
        print("Its a " + str(dice_value))
        return dice_value


    def snake_bite(old_value, current_value, player_name):
        print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))


    def ladder_climb(old_value, current_value, player_name):
        print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


    def snake_ladder(player_name, current_value, dice_value):
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        old_value = current_value
        current_value = current_value + dice_value

        if current_value > MAX_VAL:
            print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
            return old_value

        print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
        if current_value in snakes:
            final_value = snakes.get(current_value)
            snake_bite(current_value, final_value, player_name)

        elif current_value in ladders:
            final_value = ladders.get(current_value)
            ladder_climb(current_value, final_value, player_name)

        else:
            final_value = current_value

        return final_value


    def check_win(player_name, position):
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        if MAX_VAL == position:
            print("\n\n\nThats it.\n\n" + player_name + " won the game.")
            print("Congratulations " + player_name)
            sys.exit(1)
            

    def start():
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        player1_name, player2_name,player3_name,player4_name = get_player_names()
        time.sleep(SLEEP_BETWEEN_ACTIONS)

        player1_current_position = 0
        player2_current_position = 0
        player3_current_position = 0
        player4_current_position = 0

        while True:
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            input_1 = input("\n" + player1_name + ": " + " Hit the enter to roll dice: ")
            print("\nRolling dice...")
            dice_value = get_dice_value()
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(player1_name + " moving....")
            player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)

            check_win(player1_name, player1_current_position)

            input_2 = input("\n" + player2_name + ": " + " Hit the enter to roll dice: ")
            print("\nRolling dice...")
            dice_value = get_dice_value()
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(player2_name + " moving....")
            player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)

            check_win(player2_name, player2_current_position)

            input_3 = input("\n" + player3_name + ": " + " Hit the enter to roll dice: ")
            print("\nRolling dice...")
            dice_value = get_dice_value()
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(player3_name + " moving....")
            player3_current_position = snake_ladder(player3_name, player3_current_position, dice_value)

            check_win(player3_name, player3_current_position)

            input_4 = input("\n" + player4_name + ": "  + " Hit the enter to roll dice: ")
            print("\nRolling dice...")
            dice_value = get_dice_value()
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(player4_name + " moving....")
            player4_current_position = snake_ladder(player4_name, player4_current_position, dice_value)

            check_win(player4_name, player4_current_position)

        def displayScore():
            print("Displaying the Score:")
            print(player1_name,player1_current_position)
            print(player2_name,player2_current_position)
            print(player3_name,player3_current_position)
            print(player4_name,player4_current_position)

        


if __name__ == "__main__":
    start()