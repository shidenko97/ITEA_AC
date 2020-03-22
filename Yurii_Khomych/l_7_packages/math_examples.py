import math

math.pi
math.e

an_int = 6
a_neg_int = -8
a_float = 2.00

print(math.exp(an_int))
print(math.exp(a_neg_int))
print(math.exp(a_float))

radius = 2
print("The area of a circle with a radius of 2 is:", math.pi * (radius ** 2))


print("math.log(10.43):", math.log(10.43))
print("math.log(20):", math.log(20))
print("math.log(math.pi):", math.log(math.pi))

print("The log10 of 50 is:", math.log10(50))


num = -4.28
a = 14
b = 8
num_list = [10, 8.25, 75, 7.04, -86.23, -6.43, 8.4]
x = 1e-4  # A small value of x

print("The number is:", num)
print("The floor value is:", math.floor(num))
print("The ceiling value is:", math.ceil(num))
print("The absolute value is:", math.fabs(num))
print("The GCD of a and b is: " + str(math.gcd(a, b)))
print("Sum of the list elements is: " + str(math.fsum(num_list)))
print("e^x (using function exp()) is:", math.exp(x) - 1)
print("e^x (using function expml()) is:", math.expm1(x))

math.pow(3, 4)

math.sqrt(81)


angle_In_Degrees = 62
angle_In_Radians = math.radians(angle_In_Degrees)

print("The value of the angle is:", angle_In_Radians)
print("sin(x) is:", math.sin(angle_In_Radians))
print("tan(x) is:", math.tan(angle_In_Radians))
print("cos(x) is:", math.cos(angle_In_Radians))
