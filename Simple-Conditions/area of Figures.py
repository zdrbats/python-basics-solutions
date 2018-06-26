import math
figure = input()
area = 0
if figure == 'square':
    lenght = float(input())
    area = lenght*lenght
elif figure == 'rectangle':
    lenght = float(input())
    brigth = float(input())
    area = lenght*brigth
elif figure == 'circle':
    radius = float(input())
    area =  math.pi * radius * radius
elif figure == 'triangle':
    lenght = float(input())
    hight = float(input())
    area = lenght * hight /2
else:
    pass
area = float("{0:.3f}".format(area))
print(area)