import random
print("WELCOME TO ROCK,PAPER & SCISSOR GAME")
print('0-rock\n1-paper\n2-scissor')
option=['rock','paper','scissor']
user_score=0
computer_score=0
running=True
while running:
  user_choice_index = int(input("enter your choice:"))
  if user_choice_index<3:
    user_choice = option[user_choice_index]
    computer_choice_index=random.randint(0,2)
    computer_choice=option[computer_choice_index]
    if user_choice_index==computer_choice_index:
      print(f"you choose:",user_choice," and the computer choose:",computer_choice,"\nIt's a tie match")
    elif (user_choice_index==0 and computer_choice_index==2)or(user_choice_index==1 and computer_choice_index==0)or(user_choice_index==2 and computer_choice_index==1):
      print("you choose:",user_choice," and the computer choose",computer_choice,"\n you win")
      user_score+=1
    else:
      print(f"you choose:",user_choice," and the computer choose:",computer_choice,"\n computer win")
      computer_score+=1
  else:
    print("invalid option")
  play_again=input("play again?(y/n):").lower()
  if not play_again=='y':
    running=False
print("the user score is:",user_score)
print("the computer score is:",computer_score)
print("THANKS FOR THE PLAYING")
