import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
ls = [rock,paper,scissors]
select = int(input("What do you choose? Select '0' for rock, '1' for paper, '2' for scissors\n"))
if select == 0 or select == 1 or select == 2:
    user_choice = ls[select]
    print(f"Your choice: {user_choice}")
    game = random.randint(0,2)
    print(f"Computer chose: {ls[game]}")
    if select == game:
        print("Game Tie!")
    elif (select == 0 and game == 2 ) or (select == 1 and game == 0) or  (select == 2 and game== 1):
        print("You won the match!")
    else:
        print("You lose the match! ")
else:
    print("Invalid! ")

