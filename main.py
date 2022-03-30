ply1_score=0
ply2_score=0

round=1

from func import roll_dice,roll_value 
# from details import username

def username():
  plyusername = input("username: ")
  return plyusername

def password():
  plypassword = input("Please enter your password: ")
  return plypassword



valid= False



def check_for_user(username, password):
  user_found = False
  file = open("details.csv", "r")
  for line in file:
    line = line.strip()
    line = line.split(",")
    if username == line[0]:
      if password == line[1]:
        user_found = True
      else:
        print("\033[31mIncorrect password!\033[0m")
  file.close()
  return user_found

users = []

while len(users) < 2:
  # Indicate who is logging in
  print(f"PLAYER {len(users) + 1} SIGN IN")
  
  # Ask for a username
  given_username = username()
  # Ask for a password
  given_password = password()
  
  # Check your database
  user_found = check_for_user(given_username, given_password)

  if user_found:
    users.append(given_username)
  

ply1username, ply2username = users


while round <6:
  print(f"\n\033[41m  Round: {round}  \033[0m")
    
  #Rolls the dice and assign that dice roll to "ply1roll" & "ply2roll".
  
  ply1roll1 = roll_dice("Player 1, enter 'r' to roll the dice. \n")
  
  ply1roll2 = roll_dice("Player 1, enter 'r' to roll the dice. \n")
  
  ply1_score += roll_value(ply1roll1 + ply1roll2) #Value of Player 1s roll.
  
  
  if ply1roll1 == ply1roll2:
    ply1roll3 = roll_dice("Player 1, enter 'r' to roll the dice. \n")
    ply1_score += roll_value(ply1roll3)
  
  if ply1_score < 0:
    ply1_score = 0
  
  ply2roll1 = roll_dice("Player 2, enter 'r' to roll the dice. \n")
  
  ply2roll2 = roll_dice("Player 2, enter 'r' to roll the dice. \n")
  
  ply2_score += roll_value(ply2roll1 + ply2roll2) #Value of Player 2s roll.
  
  if ply2roll1 == ply2roll2:
    ply2roll3 = roll_dice("Player 2, enter 'r' to roll the dice. \n")
    ply2_score += roll_value(ply2roll3)
  
  if ply2_score < 0:
    ply2_score = 0

  round +=1

print(f"ply1score: {ply1_score}")

print(f"ply2score: {ply2_score}")

winner = None
if ply1_score > ply2_score:
  winner = ply1username
elif ply1_score < ply2_score: 
  winner = ply2username
else:
  print("try rolling 1 more time")
  while winner is None:
    ply1roll = roll_dice("Player 1, enter 'r' to roll the dice. \n")
    ply2roll = roll_dice("Player 2, enter 'r' to roll the dice. \n")
    if ply1roll > ply2roll:
      winner = ply1username
    elif ply1roll < ply2roll:
      winner = ply2username
    else:
      print("You rolled the same number... Try again!")  
print(f"\n\033[32m  Winner is {winner}!   \033[0m")

