import os
import time
import random


def loading_screen(seconds):
    screens = open("Screen.txt", 'r')
    for lines in screens:
        print(lines, end='')
        time.sleep(seconds)
    screens.close


def unicorn_draw(seconds):
  screens = open("Unicorn.txt", 'r')
  for lines in screens:
    print(lines, end='')
    time.sleep(seconds)
  screens.close

def horse_draw(seconds):
  screens = open("Horse.txt", 'r')
  for lines in screens:
    print(lines, end='')
    time.sleep(seconds)
  screens.close

def zebra_draw(seconds):
  screens = open("Zebra.txt", 'r')
  for lines in screens:
    print(lines, end='')
    time.sleep(seconds)
  screens.close

def donkey_draw(seconds):
  screens = open("Donkey.txt", 'r')
  for lines in screens:
    print(lines, end='')
    time.sleep(seconds)
  screens.close
#Main Code Start
os.system('cls' if os.name == 'nt' else 'clear')
loading_screen(.35)
print("\n")
print("Lucky Unicorns 2022")
print("-----------------------\n")

#1. Users pay an initial amount at the start of the game.
token = None


def numberCheck(question, low, high):
  valid = False
  errorMessageRange = "\nPlease make sure you have entered a value between {} and {}.\n".format(low, high)
  errorMessageValueError = "\nPlease make sure your number is an Integer (a whole number that is above 0)\n"
  
  
  while not valid:
    try:
      global response
      response = int(input(question))
      
      if (low <= response <= high):
        return response
      #4. The maximum amount of money that students can spend on the game is $10 per session.
      else:
        print(errorMessageRange)

    except ValueError:
      print(errorMessageValueError)



#-----------------------MAIN CODE----------------------------------
#2. The cost should be $1 per round and users should press <enter> to play.  The computer should then generate a token that is either a zebra, horse, donkey or unicorn.
numberOfPlays = int(numberCheck("How much rounds? ($1 per round) \nYou may play up to 10 rounds. Enter number and press <enter>: \n", 1, 10))

def main():
  global token
  token = random.randint(0, 3)
  playAgain = True
  def askPlayAgain():
    ask = input("Play again? Enter Y for yes and N for no)")
  if (token == 0):
    print("\n")
    print("\n")
    unicorn_draw(.5)
    print("\n")
    

  elif (token == 1):
    print("\n")
    print("\n")
    horse_draw(.5)
    print("\n")

  elif (token == 2):
    print("\n")
    print("\n")
    zebra_draw(.5)
    print("\n")

  elif (token == 3):
    print("\n")
    print("\n")
    donkey_draw(.5)
    print("\n")
    

while numberOfPlays > 0:
  main()
  numberOfPlays -= 1
  
  


#a. This should be displayed to the user.  
#b. DECISION:
#i. If the token is a unicorn, the user wins $5, 
#ii. if it is a zebra or horse, they win 50c
#iii.  if it is a donkey then they don’t win anything.
 
#5.  The game should allow players to continue / quit provided they have not lost all of their money. 
#6. It should supply appropriate feedback so that the user knows how much money they have won / lost each round and how much money they have left.
#7. Once students have no more money, the game should end (although players do have the option of quitting while they are ahead) 

