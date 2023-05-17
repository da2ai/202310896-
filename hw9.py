class point :
  def __init__(self, x=0, y=0):
    self.__x = x
    self.__y = y

  def show(self):
    print(f'({self.__x},{self.__y})')

  def set(self, x ,y):
    self.__x=x
    self.__y=y

  def get(self):
    return (self.__x, self.__y)

def test():
  p1 = point()
  p2 = point(2,3)

  p1.show(); print()

  p1.set(10,20); p1.show(); print()

  p2.show();print()

  x,y=p2.get()
  print(f'x={x}, y={y}')

if __name__=='__main__':
  test()