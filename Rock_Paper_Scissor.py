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

ascii_images=[rock,paper,scissors]  
userInput=int(input("What do you choose? Type 0 for Rock, 1 for Paper or  2  for Scissor.\n "))
print(ascii_images[userInput])

computerInput=random.randint(0,2)
print("computer Choice:")
print(ascii_images[computerInput])

if userInput>=3 or userInput<0:
  print("You typed an invalid number, you lose!")

elif userInput==2 and computerInput==0:
  print("You lose!")
elif computerInput>userInput:
  print("You losse!.")
elif userInput>computerInput:
  print("You win!")
elif computerInput==userInput:
  print("It's a tie")
