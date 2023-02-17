import os, sys, random

def cls():
  os.system('cls||clear')

def quit():
  print("Dzięki za grę i do zobaczenia.")
  sys.exit(0)

def get_empty_board():
  board = []
  for i in range(3):
    board.append([])
    for i in range(3):
      board[-1].append(".")
  return board

def get_human_coordinates(character, board):
  human_input_row = input("Wprowadź literę rzędu (od A do C"
                          ")")
  if human_input_row.lower() == "quit":
    quit()
  while human_input_row.upper() != "A" and human_input_row.upper(
  ) != "B" and human_input_row.upper() != "C":
    human_input_row = input("Błędne dane. Wprowadz literę rzędu (od A do C"
                            ")")

  try:
    human_input_col = int(input("Wprowadź kolumnę (od 1 do 3"
                                ")"))
    while human_input_col != 1 and human_input_col != 2 and human_input_col != 3:
      human_input_col = int(
        input("Błędne dane. Wprowadz kolumnę (od 1 do 3"
              ")"))
  except ValueError:
    human_input_col = int(
      input("Wprowadź liczbę a nie znak. Wprowadz kolumnę (od 1 do 3"
            ")"))
    while human_input_col != 1 and human_input_col != 2 and human_input_col != 3:
      human_input_col = int(
        input("Błędne dane. Wprowadz kolumnę (od 1 do 3"
              ")"))

  input_coordinates_dict = {
    "A1": (0, 0),
    "A2": (0, 1),
    "A3": (0, 2),
    "B1": (1, 0),
    "B2": (1, 1),
    "B3": (1, 2),
    "C1": (2, 0),
    "C2": (2, 1),
    "C3": (2, 2)
  }
  human_input_row = human_input_row.upper()
  row_coordinate = human_input_row
  col_coordinate = human_input_col
  col_coordinate = str(col_coordinate)
  coordinates = [row_coordinate, col_coordinate]
  coordinates_string = "".join(coordinates)
  coordinates_tuple = input_coordinates_dict[coordinates_string]
  if board[coordinates_tuple[0]][coordinates_tuple[1]] == ".":
    board[coordinates_tuple[0]][coordinates_tuple[1]] = character
  elif board[coordinates_tuple[0]][coordinates_tuple[1]] == "X" or board[
      coordinates_tuple[0]][coordinates_tuple[1]] == "O":
    print("Na tym polu jest już znak. Spróbuj wprowadzić inne współrzędne.")
    get_human_coordinates(character, board)
  return (board)


def display_board(board):
  line = "  ---+---+---"
  print("   1   2   3")
  print(line)
  print("A ", board[0][0], "|", board[0][1], "|", board[0][2])
  print(line)
  print("B ", board[1][0], "|", board[1][1], "|", board[1][2])
  print(line)
  print("C ", board[2][0], "|", board[2][1], "|", board[2][2])
  print(line)
  return board


def is_board_full(board):
  return not any("." in sl for sl in board)


def check_win(board):
  if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X' or board[
      0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
    return True
  if board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X' or board[
      1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
    return True
  if board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X' or board[
      2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
    return True
  if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X' or board[
      0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
    return True
  if board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X' or board[
      0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
    return True
  if board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X' or board[
      0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
    return True
  if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' or board[
      0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
    return True
  if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X' or board[
      0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
    return True
  else:
    return False
    
def menu_again():
  again = input("Chcesz zagrać jeszcze raz? (t/n): ")
  if again.lower() == "t":
    main_menu()
  else:
    quit()


def main_menu():
  print(
    "Witamy w grze w kółko i krzyżyk.\nŻeby wyjść z gry wpisz 'quit' zamiast litery rzędu.\n"
  )
  oponent = input(
    "Wybierz czy chcesz zagrać z komputerem czy człowiekiem \n('k' - komputer/ 'c' - człowiek): "
  )
  if oponent.lower() == "k":
    whos_first()
  elif oponent.lower() == "c":
    game()
  else:
    print("Wprowadziłeś coś innego niż 'k' lub 'c'. Spróbuj jeszcze raz.")
    main_menu()

def choose_character():
  is_circle = True
  character_choice = input(
    "Wybierz czy chcesz zacząć grać kółkiem ('O') czy krzyżykiem ('X'): ")
  if character_choice.lower() == "o":
    is_circle = True
  elif character_choice.lower() == "x":
    is_circle = False
  else:
    print("Wprowadziłeś coś innego niż 'X' lub 'O', spróbuj jeszcze raz")
    choose_character()
  return is_circle 

def whos_first():
  who = input("Kto zaczyna komputer czy Ty (K/T)? ")
  if who == "k":
    AI_game_k()
  elif who == "t":
    unbeatable_AI_game()
  else:
    print("Wbrałeś coś innego niż 'K' lub 'T', spróbuj jeszcze raz")
    whos_first() 

