import math
import _random
import time

name = raw_input("Name?")
print "Hello, " + name, "Time to play hangaman"
print ""

time.sleep(10)
print "Start guessing "
time.sleep(5)
word = "Secret"
guesses = ''
turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print char,
        else:
             print "_"
             failed += 1
             if failed == 0:
                 print "You won"
                 print
                 guess = raw_input("guess a char:")
                 if guess not in word:
                     turns -= 1
                     print "Wrong"
                     print  "You have", + turns,'more guesses'
                     if turns == 0:
                         print "You lose"