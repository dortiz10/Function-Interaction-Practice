import random
def newFunction():
  dice1 = random.randint(0,6)
  dice2 = random.randint(0,6)
  print(f"First dice value is a {dice1} and second dice value is {dice2}")
  sum = dice1 + dice2
  if sum <= 6:
    print(f'The sum of your dice is {sum}. Unfortunate')
  if sum > 6 and sum < 10:
    print(f"The sum of your dice is {sum}. You have a good chance")
  if sum > 10 or sum == 10:
    print(f"The sum of your dice is {sum}. It looks like a winning roll")
