import random 
secret_codes = ("Ice Cream", "Napoleon", "France", "Europa")
def secret():
  print("Lets do a coin toss!")
  coin_flip = random.choice(["Heads", "Tails"])
  if coin_flip == "Heads":
    print("You scored heads!: List is saved")
    print(secret_codes)
  elif coin_flip == "Tails":
    print("Your scored Tails!: List will self-destruct")
    print("Empty_list = []")
  return coin_flip

