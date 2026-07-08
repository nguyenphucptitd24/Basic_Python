import math
def calculator(a, b):
    angle_rad = math.atan(a / b)
    angle_deg = math.degrees(angle_rad)
    result = round(angle_deg)
    print(f"{result}{chr(176)}")
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    calculator(a,b)
    