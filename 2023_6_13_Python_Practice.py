# #Quiz_1
# station = "Bethesda"
# print("This station is " + str(station) + ".")

# #Quiz_2
# from random import *
# print("It is " + str(randint(4,28)) + ".")

#Quiz_3
url = "http://naver.com"
# my_str_1 = url[7:]
# print(my_str_1)
my_str_2 = url.replace("http://", "") #naver.com
my_str_3 = my_str_2[0:my_str_2.index(".")] #naver
my_str_4 = my_str_3[0:3] #nav
my_str_5 = len(my_str_3) #5
my_str_6 = my_str_3.count("e") #1
password = my_str_3[:3] + str(len(my_str_3)) + str(my_str_3.count("e")) + "!"
print(password)