def game():
  GAME_ON = True
  is_circle = choose_character()
  board = get_empty_board()
  while GAME_ON:
    if is_circle == True:
      character = "O"
    else:
      character = "X"
    get_human_coordinates(character, board)
    cls()
    display_board(board)
    if character == "X":
      is_circle = True
    else:
      is_circle = False
    if check_win(board):
      GAME_ON = False
      print("Wygrał gracz grający znakiem:", character)
      menu_again()
    if is_board_full(board):  #
      GAME_ON = False
      print("Remis!")
      menu_again()


def AI_game_k():
  GAME_ON = True
  is_circle = True
  board = get_empty_board()
  while GAME_ON:
    if is_circle == True:
      character = "X"
    else:
      character = "O"
    get_random_ai_coordinates(character, board)
    cls()
    display_board(board)
    if check_win(board):
      GAME_ON = False
      print("Wygrał gracz grający znakiem:", character)
      menu_again()
    if is_board_full(board):
      GAME_ON = False
      print("Remis!")
      menu_again()
    character = "O"
    get_human_coordinates(character, board)
    display_board(board)
    if check_win(board):
      GAME_ON = False
      print("Wygrał gracz grający znakiem:", character)
      menu_again()
    if is_board_full(board):
      GAME_ON = False
      print("Remis!")
      menu_again()


def AI_game():
  GAME_ON = True
  is_circle = True
  board = get_empty_board()
  while GAME_ON:
    if is_circle == True:
      character = "X"
    else:
      character = "O"
    get_human_coordinates(character, board)
    display_board(board)
    if check_win(board):
      GAME_ON = False
      print("Wygrał gracz grający znakiem:", character)
      menu_again()
    if is_board_full(board):  #
      GAME_ON = False
      print("Remis!")
      menu_again()
    character = "O"
    get_random_ai_coordinates(character, board)
    cls()
    display_board(board)

def get_random_ai_coordinates(character, board):
  random_ai_input_row = random.randint(0, 2)
  random_ai_input_col = random.randint(0, 2)
  random_ai_coordinates_tuple = (random_ai_input_row, random_ai_input_col)
  if board[random_ai_coordinates_tuple[0]][
      random_ai_coordinates_tuple[1]] == ".":
    board[random_ai_coordinates_tuple[0]][
      random_ai_coordinates_tuple[1]] = character
  elif board[random_ai_coordinates_tuple[0]][
      random_ai_coordinates_tuple[1]] == "X" or board[
        random_ai_coordinates_tuple[0]][random_ai_coordinates_tuple[1]] == "O":
    get_random_ai_coordinates(character, board)

def unbeatable_AI_game():
  GAME_ON = True
  is_circle = True
  board = get_empty_board()
  while GAME_ON:
    if is_circle == True:
      character = "X"
    else:
      character = "O"
    get_human_coordinates(character, board)
    display_board(board)
    if check_win(board):
      GAME_ON = False
      print("Wygrał gracz grający znakiem:", character)
      menu_again()
    if is_board_full(board):
      GAME_ON = False
      print("Remis!")
      menu_again()
    character = "O"
    get_unbeatable_ai_coordinates(character, board)
    cls()
    display_board(board)
    if check_win(board):
      GAME_ON = False
      print("Wygrał gracz grający znakiem:", character)
      menu_again()
    if is_board_full(board):
      GAME_ON = False
      print("Remis!")
      menu_again()

def get_unbeatable_ai_coordinates(character, board):
  if board[0][0] == ".":
    board[0][0] = character
  if board[1][1] == "X" and board[0][1] == "X":
    board[2][1] = character
  if board[1][1] == "X" and board[1][0] == "X":
    board[1][2] = character
  if board[1][1] == "X" and board[1][2] == "X":
    board[1][0] = character
  if board[1][1] == "X" and board[2][1] == "X":
    board[0][1] = character
  if board[1][1] == "X" and board[0][2] == "X":
    board[2][0] = character
  if board[1][1] == "X" and board[2][0] == "X":
    board[0][2] = character
  elif board[1][1] == ".":
    board[1][1] = character
  if board[0][0] == "X" and board[0][1] == "X":
    board[0][2] = character
  if board[0][0] == "X" and board[0][2] == "X":
    board[0][1] = character
  if board[0][0] == "X" and board[1][0] == "X":
    board[2][0] = character
  if board[0][0] == "X" and board[2][0] == "X":
    board[1][0] = character
  if board[1][1] == "X" and board[0][2] == "X":
    board[2][0] = character
  if board[1][1] == "X" and board[2][0] == "X":
    board[0][2] = character

main_menu()

# uprościć check_win
