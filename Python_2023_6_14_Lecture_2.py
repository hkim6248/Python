print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) #2^3 = 8
print(5%3) #2
print(10%3) #1
print(5//3) #1
print(10//3) #3

print(10 > 3) #True
print(4 >= 7) #False
print(10 < 3) #False
print(5 <= 5) #True

print(3 == 3) #True
print (4 == 2) #False
print (3 + 4 == 7) #True

print(1 != 3) #True
print(not(1 != 3)) #False

print((3 > 0) and (3 < 5)) #True
print((3 > 0) & (3 < 5)) #True

print((3 > 0) or (3 > 5)) #True
print((3 > 0) | (3 > 5)) #True

print(5 > 4 > 3) #True
print(5 > 4 > 7) #False

print(2 + 3 * 4) #14
print((2 + 3) * 4) #20
number = 2 + 3 * 4 #14
print(number) #14
number = number + 2 #16
print(number) #16

number += 2 #18
print(number)
number *= 2 #36
print(number)
number /= 2 #18
print(number)
number -= 2 #16
print(number)
number %= 5 #1
print(number)

print(abs(-5)) #5
print(pow(4, 2)) #16
print(max(5, 12)) #12
print(min(5, 12)) #12
print(round(3.14)) #3
print(round(4.99)) #5

from math import *
print(floor(4.99)) #4
print(ceil(3.14)) #4
print(sqrt(16)) #4

from random import *
print(random()) #[0, 1)
print(random()*10) #[1 ~ 10)
print(int(random()*10)) #[0, 10)
print(int(random()*10+1)) #[1, 11)
print(int(random()*45+1)) #[1, 46)
print(randrange(1, 46)) #[1, 46)
print(randint(1, 45)) #[1, 45]

#Quiz 2
date = randint(4, 28)
print(date)
print("Our regular meeting is on the " + str(date) + "th of every month.")