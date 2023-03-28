def sale_rate(rate):
  global get_fixed_price
  rate=get_fixed_price

def sale_price(prompt):
  s=int(input(prompt))
  return s

def get_fixed_price(price):
  t=price*100/(100-rate)
  return t

rate=int(input('할인율은? '))
p=sale_price('A상품의 할인 가격은? ')
q=sale_price('B상품의 할인 가격은? ')
print('A제품의 정가는',int(get_fixed_price(p)),"원")
print('B제품의 정가는',int(get_fixed_price(q)),"원")