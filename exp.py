while True:
  # time.sleep(1)
  os.system("clear")
  print("---------------BATTLE TIME--------------\n\n")

  c1_Dise = roll_dice(6)
  c2_Dise = roll_dice(6)

  # abs is a function which make sure that the ouput must be positve
  difference = abs(c1_strenght - c2_strenght) + 1

  if c1_Dise > c2_Dise:  # if player 1 is winner
    "we have low down the health of the player 2 by minusing it by difference"
    c2_health -= difference
    # also we can write c2_health -= difference. it is one and same
    if round == 1:
      print(c1_name, "\nis fist winner")
    else:
      print(c1_name, "\nwins round")

  elif c2_Dise > c1_Dise:  # if player 2 is winner
    "we have low down the health of the player 1 by minusing it by difference"
    c2_health -= difference
    # also we can write c2_health -= difference. it is one and same
    if round == 1:
      print(c2_name, "\nis winner of round one")
    else:
      print(c2_name, "\nwins round")
  else:  # if there is an tie
    print("\nThrer swords clash and they draw round\n")




print(c1_name)
print("\nhealth ----> ", c1_health)
print("\n")
print(c2_name)
print("\nhealth ----> ", c2_health)
print()
"---------------------now concluding the battele------------------"
if c1_health >= 0:
  print(c1_name, "had died")
  winner=c1_name
  break
elif c2_health >= 0:
  print(c2_name, "had died")
  winner= c2_name
  break
else:
  print("and they're both standing for the next round\n")
  round +=1
  # continue