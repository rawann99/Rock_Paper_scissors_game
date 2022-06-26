import random as r

game = {
    "rock": ''' _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) ''',

    "paper": '''_______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''',
    "scissors": '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''',
}
enter_user = int(input("What do U choose? Type 0 for Rocket, 1 for paper and 2 for scissors."))
computer = ["rock", "paper", "scissors"]
choose_computer = r.randint(0, len(computer) - 1)
# print(choose_computer)
# print(game[computer[enter_user]])
if enter_user == choose_computer:
    print(game[computer[enter_user]], "\n", "computer choose: '\n'", game[computer[choose_computer]], "\n",
          "It's a draw")
elif enter_user == 0:
    if computer[choose_computer] == "scissors":
        print(game[computer[enter_user]], "\n", "computer choose:'\n'", game[computer[choose_computer]], "\n",
              "You win!")
    else:
        print(game[computer[enter_user]], "\n", "computer choose:'\n'", game[computer[choose_computer]], "\n",
              "You lose.")
elif enter_user == 1:
    if computer[choose_computer] == "scissors":
        print(game[computer[enter_user]], "\n", "computer choose:'\n'", game[computer[choose_computer]], "\n",
              "You lose")
    else:
        print(game[computer[enter_user]], "\n", "computer choose:'\n'", game[computer[choose_computer]], "\n",
              "You win!")
elif enter_user == 2:
    if computer[choose_computer] == "rock":
        print(game[computer[enter_user]], "\n", "computer choose:'\n'", game[computer[choose_computer]], "\n",
              "You lose")
    else:
        print(game[computer[enter_user]], "\n", "computer choose:'\n'", game[computer[choose_computer]], "\n",
              "You win!")
        import random as r
game = {
  "rock": ''' _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) ''' ,

  "paper": '''_______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''',
  "scissors": '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''',
}
enter_user=int(input("What do U choose? Type 0 for Rocket, 1 for paper and 2 for scissors."))
computer=["rock","paper","scissors"]
choose_computer=r.randint(0,len(computer)-1)
#print(choose_computer)
#print(game[computer[enter_user]])
if enter_user== choose_computer:
    print(game[computer[enter_user]],"\n","computer choose: '\n'",game[computer[choose_computer]],"\n","It's a draw")
elif enter_user == 0:
    if computer[choose_computer] =="scissors" :
        print(game[computer[enter_user]],"\n","computer choose:'\n'",game[computer[choose_computer]],"\n","You win!")
    else:
        print( game[computer[enter_user]],"\n" ,"computer choose:'\n'",game[computer[choose_computer]],"\n","You lose.")
elif enter_user == 1:
    if computer[choose_computer] =="scissors" :
        print(game[computer[enter_user]],"\n","computer choose:'\n'",game[computer[choose_computer]],"\n","You lose")
    else:
        print( game[computer[enter_user]],"\n" ,"computer choose:'\n'",game[computer[choose_computer]],"\n","You win!")
elif enter_user == 2:
    if computer[choose_computer] == "rock":
        print(game[computer[enter_user]], "\n", "computer choose:'\n'", game[computer[choose_computer]], "\n",
              "You lose")
    else:
        print(game[computer[enter_user]], "\n", "computer choose:'\n'", game[computer[choose_computer]], "\n",
              "You win!")