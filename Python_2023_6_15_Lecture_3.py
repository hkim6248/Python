#Python_2023_6_15_Lecture_3

sentence_1 = "I am a boy."
print(sentence_1)

sentence_2 = "Python is easy."
print(sentence_2)

sentence_3 = '''
I am a boy.
Python is easy.
'''
print(sentence_3)

KSSN = "990120-1234567"
print("Sex: " + KSSN[7])
print("Year: " + KSSN[0:2])
print("Month: " + KSSN[2:4])
print("Day: " + KSSN[4:6])
print("DOB: " + KSSN[0:6])
print("DOB: " + KSSN[:6])
print("Last 7: " + KSSN[7:14])
print("Last 7: " + KSSN[7:])
print("Last 7: " + KSSN[-7:])

python = "Python is Amazing!"
print(python.lower()) #python is amazing!
print(python.upper()) #PYTHON IS AMAZING!
print(python[0].isupper()) #True
print(len(python)) #18
print(python.replace("Python", "Java")) #Java is Amazing!

index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)
print(python.find("n"))
print(python.find("Java"))
#print(python.index("Java"))
print("Hey?")
print(python.count("n"))

print("a" + "b")
print("a", "b")

#Method 1
print("I am %d years old." %20)
print("I like %s." %"Hyojung")
print("Apple begins with %c." %"A")
#print("Apple begins with %c." %"AB")
print("I am %s years old." %"20")
print("I am %s years old." %20)
print("I like %s and %s." %("red", "blue"))

#Method 2
print("I am {} years old.".format(20))
print("I like {} and {}.".format("red", "blue"))
print("I like {0} and {1}.".format("red", "blue"))
print("I like {1} and {0}.".format("red", "blue"))

#Method 3
print("I am {age} years old and I like {color}".format(age = 20, color = "red"))
print("I am {color} years old and I like {age}".format(age = 20, color = "red"))
print("I am {age} years old and I like {color}".format(color = "red", age = 20))

#Method 4
age = 20
color = "red"
print(f"I am {age} years old and I like {color}.")

#\n
print("I love \nHyojung!")

#\"
#I love "Hyojung"!
print("I love \"Hyojung\"!")

#\\
#print("C:\Users\Hyojung Kim\Desktop\2023_6_13_Hyojung_Kim\GitHub\Python")
print("C:\\Users\\Hyojung Kim\\Desktop\2023_6_13_Hyojung_Kim\\GitHub\\Python")

#\r
print("Red Apple\rPine")
print("Red  Apple\rPine")

#\b
print("Redd\bApple")

#\t
print("Red\tApple")

#Quiz 3
url_1 = "http://naver.com"
#print(url[7:])
url_2 = url_1.replace("http://", "")
print(url_2)
#url_3 = url_2.replace(".com", "")
url_3 = url_2[:url_2.index(".")]
print(url_3)
# print(url_3[:3])
# print(len(url_3))
# print(url_3.count("e"))
# print(url_3[:3] + str(len(url_3)) + "!")
# print(url_3[:3] + str(url_3.count("e")) + "!")
# print(url_3[:3] + str(len(url_3)) + str(url_3.count("e")) + "!")
password = url_3[:3] + str(len(url_3)) + str(url_3.count("e")) + "!"
print(f"{url_1}'s password is {password}.")
