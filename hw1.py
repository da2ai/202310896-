def get_radius(prompt):
    r=int(input(prompt))
    return r

def get_circle_area(i):
    area=3.14*i*i
    return area

radius=get_radius("넓이를 구하고자 하는 원의 반지름은? ")
print("반지름 ",radius,"인 원의 넓이 = 3.14 x ",radius," x ",radius," = ", get_circle_area(radius))