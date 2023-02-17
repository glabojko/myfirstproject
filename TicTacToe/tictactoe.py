import os, sys

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
  human_input_row = input("Wprowadz literę rzędu (od A do C"
                          ")")
  if human_input_row.lower() == "quit":
    quit()
  while human_input_row.upper() != "A" and human_input_row.upper(
  ) != "B" and human_input_row.upper() != "C":
    human_input_row = input("Błędne dane. Wprowadz literę rzędu (od A do C"
                            ")")

  try:
    human_input_col = int(input("Wprowadz kolumnę (od 1 do 3"
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
    game()
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
    print(
      "Niestety tej opcji nie udało nam się jeszcze zakodować. Pracujemy nad tym."
    )
    main_menu()  # AI_game()
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
  if character_choice.lower() == "x":
    is_circle = False
  # else:
  #   choose_character()
  return is_circle

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

main_menu()

# def AI_game()

# poprawić quit ==> na razie tylko do wpisywania rzędu wyjście jest niezbyt eleganckie (repl process died unexpectedly)
# uprościć check_win
# zrobić algorytm do gry z komputerem
