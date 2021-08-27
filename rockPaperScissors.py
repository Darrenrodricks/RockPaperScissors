import random

a = ["Rock", "Paper", "Scissors"]

enemy_hand = random.choice(a)

player = False

while player == False:
    player = input("Please pick: Rock, Paper or Scissors: ")
    if player.casefold() == enemy_hand.casefold():
        print("It was a Tie! You picked {} and the computer also chose {}".format(player, enemy_hand))
    elif player.casefold() == "Rock".casefold():
        if enemy_hand.casefold() == "Paper".casefold():
            print("Oh No! You have been consumed by Paper! You picked {} and the computer picked {}!".format(player,
                                                                                                             enemy_hand))
        elif enemy_hand.casefold() == "Scissors".casefold():
            print("Congrats, You smashed the Scissors! You picked {} and the computer picked {}!".format(player,
                                                                                                         enemy_hand))
    elif player.casefold() == "Paper".casefold():
        if enemy_hand.casefold() == "Scissors".casefold():
            print(
                "Oh No! You have been sliced by the Scissors! You picked {} and the computer picked {}!".format(player,
                                                                                                                enemy_hand))
        elif enemy_hand.casefold() == "Rock".casefold():
            print(
                "Congrats, You consumed the Rock! You picked {} and the computer picked {}!".format(player, enemy_hand))
    elif player.casefold() == "Scissors".casefold():
        if enemy_hand.casefold() == "Rock".casefold():
            print("Oh No! You have been smashed by Rock! You picked {} and the computer picked {}!".format(player,
                                                                                                           enemy_hand))
        if enemy_hand.casefold() == "Paper".casefold():
            print(
                "Congrats, You sliced the Paper! You picked {} and the computer picked {}!".format(player, enemy_hand))
    else:
        print("That was not an option, Try again!")
