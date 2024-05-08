import os
import random
import time

from replit import audio

# till now we have imported all required modules

print("\033[34m","\n\n\n-------------------> Character Builder <----------------------------","\033[0m")
print("\033[31m","         <--------------------------------------------->\n","\033[0m")
print("\nPlease wait geating character builder ready.\n")
print("Loading...")

time.sleep(5)
os.system("clear")


def roll_dice(side):
  '''created a function which stores n number of sides of a dice.
  then it is given to the variable result
  the result uses random.randint to produce radom number from 1 to n
  
  at last we return the variable (here it is result)'''
  result = random.randint(1, side)
  return result


def health():
  '''the function aim is to give the character there health stats
  for that the logic is made like
  *** a variable is also created and in that varialbe this operion shall execute
  1.  roll 1 dice of 6 side
  2.  roll second dice of 12 side
  then it is divided by 2 and the final answer is added by plus 10
  
  at last the variable is return to the function as it contains answer'''
  healthStat = ((roll_dice(6) * roll_dice(12)) / 2) + 10
  return healthStat


def strenght():
  '''the function aim is to give the character there strenght stats
  for that the logic is made like
  *** a variable is also created and in that varialbe this operion shall execute
  1.  roll 1 dice of 6 side
  2.  roll second dice of 8 side
  then it is divided by 2 and the final answer is added by plus 12
  
  at last the variable is return to the function as it contains answer'''
  strenghtStat = ((roll_dice(6) * roll_dice(8)) / 2) + 12
  return strenghtStat


print("------------- GET READY FOR BATTLE  ------------\n\n"
      )  # starting of the programe

# making of character 1
c1_name = input("Name your Legend ----> ")
c1_ability = input("\ncharacter type is (Human, Elf, Wizard, Orc) ----> ")
print("\n", c1_name)
c1_health = health()
c1_strenght = strenght()
print("\n", "HEALTH ------>", c1_health, "\n")
print("\n", "STRENGHT --->", c1_strenght)
print()

print("\n\n\n", "who is the opponent ? \n\n\n")

#making of character 2
c2_name = input("Name your Legend ---->  ")
c2_ability = input("\ncharacter type is (Human, Elf, Wizard, Orc) ----> ")
print("\n", c2_name)
c2_health = health()
c2_strenght = strenght()
print("\n", "HEALTH ------>", c2_health)
print("\n", "STRENGHT --->", c2_strenght)
print()
"-----------------------starting of the fight----------------------"

round = 1
winner = None
while True:
  time.sleep(2)
  os.system("clear")
  print("---------------BATTLE TIME--------------\n\n")

  c1_Dice = roll_dice(6)
  c2_Dice = roll_dice(6)
  difference = abs(c1_strenght - c2_strenght) + 1

  # Update the health of both characters based on the outcome of the round
  if c1_Dice > c2_Dice:
    c2_health -= difference  # Reduce c2's health
    print("\033[33m",c1_name, "wins round\n","\033[0m")
  elif c2_Dice > c1_Dice:
    c1_health -= difference  # Reduce c1's health
    print("\033[36m",c2_name, "wins round\n","\033[0m")
  else:
    print("\nTheir swords clash and they draw round\n")

  print(c1_name, "\nHealth ----> ", c1_health, "\n")
  print(c2_name, "\nHealth ----> ", c2_health, "\n")

  # Check if any character's health is less than or equal to 0
  if c1_health <= 0:
    print(c1_name, "has died")
    winner = c2_name
    break
  elif c2_health <= 0:
    print(c2_name, "has died")
    winner = c1_name
    break
  else:
    print("--------------> And they're both standing for the next round\n")
    round += 1

time.sleep(1)
os.system("clear")
print("\n⚔️ YOU HAD A BGREAT BATTLE TIME ⚔️\n\n")

print("\033[32m",winner, "has won in", round, "rounds 🏆🏆\n\n","\033[0m")
print(
    "times to clelebrate. 🥳🥂\n\nPlaying song...(FIFA france 2018 celebration)")
celebration = audio.play_file('france.mp3')
