#DiceRoll.py
#Name: Mariana Chavez
#Date: 03.01.2026
#Assignment: Lab 6
import random

def main():
  #Create an empty list with possible roll values
  counts = [0,0,0,0,0,0,0,0,0,0,0,0,0]
  total_rolls = 10000
  #Create two dice values ranging from 1 - 6 ea    dice2 = random.rantidit(1.,6)ch
  for r in range(total_rolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
  #find the sum total of the two dice
    sum = dice1 + dice2    
    counts[sum] += 1

  #print statictics for dice rolls
  print("Sum: Count: Percentage:")
  for sum in range(2, 13):
    count = counts[sum]
    percentage = (count / total_rolls) * 100
    print(sum, "   ", count, "   ", round(percentage,2),"%")

if __name__ == '__main__':
  main()
