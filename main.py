# ====== tarun_code.py ====== # 
import random
min = 1
max = 6

print('Welcome To Dice Game')
while True:
  print()
  choice = int(input("1. Play Game\n2. About Game\n3. Exit\nEnter Your Choice -> "))
  if choice == 1:
    roll_choice = input('Ready to roll? (y/n)')
    print()
    while roll_choice.lower() == 'y':
      num1 = random.randint(min,max)
      num2 = random.randint(min,max)
      print(f'First Number  -> {num1}')
      print(f'Second Number -> {num2}')
      if num1+num2 in (7,11):
        print("SUM ->", num1+num2)
        print("YOU WIN !!")
        print("-"*100)
        print()
        roll_choice = input("Want to try again? (y/n)")
      else:
        print()
        print("You lost")
        roll_choice = input("Want to try again? (y/n)")
      
  elif choice == 2:
    print()
    print("Dice Game")
    print("In this game, the user is allowed to roll dice twice, and if the sum of the results are rolling are equal to 7 or 11, the player wins. Else they lose")
    print('All the Best!')

  elif choice == 3:
    print()
    print("Thanks for playing!")
    break
  else:
    pass
