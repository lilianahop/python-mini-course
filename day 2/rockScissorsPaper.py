# create rock scissors paper program that asks for user input
# 0 = rock 1 = scissors 2 = paper

import random

def whatIsIt(num):
  if num < 0 or num > 2: 
    return "You gave a wrong number! Number has to be between 0 and 2"
  choices = ["Rock", "Scissors", "Paper"]
  return choices[num]

#gives back 0-2 at random
def computerChoice():
  return random.randint(0, 2)

def rockScissorsPaper():
  #Code Here
  user_choice = input("choose Rock or Scissors or Paper: ")
  print(user_choice)
  if user_choice == "Rock" or user_choice == "Paper" or user_choice == "Scissors": 
    print("Valid")
  else:
    print("Invalid")
  
  computer_response = whatIsIt(computerChoice())
  print(computer_response)
  if computer_response == user_choice:
    print("It's a tie.")
  else: 
    if user_choice == "Rock":
      if computer_response == "Scissors":
        print("User won")
      if computer_response == "Paper":
        print("Computer won")
    elif user_choice == "Scissors":
      if computer_response == "Rock":
        print("Computer won")
      if computer_response == "Paper":
        print("User won")
    elif user_choice == "Paper":
      if computer_response == "Rock":
        print("Computer won")
      if computer_response == "Scissors":
        print("User won")
  
  

  #print random computer response
  # print(whatIsIt(computerChoice()))

rockScissorsPaper()


