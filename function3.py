# import random
def reduce_list(numbers):
  return list(dict.fromkeys(numbers))

my_list = reduce_list([1,2,2,3,15,16,16,25])

my_list.remove(max(my_list))

  
