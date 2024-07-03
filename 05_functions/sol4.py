import math

def circleStats(radius):
    area=round(math.pi*radius**2 , 2)
    circumference = round(2*math.pi*radius,2)
    
    return area,circumference

area,circumference = circleStats(4)

print("Area of the Circle : " , area , "Circumference of the circle : " , circumference)