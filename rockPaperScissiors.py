#To play rock paper sciccors
import random

def getChoices():
  list_choice=["Rock","Paper","Scissors"]
  randOpt=random.choice(list_choice)
  return randOpt

def choiceComparator():
  i="Yes"
  human=0
  computer=0
  while (i=="Yes"):
    humOpt=input("\n\tEnter your choice (Rock/Paper/Scissors):") 
    compOpt=getChoices()
    print("\n\tComputer's choice: ",compOpt)
    if (compOpt=="Rock" and humOpt=="Paper"):
      human+=1
    elif (compOpt=="Rock" and humOpt=="Scissors"):
      computer+=1
    elif (compOpt=="Paper" and humOpt=="Rock"):
      computer+=1
    elif (compOpt=="Paper" and humOpt=="Scissors"):
      human+=1
    elif (compOpt=="Scissors" and humOpt=="Rock"):
      human+=1
    elif (compOpt=="Scissors" and humOpt=="Paper"):
      computer+=1
    i=input("\n\tDo you want to continue (Yes/No):")
    if (i=="No"):
      print("\n\tFINAL RESULT")
      print("\n\tComputer: ",computer)
      print("\n\tHuman: ",human)
      if (human>computer):
        print("\n\tCongratulation,human won\n\n")
      elif (human<computer):
        print("\n\tCongratulation, computer won\n\n")
      else:
        print("\n\tBoth human and computer have ht same points\n\n")

choiceComparator()