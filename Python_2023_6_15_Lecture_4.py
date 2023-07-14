# Python_2023_6_15_Lecture_4

# list []
subway_1 = 10
subway_2 = 20
subway_3 = 30
subway = [10, 20, 30]
subway = ["Hyojung", "Jihyun", "Dana"]
print(subway)
print(subway.index("Hyojung"))
print(subway.index("Jihyun"))
print(subway.index("Dana"))
# print(subway.index("Kim"))
subway.append("Kim")
print(subway)
subway.insert(1, "Ha")
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
# print(subway.pop())
# print(subway)
subway.append("Hyojung")
print(subway)
subway.append("Hyojung")
print(subway)
print(subway.count("Hyojung"))
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
num_list.clear()
print(num_list)
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)
mix_list = ["Hyojung", 20, True]
print(mix_list)
num_list.extend(mix_list)
print(num_list)

# Dictionary
cabinet = {3: "Hyojung", 100: "Jihyun"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
# print(cabinet[5])
print(cabinet.get(5))
print(3 in cabinet)
print(5 in cabinet)
cabinet = {"A-3": "Hyojung", "B-100": "Jihyun"}
print(cabinet["A-3"])
print(cabinet["B-100"])
cabinet["A-3"] = "Kim"
cabinet["B-100"] = "Ha"
print(cabinet)
del cabinet["A-3"]
print(cabinet)
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())
cabinet.clear()
print(cabinet)

# Tuple