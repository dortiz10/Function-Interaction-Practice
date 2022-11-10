from math import *

  
# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and         returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).

def sum_squares():
  number1 = int(input("Give us a numbers: "))
  number2 = int(input("Maybe another: "))
  number3 = int(input("Give us a last one: "))
  first = int(pow(number1, 2))
  second = int(pow(number2, 2))
  third = int(pow(number3, 2))
  final = first + second + third
  print(f"Squared result of your given numbers are {final}")
  




########################################################################################################################
# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).

  # def absolute_sum(*args):



########################################################################################################################
# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"

