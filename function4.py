import random 
secret_codes = ("Ice Cream", "Napoleon", "France", "Europa")
def secret():
  coin_flip = random.choice(["Heads", "Tails"])
  if coin_flip == "Heads":
    print("List is saved")
    print(secret_codes)
  elif coin_flip == "Tails":
    print("List will self-destruct")
    print("Empty_list = []")
  return coin_flip

