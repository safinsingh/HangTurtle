import random
import os
import time
import re
from collections import OrderedDict
print
def remDups(orig): 
    fixList = [] 
    for num in orig: 
        if num not in fixList: 
            fixList.append(num) 
    return fixList 
      
# Driver Code 

hangturtle_stages=['''

   ________
  |        |
  |        |
  |
  |
  |
  |
----- 
''',
'''

   ________
  |        |
  |        |
  |        O
  |
  |
  |
-----
''',
'''

   ________
  |        |
  |        |
  |        O
  |        |
  |        |
  |
-----
''',
'''

   ________
  |        |
  |        |
  |        O
  |        |--
  |        |
  |
-----
''',
'''

   ________
  |        |
  |        |
  |        O
  |      --|--
  |        |
  |       
-----
''',
'''

   ________
  |        |
  |        |
  |        O
  |      --|--
  |      --|
  |       
-----
''',
'''

   ________
  |        |
  |        |
  |        O
  |      --|--
  |      --|--
  |
-----
''']

#print(hangturtle_stages[0])
#time.sleep(1)
#os.system('cls')

wordBase=["turtle","message","hello","guess","python","trinket","googlechrome"]

hangWord=random.choice(wordBase)

hangWordArray=[]

for everyChar in hangWord:
  hangWordArray.append(everyChar)
newHW = remDups(hangWordArray)
newHW.sort()

print("Welcome to hangturtle!")

stages=0
print(hangturtle_stages[stages])

i=1
while i <= int(len(hangWord)):
  print("_"),
  i+=1

print
print

y=0

correctLetters=[]
incorrectLetters=[]

while y < 100:
  x=0
  i=0
  print
  print("Incorrect Letters:"),
  print(incorrectLetters)
  guessLetter = raw_input("Guess a letter: ")
  print
  for char in str(hangWord):
    if str(char) == str(guessLetter):
      if x == 0:
        correctLetters.append(char)
        x+=1
  correctLetters = remDups(correctLetters)
#    else:
#      print("_")
  for letter in str(hangWord):
    if letter in correctLetters:
      print(letter),
    else:
      print("_"),
  print
  if guessLetter not in hangWord:
      stages+=1
      incorrectLetters.append(guessLetter)
  i+=1
  print
  
  correctLetters.sort()
  y+=1
  
  print(hangturtle_stages[stages])
  if correctLetters == newHW:
    print("you win!")
    break
  if stages == 6:
    print("you lose!")
    break
 
