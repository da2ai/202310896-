def rep_char(a,b):
  print(a*b)

def draw_string(name):
  msg1='Hello '+name
  msg2='Welcome to Seoul.'
  if(len(msg1) > len(msg2)):
    nstr = len(msg1)
  else:
    nstr = len(msg2)
  rep_char('-',nstr+3)
  print(f'  {msg1}  ')
  print(f'  {msg2}  ')
  rep_char('-',nstr+3)

name=input('Input his/her name: ')
draw_string(name)

