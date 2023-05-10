shopping_bag={}

print('[구입]')
while True:
  item = input('상품명? ')
  if item=='':
    break
  num=int(input('수량은? '))
  shopping_bag.setdefault(item,num)
  print(f'장바구니에 {item} {num}개가 담겼습니다.')
  print('\n')

print(f'\n>>> 장바구니 보기 : {shopping_bag}')

print('\n')
print('[검색]')
s=input('장바구니에서 확인하고자 하는 상품은? ')
if s in shopping_bag:
  print(f'{s}은(는) {shopping_bag.get(s)}개 담겨 있습니다.')
else :
  print(f'장바구니에 {s}은(는) 없습니다.')