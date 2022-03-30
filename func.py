from random import randint

resetclr = "\033[0m"
yellow = "\033[33m"
red = "\033[31m"

#Feel free to add new defs.
#Dont forget to import new defs into main.py.


def roll_dice(prompt): #Rolls the dice
  not_valid = True
  while not_valid:
    
    user_input = (input(prompt))
    if user_input == "r":
      not_valid = False
      number = randint(1,6)
      print(number)
    elif user_input != "r":
       print(f"{red} You can only enter 'r' to roll the dice! {resetclr}")
  return number

def roll_value(a): #The value of roll 'Even = +10 Points' 'Odd = -5 Points'.
  total = a
  if (a % 2) == 0:
    print(f"{yellow}+10 Points{resetclr}")
    total += 10
  else:
    print(f"{red}-5 Points{resetclr}")
    total -= 5
  return total



