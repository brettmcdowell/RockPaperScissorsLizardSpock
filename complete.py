def game_conditions():
  final_one = finalsign[0]
  final_two = finalsign[1]
  if (final_one == 'C' and final_two == 'P'):
    winner = '1'
  elif (final_one == 'P' and final_two == 'C'):
    winner = '2'
  elif (final_one == 'P' and final_two == 'R'):
    winner = '1'
  elif (final_one == 'R' and final_two == 'P'):
    winner = '2'
  elif (final_one == 'R' and final_two == 'L'):
    winner = '1'
  elif (final_one == 'L' and final_two == 'R'):
    winner = '2'
  elif (final_one == 'L' and final_two == 'S'):
    winner = '1'
  elif (final_one == 'S' and final_two == 'L'):
    winner = '2'
  elif (final_one == 'S' and final_two == 'C'):
    winner = '1'
  elif (final_one == 'C' and final_two  == 'S'):
    winner = '2'
  elif (final_one == 'C' and final_two == 'L'):
    winner = '1'
  elif (final_one == 'L' and final_two == 'C'):
    winner = '2'
  elif (final_one == 'L' and final_two == 'P'):
    winner = '1'
  elif (final_one == 'P' and final_two == 'L'):
    winner = '2'
  elif (final_one == 'P' and final_two == 'S'):
    winner = '1'
  elif (final_one == 'S' and final_two == 'P'):
    winner = '2'
  elif (final_one == 'S' and final_two == 'R'):
    winner = '1'
  elif (final_one == 'R' and final_two == 'S'):
    winner = '2'
  elif (final_one == 'R' and final_two == 'C'):
    winner = '1'
  elif (final_one == 'C' and final_two == 'R'):
    winner = '2'
  elif (final_one == final_two or final_two == final_one):
    winner = 'D'
  print(winner)

def sign_selection():
  sign_selection_process = True
  while sign_selection_process == True:
    print("Enter choice: \n Rock = R \n Paper = P \n Scissors = C \n Lizard = L \n Spock = S \n")
    conditionlist = ['R','P','C','L','S']
    choice_one = input("Player 1, please select a sign: ")
    choice_one = choice_one.upper()
    finalsign.append(choice_one)
    if choice_one in conditionlist:
      choice_one = True
    else:
      sign_selection_process = False
    choice_two = input("Player 2, please select a sign: ")
    choice_two = choice_two.upper()
    finalsign.append(choice_two)
    if choice_two in conditionlist:
      choice_two = True
    else:
      sign_selection_process = False
    if choice_two and choice_one == True:
      game_conditions()
    else:
      print("Please enter valid input.\n")
      finalsign.clear()
      sign_selection()
    break

finalsign = []
sign_selection()
