from math import *
try:
    x1 = int(input("x1?: "))
    y1 = int(input("y1?: "))
    x2 = int(input("x2?: "))
    y2 = int(input("y2?: "))
    x3 = int(input("x3?: "))
    y3 = int(input("y3?: "))
except:
    print("You are an idiot.")
#x1,x2,x3,y1,y2,y3=0,2,1,0,1,3

def slope(a,b,c,d):
    return(str(round((d-b)/(c-a),2)))

def length(a,b,c,d):
    return(round(hypot(c-a,d-b),2))

A_length = length(x1,y1,x2,y2)
B_length = length(x2,y2,x3,y3)
C_length = length(x1,y1,x3,y3)
semi = (A_length+B_length+C_length)/2
try:
    print("The slope of line A is " + slope(x1,y1,x2,y2))
except(ZeroDivisionError):
    print("You have a vertical line.")
try:
    print("The slope of line B is " + slope(x2,y2,x3,y3))
except(ZeroDivisionError):
    print("You have a vertical line.")
try:
    print("The slope of line C is " + slope(x1,y1,x3,y3))
except(ZeroDivisionError):
    print("You have a vertical line.")
print("The length of line A is " + str(A_length))
print("The length of line B is " + str(B_length))
print("The length of line C is " + str(C_length))
print("The area of the triangle is " + str(round(sqrt(semi*(semi-A_length)*(semi-B_length)*(semi-C_length)),2)))
print("The measure of angle A is " + str(round(sqrt(A_length**2 + B_length**2 - 2 * A_length * B_length * cos( )))))
