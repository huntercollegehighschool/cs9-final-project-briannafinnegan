"""
Name(s): Brianna Finnegan
Name of Project: Hangman
"""

from page1 import word_list
import random
print("welcome to hangman! you get 7 wrong turns to guess the word.")
word = random.choice(word_list)
list_word = list(word)
#print("['_'] " * len(word))
#guess = input("enter a letter: ")
guess_list = []
#guess_list.append(guess)


while True:
  wrong = 0
  for i in word:
   if i in guess_list: 
     print(i, end = " ")
   else:
     print("_", end = " ")  
     wrong += 1
  print(" ")
    
  if wrong == 0:
    print("you won, the word was", word)
    break
  guess = str(input("enter a letter: "))
  guess_list.append(guess)
   





     