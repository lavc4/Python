# flag = False
# guessed_word = []
# for i in range(5):
#     guessed_word.append("_")
# print(guessed_word)
# while flag is not True:
#     print("hello")

# words = ["player", "happy", "racer", "coder"]
# words[0] is "player"
# words[0] == "player"
# print(words[0])

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 /|\  |
      |
=========
''',  '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',  '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',  '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',  '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',  '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',  '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = -1
print("=+++++++=",len(stages))
while lives > -7:
    print(stages[lives])
    print("---", lives)
    lives -= 1
    print("====", lives)
    