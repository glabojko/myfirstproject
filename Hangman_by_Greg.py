# Hangman by breakout 6

import random
from words import words_level1
from words import words_level2
from words import words_level3
from words import words_level4
from words import words_level5


def game():
  difficulty_level = int(
    input("Wybierz poziom trudności 1 (łatwy) - 5 (trudny): "))
  lives = 7 - difficulty_level
  if difficulty_level == 1:
    print("\n Masz", lives, "żyć.")
    word = random.choice(words_level1)
  elif difficulty_level == 2:
    print("\n Masz", lives, "żyć.")
    word = random.choice(words_level2)
  elif difficulty_level == 3:
    word = random.choice(words_level3)
  elif difficulty_level == 4:
    print("\nMasz", lives, "życia.")
    word = random.choice(words_level4)
  elif difficulty_level == 5:
    print("\nMasz", lives, "życia.")
    word = random.choice(words_level5)
  else:
    print("\nWprowadź liczbę między 1 a 5")
  print("\nOto słowo do odgadnięcia:\n")
  word_completion = "_" * len(word)
  print(word_completion)
  print("\nJak widać ma ono", len(word), "liter.\n")
  print("Jeśli chcesz wyjść z programu wpisz 'quit'\n")
  end = False
  guessed_letters = []
  guessed_bad_letters = []
  guessed_words = []

  while not end and lives > 0:

    letter = input("Zgadnij literę (lub od razu całe słowo): ").lower()

    if letter == "quit":
      print("Do zobaczenia")
      return quit()
    if len(letter) == 1 and letter.isalpha():
      if letter in guessed_letters:
        print(
          "Tą literę",
          letter,
          "już wpisywałeś, wpisz inną.",
        )
        guessed_letters.append(letter)
        print("Te litery już wpisywałeś i nie ma ich w tym słowie: ",
              guessed_bad_letters)

      elif letter not in word:
        print("Litery:", letter.upper(), "nie ma w tym słowie")
        guessed_letters.append(letter)
        guessed_bad_letters.append(letter)
        print("Te litery już wpisywałeś i nie ma ich w tym słowie: ",
              guessed_bad_letters)
        lives -= 1
        print(display_hangman(lives))
        print("Zostało Ci jeszcze", lives, "życia")

      elif letter in word:
        print("Zgadłeś litera", letter.upper(), "jest w tym słowie!")
        print("litera", letter, "występuje w tym słowie", word.count(letter),
              "razy.")
        guessed_letters.append(letter)
        word_as_list = list(word_completion)
        indices = [
          i for i, guessed_letter in enumerate(word)
          if guessed_letter == letter
        ]
        for index in indices:
          word_as_list[index] = letter
        word_completion = "".join(word_as_list)
        print(word_completion)
        if "_" not in word_completion:
          print("Brawo odgadłeś słowo, chodziło oczywiście o", word.upper(),
                "!")
          end = True

    elif len(letter) != len(word) and letter.isalpha():
      print("To słowo ma", len(word),
            "liter, więc albo wpisz ich tyle albo pojedynczą literę")
      lives -= 1
      print(display_hangman(lives))
      print("Zostało Ci jeszcze", lives, "życia")

    elif len(letter) == len(word) and letter.isalpha():
      if letter in guessed_words:
        print("Już wpisywałeś to słowo", letter)
        guessed_words.append(letter)
      elif letter != word:
        print(letter.upper(), "to nie jest to słowo o które chodzi.")
        lives -= 1
        print(display_hangman(lives))
        print("Zostało Ci jeszcze", lives, "życia")
        guessed_words.append(letter)
        print("Te słowa już wpisywałeś:", guessed_words)
      elif letter == word:
        end = True
        word_completion = word
        print("Brawo odgadłeś słowo, chodziło oczywiście o", word.upper(), "!")

      else:
        print("Skończ wpisywać głupoty.")
        lives -= 1
        print(display_hangman(lives))
        print("Zostało Ci jeszcze", lives, "życia")

    else:
      print("Skończ wpisywać głupoty.")
      lives -= 1
      print(display_hangman(lives))
      print("Zostało Ci jeszcze", lives, "życia")

  if lives == 0:
    print(
      "Sorry man, skończyły Ci się życia. Zawisłeś - przegrwasz. Chodziło o słowo:",
      word.upper())
    print(display_hangman(lives))


def play():
  game()
  while input("Chcesz zagrać jeszcze raz? (T/N): ").lower() == "t":
    game()
  print("Dzięki za grę. Do zobaczenia następnym razem.")


def display_hangman(lives):
  drawing = [  # 0 żyć
    '''
        _______
        |/    |
        |     O
        |    /|\\
        |     |
        |    / \\
        |
      =====
    ''',
    # 1 życie
    '''  
        _______
        |/    |
        |     O
        |    /|\\
        |     |
        |    
        |
      =====
    ''',
    # 2 życia
    ''' 
        _______
        |/    |
        |     O
        |     |
        |     |
        |    
        |
      =====
    ''',
    # 3 życia
    ''' 
        _______
        |/    |
        |     O
        |     
        |     
        |    
        |
      =====
    ''',
    # 4 życia
    ''' 
        _______
        |/    
        |     
        |     
        |     
        |    
        |
      =====
    ''',
    # 5 żyć
    '''  
        
        |    
        |     
        |     
        |     
        |    
        |
      =====
    ''',
    # 6 żyć
    '''  
        
            
             
             
             
            
        
      =====
    ''',
  ]

  return drawing[lives]


play()
