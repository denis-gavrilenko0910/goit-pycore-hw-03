from random import randint

def number_gen(a, b):
  return randint(a,b)

def get_numbers_ticket(min, max, quantity):
  result = []
  if min >= 1 and 1 < max < 1000 and min < quantity < max:
    while quantity != 0:
      num = number_gen(min, max)
      if not num in result:
        result.append(num)
        quantity -= 1
  
  return sorted(result)

lottery_numbers = get_numbers_ticket(1 , 49 , 6)
print ("Ваши лотерейные числа:", lottery_numbers)